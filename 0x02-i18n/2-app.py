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
