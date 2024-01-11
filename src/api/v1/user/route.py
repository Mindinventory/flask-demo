from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from src.api.v1.user import controller


user = Blueprint('user', __name__)


@user.route('/<int:user_id>', methods=['GET', "PUT"])
@jwt_required()
def get_user_info(user_id):
    if request.method == "PUT":
        return controller.update_user(user_id=user_id)
    elif request.method == "GET":
        return controller.get_user_info(user_id=user_id)


@user.route('', methods=['POST'])
def create_user():
    return controller.create_user()
