#!/usr/bin/env python3
"""BasicAuth module"""
from api.v1.auth.auth import Auth
from typing import Tuple, TypeVar
from models.user import User
import base64


class BasicAuth(Auth):
    """declaration of class BasicAuth"""
