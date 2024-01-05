from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from .routes.route import register_blueprints

from config.config import Config


app = Flask(__name__)

# Configrations
app.config.from_object(Config)

# Db connecation and migrations
db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)

# import models
from .models import model

# CORS
CORS(app)

# Register blueprints here
register_blueprints(app)
