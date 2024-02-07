#!/usr/bin/env python3
'''
This module is a flask application for a single route.
'''
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from typing import List, Union, Dict
# from pytz import timezone, exceptions
import pytz
from datetime import datetime
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    A configuration class to specify the languages for the app
    and other default configurations.
    """
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'


app.config.from_object(Config)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Get user login details based on the ID passed in the URL parameter"""
    user_id = request.args.get('login_as')
    if user_id is not None and int(user_id) in users:
        # return users[int(user_id)]["name"]
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """
    This function will execute before all other functions.
    specifically for user login.
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Returns a locale object for any language"""
    if 'locale' in request.args and \
            request.args['locale'] in app.config['LANGUAGES']:
        return request.args['locale']
    elif g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    elif 'locale' in request.headers and \
            request.headers['locale'] in app.config['LANGUAGES']:
        return request.headers['locale']
    else:
        return Config.BABEL_DEFAULT_LOCALE


@babel.timezoneselector
def get_timezone():
    """Get locale time"""
    try:
        if 'timezone' in request.args and request.args.get('timezone') and pytz.timezone:
            return request.args['timezone']
        elif g.user and g.user.get('timezone') and pytz.timezone:
            return g.user.get('timezone')
        else:
            return app.config['BABEL_DEFAULT_TIMEZONE']
    except pytz.exceptions.UnknownTimeZoneError:
        raise


@app.route('/')
def index() -> str:
    """
    The route to the home page of the app.
    """
    if g.user:
        time = format_datetime(datetime.now())
        return render_template(
                'index.html',
                username=g.user.get('name'),
                current_time=time)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
