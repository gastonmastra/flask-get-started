import os
import click

class Config(object):
   ENV = os.environ["ENV"] if "ENV" in os.environ else "DEVELOPMENT"
   CSRF_ENABLED = True
   SECRET_KEY = "this_is_a_secret_key"
   SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
   DEBUG = True
   SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://" + os.environ["DB_USERNAME"] + ":" \
                             + os.environ["DB_PASSWORD"] + "@" \
                             + os.environ["DB_HOST"] + ":" \
                             + os.environ["DB_PORT"] + "/" \
                             + os.environ["DB_DATABASE"]
   click.echo(SQLALCHEMY_DATABASE_URI)

class TestingConfig(Config):
   DEBUG = False
   SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://" + os.environ["DB_USERNAME"] + ":" \
                             + os.environ["DB_PASSWORD"] + "@" \
                             + os.environ["DB_HOST"] + ":" \
                             + os.environ["DB_PORT"] + "/" \
                             + os.environ["DB_DATABASE"]
   
def get_environment_config():
   print(Config.ENV)
   if Config.ENV == "TESTING":
       return "config.TestingConfig"
   elif Config.ENV == "DEVELOPMENT":
       return "config.DevelopmentConfig"
   