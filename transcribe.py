from __future__ import print_function
import time
import boto3
transcribe = boto3.client('transcribe')
job_name = "superman"
job_uri = "https://aiml-labs.s3.amazonaws.com/Superman_The_Dark_Evil.mp3"
transcribe.start_transcription_job(
    TranscriptionJobName = job_name,
    Media = {'MediaFileUri': job_uri},
    MediaFormat = 'mp3',
    LanguageCode='en-US',
)

while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Not done yet!")
    time.sleep(5)