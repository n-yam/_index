import atexit

from flask import Flask, send_from_directory
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler

from index import config
from index.jobs import dbresetter
from index.controllers.card_controller import card_controller
from index.controllers.question_controller import question_controller

application = Flask(__name__, static_folder="static")
application.register_blueprint(card_controller)
application.register_blueprint(question_controller)


@application.route("/<path:path>")
def serve_static_files(path):
    return send_from_directory(application.static_folder, "index.html")


CORS(
    application,
    resources={
        r"/api/*": {"origins": config.CORS_ORIGINS},
        r"/images/*": {"origins": config.CORS_ORIGINS},
    },
)

# Setup scheduler
scheduler = BackgroundScheduler()

run_date = dbresetter.get_run_date()
scheduler.add_job(dbresetter.run, "date", run_date=run_date, args=[scheduler])
print("Questions will be reset at {}".format(run_date))

scheduler.start()

atexit.register(scheduler.shutdown)
