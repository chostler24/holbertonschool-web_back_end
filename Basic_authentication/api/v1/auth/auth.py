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
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True

        path = path.rstrip('/')
        excluded_paths = [p.rstrip('/') for p in excluded_paths]

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """Public method returns None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Public method returns None"""
        return None
