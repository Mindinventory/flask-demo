from src.api.v1.user.models import User
from src.db.session import db
from src.general.hash_utils import Hasher


def get_user_by_email(email: str):
    user = db.session.query(
        User
    ).filter(
        User.email == email
    )
    return user.first()
