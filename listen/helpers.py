import os
import requests
import time
import uuid

import boto3
from botocore.exceptions import ClientError


def load_json_from_uri(uri):
    return requests.get(uri).json()


def transcribe(job_uri):
    """Wrapper for AWS Transcribe API"""
    transcribe = boto3.client(
        "transcribe",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name="us-west-1",
    )
    job_name = str(uuid.uuid4())
    # job_uri = f'https:///really-listening-client-uploads.s3-us-west-1.amazonaws.com/{filename}'
    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={"MediaFileUri": job_uri},
        # MediaFormat='mp3',
        LanguageCode="en-US",
    )
    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status["TranscriptionJob"]["TranscriptionJobStatus"] in [
            "COMPLETED",
            "FAILED",
        ]:
            break
        print(status)
        time.sleep(5)
    return status


def comprehend():
    """Wrapper for AWS Comprehend API"""
    pass
