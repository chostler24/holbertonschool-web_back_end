#!/usr/bin/env python3
"""Encrypts a password using a one string argument"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a salted, hashed password as a byte string"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(
        password.encode('utf-8'), salt
    )
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Returns a boolean is password is encrypted"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
