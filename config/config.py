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

class JWTSettings:
    ACCESS_TOKEN_EXPIRE_TIME_MINUTES = environ.get("ACCESS_TOKEN_EXPIRE_TIME_MINUTES")
    REFRESH_TOKEN_EXPIRE_TIME_HOURS = environ.get("REFRESH_TOKEN_EXPIRE_TIME_HOURS")
    JWT_ALGORITHM = environ.get("JWT_ALGORITHM")
    AUTH_SECRET_KEY = environ.get("AUTH_SECRET_KEY")
