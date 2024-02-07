#!/usr/bin/env python3
"""Sets up a locale marker"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import List
import pytz


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
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app.config.from_object(Config)


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


@babel.localeselector
def get_locale() -> str:
    """Returns a locale object for any language"""
    if 'locale' in request.args and \
            request.args['locale'] in app.config['LANGUAGES']:
        return request.args['locale']
    elif g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    # locale from request header
    elif 'locale' in request.headers and \
            request.headers['locale'] in app.config['LANGUAGES']:
        return request.headers['locale']
    # Return default locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Get locale time"""
    try:
        if 'timezone' in request.args and request.args.get('timezone') and \
                pytz.timezone(request.args.get('timezone')):
            return request.args['timezone']
        elif g.user and g.user.get('timezone') and \
                pytz.timezone(request.args.get('timezone')):
            return g.user.get('timezone')
        else:
            return app.config['BABEL_DEFAULT_TIMEZONE']
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


if __name__ == '__main__':
    app.run(debug=True)
