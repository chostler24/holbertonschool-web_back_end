#!/usr/bin/env python3
"""module for flask view that handles session auth"""
from flask import Blueprint, request, jsonify
from models.user import User
from api.v1.app import auth
from api.v1.views import app_views

session_auth = Blueprint('session_auth', __name__, url_prefix='/api/v1')

@app_views.route('/auth_session/login', methods=['POST'])
def session_login():
    """
    Handle user login using session authentication.

    Returns:
        Response: JSON response containing the user information if login is successful,
                  or an error message with the appropriate status code.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    user_data = user.to_json()
    response = jsonify(user_data)
    response.set_cookie(auth.SESSION_NAME, session_id)

    return response
