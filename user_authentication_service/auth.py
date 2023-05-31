#!/usr/bin/env python3
"""Module for authorization"""
from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register user function"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))


def _hash_password(password: str) -> str:
    """Password slinging hasher"""
    return hashpw(password.encode(), gensalt())
