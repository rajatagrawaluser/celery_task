
import time
import task2


def perform_calculation(args):
    task = args.get("task")
    total_steps = args.get("total_steps")
    for i in range(total_steps):
        print(task2.add(1,1))
        time.sleep(1)
        # Simulate a long-running operation
        if task.request.get("id"):
            task.update_state(state='PROGRESS', meta={'current': i, 'total': total_steps})

    return total_steps
