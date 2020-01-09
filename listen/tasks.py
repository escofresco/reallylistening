from __future__ import absolute_import, unicode_literals
from config.celery_app import app
from celery import shared_task

import threading

@shared_task
def add(x, y):
    threading.Event().wait(5)
    return x + y
