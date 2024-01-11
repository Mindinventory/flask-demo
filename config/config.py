from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(".env")
load_dotenv(basedir)

class Config:
    FLASK_ENV = environ.get("FLASK_ENV")
    FLASK_DEBUG = environ.get("FLASK_DEBUG")
    HOST =  environ.get("HOST")
    PORT = environ.get("PORT")

    DB_USER = environ.get("DB_USER")
    DB_PASSWORD = environ.get("DB_PASSWORD")
    DB_HOST = environ.get("DB_HOST")
    DB_NAME = environ.get("DB_NAME")
    DB_PORT = environ.get("DB_PORT")
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    JWT_ACCESS_TOKEN_EXPIRES = environ.get("JWT_ACCESS_TOKEN_EXPIRES")
    JWT_REFRESH_TOKEN_EXPIRES = environ.get("JWT_REFRESH_TOKEN_EXPIRES")
    JWT_ALGORITHM = environ.get("JWT_ALGORITHM")
    JWT_SECRET_KEY = environ.get("JWT_SECRET_KEY")

    
