#!/usr/bin/env python3
"""Encrypts a password using a one string argument"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a salted, hashed password as a byte string"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
