from celery import Celery
from celery.signals import beat_init, worker_process_init

import config

celery_app = Celery(__name__)
settings = config.get_settings()

REDIS_URL = settings.redis_url


celery_app.conf.broker_url = REDIS_URL
celery_app.conf.result_backend = REDIS_URL


def celery_on_startup(*args, **kwargs):
    print("Hello world")


beat_init.connect(celery_on_startup)
worker_process_init.connect(celery_on_startup)

@celery_app.task
def random_task(name):
    print(f"Who throws a shoe. Honestly {name}.")


