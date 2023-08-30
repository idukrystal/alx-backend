#!/usr/bin/env python3
""" A simple flask apllication with flask_babel """

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Configuratuon class for babel """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ Selects best language for user  """

    incoming_request = request.query_string.decode('utf-8').split('&')
    request_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        incoming_request,
    ))

    if 'locale' in request_table:
        if request_table['locale'] in app.config["LANGUAGES"]:
            return request_table['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
@app.route('/index')
def index() -> str:
    """ Renders homepage of web app uses babel to support translation """

    return render_template("4-index.html")
