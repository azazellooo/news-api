from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import reset_votes


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(reset_votes, 'interval', hours=24)
    scheduler.start()

