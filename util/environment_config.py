import os
from dotenv import load_dotenv

CONST_ALLOWED_ENVIRONMENTS = ["DEV", "TST", "ACC", "PROD"]

class EnvironmentConfig:
    environment: str

    mysql_host: str
    mysql_database: str
    mysql_user: str
    mysql_password: str

    country_api_wsdl_url: str

    def __init__(self):
        load_dotenv()
        self.load_environment()

    def get_variable(self, env_variable: str):
        if(env_variable not in os.environ):
            raise Exception(f"Failed to load {env_variable} from environment variables")
        return os.environ[env_variable]

    def load_environment(self):
        self.environment = self.get_variable("ENV")
        if(self.environment not in CONST_ALLOWED_ENVIRONMENTS):
            raise Exception(f"ENV in environment variables does not contain a valid value. Received: {self.environment}, Expected: {", ".join(CONST_ALLOWED_ENVIRONMENTS)}")
        
        self.mysql_host = self.get_variable("MYSQL_HOST")
        self.mysql_database = self.get_variable("MYSQL_DATABASE")
        self.mysql_user = self.get_variable("MYSQL_USER")
        self.mysql_password = self.get_variable("MYSQL_PASSWORD")
        self.country_api_wsdl_url = self.get_variable("COUNTRY_API_WSDL_URL")


        
        

