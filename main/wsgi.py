from flask import Flask
from flask import request

app = Flask(__name__)


@app.post("/api/cards")
def card_post():
    frontText = request.form["frontText"]
    backText = request.form["backText"]

    json = {
        "frontText": frontText,
        "backText": backText,
    }

    return json


def get_app():
    return app
