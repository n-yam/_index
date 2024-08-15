from flask import Flask

from index.controllers.card_controller import card_controller
from index.controllers.question_controller import question_controller

app = Flask(__name__)
app.register_blueprint(card_controller)
app.register_blueprint(question_controller)
