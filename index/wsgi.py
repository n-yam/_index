from flask import Flask
from sqlalchemy.orm import declarative_base

from index.controllers.deck_controller import deck_controller

app = Flask(__name__)
Base = declarative_base()

app.register_blueprint(deck_controller)


def get_app():
    return app
