from os import environ,path
from dotenv import load_dotenv

load_dotenv()


DEBUG =False
# DEVELOPMENT = True
SECRET_KEY = environ.get('SECRET_KEY')
FLASK_APP = environ.get('FLASK_APP')
FLASK_ENV = environ.get('FLASK_ENV')

SQLALCHEMY_DATABASE_URI = environ["DATABASE_URL"]
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
