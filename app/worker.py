import os
import time
import sys
# sys.path.append("/usr/src/app/tasks")
sys.path.append(os.getcwd()+"/app/tasks")
from app.tasks.task import perform_calculation
from app.tasks.task2 import add

add(2,2)

from celery import Celery

# PyInstaller friendly imports --start--
import celery.app.amqp
import celery.app.log
import celery.worker.autoscale
import celery.worker.components
import celery.bin
import celery.utils
import celery.utils.dispatch
import celery.contrib.testing
import celery.utils.static
import celery.concurrency.prefork
import celery.app.events
import celery.events.state
import celery.app.control
import celery.backends.redis
import celery.backends
import celery.backends.database
import celery.worker
import celery.worker.consumer
import celery.app
import celery.loaders
import celery.security
import celery.fixups
import celery.concurrency
import celery.events
import celery.contrib
import celery.apps
import celery
import celery.fixups
import celery.fixups.django
import celery.apps.worker
import celery.worker.strategy
import kombu.transport.redis
import sqlalchemy.sql.default_comparator               
import sqlalchemy.ext.baked
# PyInstaller friendly imports --end--


celery = Celery('tasks',
            broker="redis://localhost:6379",
            backend="redis://localhost:6379")


@celery.task(bind=True)
def create_task(self,**data):
    data.update({"task":self})
    result = perform_calculation(data)
    return result
