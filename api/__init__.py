from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from api.config import Config

api_app = Flask(__name__)

api_app.config.from_object(Config)

db = SQLAlchemy(api_app)
migrate = Migrate(api_app, db)

from api import routes