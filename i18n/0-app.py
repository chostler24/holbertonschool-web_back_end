#!/usr/bin/env python3
"""Module for basic Flask app"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    """function returns rendering of index file"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
