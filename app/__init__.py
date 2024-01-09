from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from werkzeug.exceptions import BadRequest
from marshmallow import ValidationError

from .routes.route import register_blueprints

from config.config import Config
from .db.session import db

app = Flask(__name__)

# Configrations
app.config.from_object(Config)

# Db connecation and migrations
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)

# import models
from .models import model

# CORS
CORS(app)

# Register blueprints here
register_blueprints(app)
