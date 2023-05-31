#!/usr/bin/env python3
"""Module for class session auth"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Function user_id_for_session_id returns user_id for session_id"""
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Retrieve a User instance based on a cookie value.

        Args:
            request: The request object containing the session cookie.

        Returns:
            User: The User instance associated with the session cookie,
            or None if the cookie or user is not found.

        """
        cookie_value = self.session_cookie(request)
        if cookie_value:
            user_id = self.user_id_for_session_id(cookie_value)
            if user_id:
                return User.get(user_id)
        return None

    def destroy_session(self, request=None):
        """
        Deletes the user session/logout.

        Args:
            request: The request object containing the session cookie.

        Returns:
            bool: True if the session was successfully destroyed, False otherwise.

        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if not session_id:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False

        del self.user_id_by_session_id[session_id]
        return True
