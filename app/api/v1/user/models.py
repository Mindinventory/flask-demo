from sqlalchemy import func

from ....db.session import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(), default=func.sysdate())
    updated_at = db.Column(db.DateTime(), default=func.sysdate(), onupdate=func.sysdate())
