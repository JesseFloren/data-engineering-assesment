import math
from dtos.country import Country
from services.country_api_service import CountryApiService
from services.country_database_service import DatabaseService
from util.logger import Logger
from util.environment_config import EnvironmentConfig

config = EnvironmentConfig()
logger = Logger(config)

def main():
    country_api_service = CountryApiService(config, logger.get_scope("CountryApiService"))
    db_service = DatabaseService(config, logger.get_scope("DatabaseService"))

    countries = country_api_service.get_countries()
    formatted_countries = list(map(replace_symbol_to_and, countries))
    
    db_service.create_countries_table_if_not_exist()

    logger.info("Starting a refresh of country table contents")
    db_service.clear_country_table()
    db_service.insert_into_country(formatted_countries)
    logger.info("Refreshed country")

    # Python selection of first 10 countries
    first_10_countries = formatted_countries[:10]
    logger.info("PYTHON OUTPUT")
    logger.info(first_10_countries)

    # SQL selection of first 10 countries
    output = db_service.select_first_10_countries()
    logger.info("SQL OUTPUT")
    logger.info(output)    
    

def replace_symbol_to_and(country: Country):
    old: str = country.name
    new: str = old.replace("&", "and")
    if(old != new): logger.debug(f"Country name replaced. Old: {old}, new: {new}")
    return Country(new, country.iso_code)


if __name__ == "__main__":
    main()
