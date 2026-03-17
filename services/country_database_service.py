import os
import mysql.connector
from mysql.connector import MySQLConnection

from dtos.country import Country
from util.environment_config import EnvironmentConfig
from util.logger import Logger


SQL_CREATE_COUNTRY_TABLE_IF_NOT_EXISTS = "create_country_table_if_not_exists.sql"
SQL_INSERT_INTO_COUNTRY = "insert_into_country_table.sql"
SQL_SELECT_FIRST_10_COUNTRIES = "select_first_10_countries.sql"

def sql_path_from_working_directory(path: str):
    return os.path.join(os.getcwd(), "sql", path) 

def read_sql_file(path: str) -> str:
    file = open(sql_path_from_working_directory(path), 'r')
    return file.read()

class DatabaseService:
    db: MySQLConnection
    logger: Logger

    def __init__(self, config: EnvironmentConfig, logger: Logger):
        self.logger = logger
        try: 
            self.db = mysql.connector.connect(
                host=config.mysql_host,
                user=config.mysql_user,
                password=config.mysql_password,
                database=config.mysql_database
            )
            logger.debug("Succesfully created database connection")
        except Exception as e:
            logger.error("Database connection failed")
            raise e         
    
    def clear_country_table(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("DELETE FROM country")
            self.db.commit()
        except Exception as e:
            self.logger.error("Failed to clear contents from country table")
            raise e

    def create_countries_table_if_not_exist(self):
        try:
            sql = read_sql_file(SQL_CREATE_COUNTRY_TABLE_IF_NOT_EXISTS)
            cursor = self.db.cursor()

            cursor.execute(sql)
            self.db.commit()

            self.logger.debug("Succesfully executed create table if not exist")
        except Exception as e:
            self.logger.error("Failed to create the country table")
            raise e
            

    def insert_into_country(self, countries: list[Country]):
        try:
            sql = read_sql_file(SQL_INSERT_INTO_COUNTRY)
            cursor = self.db.cursor()

            for country in countries:
                cursor.execute(sql, [country.name, country.iso_code])
            self.db.commit()

            self.logger.debug("Succesfully executed insert into table")
        except Exception as e:
            self.logger.error(f"Failed to insert countries into table. Input: {countries}")
            raise e

    
    def select_first_10_countries(self):
        try:
            sql = read_sql_file(SQL_SELECT_FIRST_10_COUNTRIES)
            cursor = self.db.cursor()

            cursor.execute(sql)
            first_10_rows = cursor.fetchall()

            return list(map(lambda x: Country(x[2], x[1]), first_10_rows))
        except Exception as e:
            self.logger.error("Failed to get the first 10 countries from the database")
            raise e
