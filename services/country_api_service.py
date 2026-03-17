from zeep import Client

from dtos.country import Country
from util.environment_config import EnvironmentConfig
from util.logger import Logger

class CountryApiService:
    soap_client: Client

    def __init__(self, config: EnvironmentConfig, logger: Logger):
        try:
            self.soap_client = Client(config.country_api_wsdl_url)
            logger.debug(f"Succesfully created soap client for {config.country_api_wsdl_url}")
        except Exception as e:
            logger.error(f"Failed to create a soap client for {config.country_api_wsdl_url}")
            raise e

    def get_countries(self) -> list[Country]:
        countries = self.soap_client.service.ListOfCountryNamesByCode()
        map_country_to_dto = lambda x: Country(x["sName"], x["sISOCode"])
        return list(map(map_country_to_dto, countries))