import atexit
from datetime import datetime, timedelta

from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

from index import config, jobs
from index.controllers.card_controller import card_controller
from index.controllers.question_controller import question_controller

app = Flask(__name__)
app.register_blueprint(card_controller)
app.register_blueprint(question_controller)


def get_run_date():
    now = datetime.now()
    configured_time = datetime.strptime(config.QUESTION_RESET_TIME, config.TIME_FORMAT)

    base_time = now.replace(
        hour=configured_time.hour,
        minute=configured_time.minute,
        second=configured_time.second,
        microsecond=0,
    )

    if now >= base_time:
        next = base_time + timedelta(days=1)
    else:
        next = base_time
    return next


run_date = get_run_date()
print("Job is going to start at {}".format(run_date))

scheduler = BackgroundScheduler()
scheduler.add_job(jobs.start, "date", run_date=run_date, args=[scheduler])
scheduler.start()


def cleanup():
    scheduler.shutdown()
    print("Background jobs have been successfully terminated")


atexit.register(cleanup)
