#!/usr/bin/env python3
"""Module for authorization"""
from bcrypt import hashpw, gensalt, checkpw
from db import DB


def _hash_password(password: str) -> str:
    """Password slinging hasher"""
    return hashpw(password.encode(), gensalt())
