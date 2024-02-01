from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from config.config import Config
from src.db.session import db
from src.routes.route import register_blueprints


app = Flask(__name__)

# Configrations
app.config.from_object(Config)

# Db connecation and migrations
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)

# JWT
jwt = JWTManager(app)

# import models
from src.db import model

# CORS
CORS(app)

# Register blueprints here
register_blueprints(app)
