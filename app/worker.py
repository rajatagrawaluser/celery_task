import os
import time

from celery import Celery

celery = Celery('tasks',
            broker="redis://localhost:6379",
            backend="redis://localhost:6379")


@celery.task(bind=True)
def create_task(self,**data):
    args = data
    args.update({"task":self})
    result = perform_calculation(args)
    return result

def perform_calculation(args):
    task = args.get("task")
    total_steps = args.get("total_steps")
    for i in range(total_steps):
        time.sleep(1)
        # Simulate a long-running operation
        if task:
            task.update_state(state='PROGRESS', meta={'current': i, 'total': total_steps})

    return total_steps
