import schedule
import time

def task_to_do():
    print("It's time to do your task!")

# Schedule the task to run every minute (for testing purposes)
schedule.every(1).minute.do(task_to_do)

while True:
    schedule.run_pending()
    time.sleep(1)
