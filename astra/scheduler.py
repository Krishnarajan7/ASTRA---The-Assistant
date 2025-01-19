import schedule
import time

def job():
    print("Running scheduled task...")

def schedule_task():
    """Schedule tasks."""
    schedule.every(1).hour.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
