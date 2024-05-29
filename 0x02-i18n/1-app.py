#!/usr/bin/env python3
""" Module for Second Flask Task """

from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """a Config class that has a LANGUAGES class attribute
    equal to ["en", "fr"]"""
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
babel = Babel(app, default_locale=Config.LANGUAGES, default_timezone="UTC")


@app.route('/', strict_slashes=False)
def home_route() -> str:
    """simply outputs “Welcome to Holberton” as page title (<title>)
    and “Hello world” as header (<h1>)"""
    return render_template('1-index.html')


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
