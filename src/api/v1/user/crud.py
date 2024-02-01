from src.api.v1.user.models import User
from src.db.session import db
from src.utils.hash_utils import Hasher


def create_user(input_data: dict):
    new_user = User(
        username=input_data.get("username"),
        email=input_data.get("email"),
        password=Hasher().hash_password(input_data.get("password")),
        first_name=input_data.get("first_name"),
        last_name=input_data.get("last_name")
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user


def get_user_id(user_id: int):
    user = db.session.query(
        User
    ).filter(
        User.id == user_id
    )
    return user.first()


def update_user(input_data: dict, user_id: int):
    user = get_user_id(user_id=user_id)
    if user:
        for key, value in input_data.items():
            setattr(user, key, value)
        db.session.commit()
    return True
