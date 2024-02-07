#!/usr/bin/env python3
"""Sets up a locale marker"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Configures language marker"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """Returns a locale object for any language"""
    user_setting = 'fr'
    if 'locale' in request.args and \
            request.args['locale'] in app.config['LANGUAGES']:
        return request.args['locale']
    elif user_setting and user_setting in app.config['LANGUAGES']:
        return user_setting
    elif 'locale' in request.headers and \
            request.headers['locale'] in app.config['LANGUAGES']:
        return request.headers['locale']
    else:
        return Config.BABEL_DEFAULT_LOCALE


@app.route('/', methods=['GET'])
def index_page() -> str:
    """Defines an index page"""
    return render_template('6-index.html')


@app.before_request
def before_request():
    """A function that delays in order to be able
       to get user login details into gettext
    """
    # g.username = get_user()
    g.user = get_user()


def get_user():
    """Get user login details based on the ID passed in the URL parameter"""
    user_id = request.args.get('login_as')
    if user_id is not None and int(user_id) in users:
        # return users[int(user_id)]["name"]
        return users[int(user_id)]
    return None


if __name__ == '__main__':
    app.run(debug=True)
