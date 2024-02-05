from flask_apscheduler import APScheduler
from .database import check_and_update_client_status


def init_tasks(app):
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.add_job(id='job_sync', func=status_handler, args=[app], trigger='interval', seconds=60)
    scheduler.start()


def status_handler(app):
    with app.app_context():
        print("Running background task...")
        check_and_update_client_status()
        
