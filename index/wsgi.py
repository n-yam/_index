import atexit

from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

from index.jobs import resetter
from index.controllers.card_controller import card_controller
from index.controllers.question_controller import question_controller

application = Flask(__name__)
application.register_blueprint(card_controller)
application.register_blueprint(question_controller)

# Setup scheduler
scheduler = BackgroundScheduler()

run_date = resetter.get_run_date()
scheduler.add_job(resetter.run, "date", run_date=run_date, args=[scheduler])
print("Questions will be reset at {}".format(run_date))

scheduler.start()

atexit.register(scheduler.shutdown)
