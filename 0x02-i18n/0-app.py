#!/usr/bin/env python3
""" A basic flask application """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ View function for Hompage """
    return render_template("0-index.html")
