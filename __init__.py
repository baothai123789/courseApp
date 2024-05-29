from flask import Flask
from .config import Config,DevEnvConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData


convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)
migrate = Migrate()
def create_app(config_class=Config):
    newApp = Flask(__name__)
    newApp.config.from_object(config_class)
    db.init_app(newApp)
    migrate.init_app(newApp, db,render_as_batch=True)
    return newApp


app = create_app(DevEnvConfig)

from . import routes
from . import model
