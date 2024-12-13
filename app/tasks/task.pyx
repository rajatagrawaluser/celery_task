
import time


def perform_calculation(args):
    task = args.get("task")
    total_steps = args.get("total_steps")
    for i in range(total_steps):
        time.sleep(1)
        # Simulate a long-running operation
        if task.request.get("id"):
            task.update_state(state='PROGRESS', meta={'current': i, 'total': total_steps})

    return total_steps
