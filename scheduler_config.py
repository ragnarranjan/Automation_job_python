from apscheduler.schedulers.background import BackgroundScheduler
from jobs import print_hi

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(print_hi, 'interval', minutes=30)
    scheduler.add_job(print_hi, 'interval', seconds=30, id='hi_every_30s_1')

    scheduler.start()
    return scheduler
