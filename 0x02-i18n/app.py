#!/usr/bin/env python3
""" A simple flask apllication with flask_babel """

from flask import Flask, g, render_template, request
from flask_babel import Babel, format_datetime
from typing import Dict, Union
import pytz


class Config:
    """ Configuratuon class for babel """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """ returns user details from http request """
    if "login_as" in request.args:
        login_id = request.args["login_as"]
        if login_id.isdigit() and int(login_id) in users:
            return users[int(login_id)]
    return None


@app.before_request
def before_request() -> None:
    """ Excutes befofe app start tries to get a user """
    user = get_user()
    if user is not None:
        g.user = user


@babel.localeselector
def get_locale() -> str:
    """ Selects best language for user  """

    request_table = request.args
    if 'locale' in request_table:
        if request_table['locale'] in app.config["LANGUAGES"]:
            return request_table['locale']
    user = get_user()
    if user:
        locale = user.get('locale')
        if locale is not None and locale in app.config["LANGUAGES"]:
            return user.get('locale')
    locale = request.headers.get('locale')
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone():
    timezone = app.config['BABEL_DEFAULT_TIMEZONE']
    user = get_user()
    if user and user.get('timezone'):
        if user.get('timezone') in pytz.all_timezones:
            timezone = user.get('timezone')
    if 'timezone' in request.args:
        if request.args['timezone'] in pytz.all_timezones:
            timezone = request.args['timezone']
    return pytz.timezone(timezone).zone


@app.route('/')
@app.route('/index')
def index() -> str:
    """ Renders homepage of web app uses babel to support translation """

    date = format_datetime()
    return render_template("index.html", date=str(date))
