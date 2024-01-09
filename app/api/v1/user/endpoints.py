from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from . import schema 
from . import crud
from config.logger import logger
from ....general.response import success_response, error_response, get_message
from ....general.helper import getting_schema_error

user = Blueprint('user', __name__)


@user.route('/<int:user_id>', methods=['GET'])
def get_user_info(user_id):
    try:
        user = crud.get_iser_id(user_id)
        if not user:
            return error_response(get_message("common_error", "user_not_exists"), 404)
        return success_response(schema.UserResponse().dump(user), "User details retrieved successfully")
    except Exception as e:
        logger.error(f"Internal server error: {e.args}")
        return error_response(get_message("internal_server", "internal"), 500)

@user.route('', methods=['POST'])
def create_user():
    try:
        input_data = request.get_json()
        try:
            user_data = schema.UserCreate()
            user_data.load(input_data)
        except ValidationError as e:
            return error_response(getting_schema_error(e))
        crud.create_user(input_data)
        return success_response(None, "User created successfully")
    except Exception as e:
        logger.error(f"Internal server error: {e.args}")
        return error_response(get_message("internal_server", "internal"), 500)
