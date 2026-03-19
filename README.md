# Data Engineering Assesment
This repository contains a execution of the assesment given by the ${Company} for the Data Engineering position. 

## The Assesment
The assignment contains the following tasks:
- Retrieving country from the following SOAP service: ``http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL``.
- Replacing the ``&`` symbol in the names of countries with ``"and"``.
- Creating a table for the countries inside a docker instantiated PostgreSQL or MySQL database.
- Inserting the countries into the database.
- Then retrieving and ouputting the first ten countries in the database.

## How to run the program?
1. Host the MySQL database using the following command (Make sure that docker is already installed on your device): 
```bash 
docker run -d -p 3306:3306 \
    --name mysql-docker-container \
    -e MYSQL_ROOT_PASSWORD=w8woord \
    -e MYSQL_DATABASE=codetest \
    -e MYSQL_USER=gebruikersnaam \
    -e MYSQL_PASSWORD=w8woord \
    mysql/mysql-server:latest
```
2. Clone this repository
3. Create a ``.env`` file in the root of the folder and add the following contents (Warning: This is only for development purposes) 
```
ENV="DEV"

MYSQL_DATABASE="codetest"
MYSQL_USER="gebruikersnaam"
MYSQL_PASSWORD="w8woord"
MYSQL_HOST="localhost"

COUNTRY_API_WSDL_URL="http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
```
4. Instantiate a virtual environment with conda or a standard ``.venv``.
5. Install the required packages with ``pip install -r requirements.txt``.
6. run the ``main.py`` file using the command: ``python main.py``

## Services
### Country Api Service
The Country API service is the layer that should implement all calls made to the SOAP api that target endpoints related to countries. Targeting the API outside of this service should be avoided at all cost. This makes sure the handling of the Api is centralized.

### Database Service
The Database Service is the layer that interacts with the MySQL database. Every unique interaction with the database should have a function defined within this service. This guarentees readibility and clear boundries between the responsibility of a singular method. All interactions with the database should be avoided at all costs outside of the Database Service.

## Utilities
### Environment Config
Environment config is a simple implementation for the extraction of environment variables. It also loads ``.env`` files. The usage of environment variables should be minimized outside the environment config. This guarentees that there is a single origin of environment variables inside the program.

### Logger
Logger implements a very lightweight logger that provides simple error/warning/info/debug logs. As well as scoping of the logger. Scopes can be used to provide services a logger that will always be easily identitfy the origin serivce in its logs.

## Dto's
### Country Dto
The Country Dto is a helper that makes it possible that every service in the program has the same understanding for the definition of a Country. When a service requires countries as inputs it should require it to be Country Dto class. Same when a service returns countries. it should always return this class. This provides consistancy and less data transformations outside of the services.