from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)


class Config(object):
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    return users.get(user_id)


@app.before_request
def before_request():
    user_id = request.args.get('login_as')
    if user_id:
        g.user = get_user(int(user_id))
    else:
        g.user = None


@app.route('/')
def index():
    if g.user:
        welcome_message = gettext(
            'You are logged in as %(username)s.') % {
                'username': g.user['name']}
    else:
        welcome_message = gettext('You are not logged in.')
    return render_template('4-index.html', welcome_message=welcome_message)


@babel.localeselector
def get_locale():
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
