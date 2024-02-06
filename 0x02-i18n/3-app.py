#!/usr/bin/env python3
"""Sets up a locale marker"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', methods=['GET'])
def index_page():
    title = _("home_title")
    message = _("home_header")
    return render_template('3-index.html', title=title, message=message)

if __name__ == '__main__':
    app.run()
