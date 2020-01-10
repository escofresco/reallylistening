from __future__ import absolute_import, unicode_literals

from config.celery_app import app
from celery import shared_task
from .helpers import *

import time


@shared_task
def add(x, y):
    threading.Event().wait(5)
    return x + y


@shared_task
def start_listening(filename):
    transcribe_res = transcribe(filename)
    job = transcribe_res["TranscriptionJob"]
    if job["TranscriptionJobStatus"] == "FAILED":
        raise Exception("Transcript failed to complete")
    transcribe_uri = job["Transcript"]["TranscriptFileUri"]
    transcript_res = load_json_from_uri(transcribe_uri)
    content = transcript_res["results"]["transcripts"][0]["transcript"]

    return content
