#!/usr/bin/env python3
"""Module for class session auth"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Declaration of class SessionAuth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Function create_session checks if user_id is str
        Creates session_id and stores it in dict
        Returns session_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
