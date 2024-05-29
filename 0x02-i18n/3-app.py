#!/usr/bin/env python3
""" 2. get local from request """

from typing import Optional
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config():
    """ Config class for app """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def home_route() -> str:
    """ / page """
    return render_template('3-index.html')


@babel.localeselector
def get_locale() -> Optional[str]:
    """ Get locale from request """
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
