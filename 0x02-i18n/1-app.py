#!/usr/bin/env python3
"""Set up flask app"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Configuration takes place here"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/', methods=['GET'])
def index_page() -> str:
    """Defines a route for an index page"""
    # title = "Welcome to Holberton"
    # message = "Hello world"
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
