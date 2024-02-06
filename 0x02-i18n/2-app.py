#!/usr/bin/env python3
"""Sets up flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@babel.localeselector
def get_locale():
    """Get the languages choice of an application"""
    return request.accepted_languages.best_match(
            app.config['LANGUAGES']
            )


@app.route('/', methods=['GET'])
def index_page() -> str:
    """Defines a route for an index page"""
    title = "Welcome to Holberton"
    message = "Hello world"
    return render_template('2-index.html', title=title, message=message)


if __name__ == '__main__':
    app.run()
