from flask import Flask

from index.controllers.card_controller import card_controller

app = Flask(__name__)
app.register_blueprint(card_controller)
