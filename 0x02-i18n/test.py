

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    if "lang" in request.args:
        return str(request.args["lang"])
    return str(" e mno dey")
