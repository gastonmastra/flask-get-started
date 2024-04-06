# FLASK GET STARTED
This project was made for practicing making flask applications using Graphene and SQLAlchemy

## RUN
docker compose up 

## NOTES
In this case, we set the environment variables by adding them to their corresponding services inside docker-compose. 
The database is 

SQLAlchemy connection string: As the official documentation say, the connection string follow this structure: 
`dialect+driver://username:password@host:port/database`
In this case, we are using the next values
```
dialect = postgresql
driver = psycopg2
username = test_postgress
password = Pass!123
host = db
port = 5432
database = test
```
