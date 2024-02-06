#!/usr/bin/env python3
"""Set up flask app"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index_page() -> str:
    """Defines a route for an index page"""
    # title = "Welcome to Holberton"
    # message = "Hello world"
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
