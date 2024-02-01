from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta, datetime

from config.config import Config


class Token:
    def __init__(self):
        self.access_token_expiry_time = Config().JWT_ACCESS_TOKEN_EXPIRES
        self.refresh_token_expiry_time = Config().JWT_REFRESH_TOKEN_EXPIRES

    def create_access_token(self, data: dict):
        expire = timedelta(seconds=int(self.access_token_expiry_time))
        jwt_token = create_access_token(
            identity=data.get("user_id"), additional_claims={"email": data.get("email")}, expires_delta=expire
        )
        return jwt_token
    
    def create_refresh_token(self, user_id):
        expire = timedelta(days=int(self.refresh_token_expiry_time))
        refresh_token = create_refresh_token(identity=user_id, expires_delta=expire)
        return refresh_token
