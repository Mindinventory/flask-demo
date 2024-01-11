from flask import Blueprint
from flask_jwt_extended import jwt_required

from src.api.v1.auth import controller


auth = Blueprint('auth', __name__)

@auth.route("/login", methods=["POST"])
def login():
    return controller.login()


@auth.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    return controller.refresh_token()


