#!/usr/bin/env python3
"""Module for Babel object instantiation"""
from Flask import flask
from flask_babel import Babel

app = Flask(__name__)


class Config(object):
    """declaration of class Config"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """Function renders 1-index"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
