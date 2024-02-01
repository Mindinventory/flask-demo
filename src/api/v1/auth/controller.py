from flask import request
from flask_jwt_extended import get_jwt_identity
from marshmallow import ValidationError

from src.api.v1.auth import schema, crud
from src.api.v1.user import crud as user_crud
from config.logger import logger
from src.utils.response import success_response, error_response, get_message
from src.utils.helper import getting_schema_error
from src.utils.hash_utils import Hasher
from src.utils.token_utils import Token


def login():
    """
    User login
    """
    try:
        input_data = request.get_json()
        
        try:
            login_data = schema.Login()
            login_data.load(input_data)
        except ValidationError as e:
            return error_response(getting_schema_error(e))
        
        user = crud.get_user_by_email(input_data.get("email"))
        if not user:
            return error_response(get_message("common_error", "unauthorized"), 401)

        if not Hasher().verify_password(plain_password=input_data.get("password"), hashed_password=user.password):
            return error_response(get_message("common_error", "unauthorized"), 401)

        data = dict(user_id=user.id, email=user.email)
        access_toekn = Token().create_access_token(data=data)
        refresh_token = Token().create_refresh_token(user_id=user.id)

        return success_response(schema.UserResponse().dump(user), "Login successful", access_toekn=access_toekn, refresh_token=refresh_token)
    except Exception as e:
        logger.error(f"Internal server error: {e.args}")
        return error_response(get_message("internal_server", "internal"), 500)
    

def refresh_token():
    """
    Function for getting new access token
    """
    try:
        current_user = get_jwt_identity()
        
        user = user_crud.get_user_id(current_user)
        if not user:
            return error_response(get_message("common_error", "unauthorized"), 401)

        data = dict(user_id=user.id, email=user.email)
        access_toekn = Token().create_access_token(data=data)
        return success_response(None, "Token refresh successfully", access_toekn=access_toekn)
    except Exception as e:
        logger.error(f"Internal server error: {e.args}")
        return error_response(get_message("internal_server", "internal"), 500)