from flask import request
from marshmallow import ValidationError

from src.api.v1.user import schema, crud
from config.logger import logger
from src.general.response import success_response, error_response, get_message
from src.general.helper import getting_schema_error


def get_user_info(user_id):
    try:
        user = crud.get_user_id(user_id)
        if not user:
            return error_response(get_message("common_error", "user_not_exists"), 404)
        return success_response(schema.UserResponse().dump(user), "User details retrieved successfully")
    except Exception as e:
        logger.error(f"Internal server error: {e.args}")
        return error_response(get_message("internal_server", "internal"), 500)


def update_user(user_id):
    try:
        input_data = request.get_json()
        user = crud.get_user_id(user_id)
        if not user:
            return error_response(get_message("common_error", "user_not_exists"), 404)
        
        try:
            user_data = schema.UserUpdate()
            user_data.load(input_data)
        except ValidationError as e:
            return error_response(getting_schema_error(e))
        
        crud.update_user(input_data=input_data, user_id=user_id)
        return success_response(None, "User details updated successfully")
    except Exception as e:
        logger.error(f"Internal server error: {e.args}")
        return error_response(get_message("internal_server", "internal"), 500)
    

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
