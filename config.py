from dotenv import load_dotenv
import os

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    pass


class DevEnvConfig(Config):
    db_name = os.getenv('DEV_DATABASE_URI')
    db_url = 'sqlite:///'+os.path.join(basedir, db_name)
    SQLALCHEMY_DATABASE_URI = db_url


class ProdEnvConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URI')
