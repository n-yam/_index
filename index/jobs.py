from datetime import datetime

# from apscheduler.schedulers.background import BackgroundScheduler

from index.services.question_service import QuestionService


# def start():
def start(scheduler):
    # scheduler = BackgroundScheduler()
    # scheduler.add_job(reset_questions, "interval", days=1)
    scheduler.add_job(reset_questions, "interval", seconds=1)


def reset_questions():
    service = QuestionService()
    service.reset(datetime.now())
    print("Questions has been reset successfully")
    print("Count: {}".format(service.count()))
