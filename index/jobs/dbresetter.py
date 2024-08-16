from datetime import datetime, timedelta

from index import config
from index.services.question_service import QuestionService


def run(scheduler):
    def execute():
        service = QuestionService()
        service.reset(datetime.now())
        print("Questions has been reset successfully")
        print("Count: {}".format(service.count()))

    scheduler.add_job(execute, "interval", days=1)


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
        run_date = base_time + timedelta(days=1)
    else:
        run_date = base_time

    return run_date
