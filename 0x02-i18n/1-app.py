#!/usr/bin/env python3
""" A simple flask apllication with flask_babel """

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ Configuratuon class for babel """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
@app.route('/index')
def index():
    """ Renders homepage of web app uses babe to support i18b """

    return render_template("1-index.html")
