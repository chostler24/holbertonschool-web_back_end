#!/usr/bin/env python3
"""Class to manage API authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Class declaration"""
    def __init__(self):
        """initialize"""
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Public method returns False"""
        return False

    def authorization_header(self, request=None) -> str:
        """Public method returns None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Public method returns None"""
        return None
