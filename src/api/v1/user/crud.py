from src.api.v1.user.models import User
from src.db.session import db
from src.general.hash_utils import Hasher


def create_user(input_data: dict):
    new_user = User(
        username=input_data.get("username"),
        email=input_data.get("email"),
        password=Hasher().hash_password(input_data.get("password")))
    db.session.add(new_user)
    db.session.commit()
    return new_user

def get_iser_id(user_id: int):
    user = db.session.query(
        User
    ).filter(
        User.id == user_id
    )
    return user.first()