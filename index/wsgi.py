from flask import Flask

from index.controllers.deck_controller import deck_controller

app = Flask(__name__)
app.register_blueprint(deck_controller)
