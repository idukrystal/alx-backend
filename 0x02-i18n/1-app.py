#!/usr/bin/env python3
""" A simple flask apllication with flask_babel """

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)


class Config:
    """ Configuratuon class for babel """

    LANGUAGES = ["en", "fr"]


@app.route('/')
@app.route('/indez')
def index():
    """ Renders homepage of web app uses babe to support i18b """
    babel.BABEL_DEFAULT_LOCALE = Config.LANGUAGES[0]
    babel.BABEL_DEFAULT_TIMEZONE = "UTC"

    return render_template("1-index.html")
