#!/usr/bin/env python3
"""Module for Flask initialization"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/")
def welcome():
    """ Welcome Method """
    return jsonify({"message": "Bienvenue"})
