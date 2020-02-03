from werkzeug.security import generate_password_hash, check_password_hash

from .base import db, Base

from sqlalchemy import Column, Integer, String


class User:
    __tablename__ = "db_user"
    id = Column(Integer, primary_key=True)
    email = Column(String(64), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def check_password(self, value):
        if not self.password_hash:
            return False
        return check_password_hash(self.password_hash, value)
