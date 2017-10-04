import time
from google.cloud import speech
client = speech.SpeechClient()
operation = client.long_running_recognize(
    audio=speech.types.RecognitionAudio(
        uri='gs://my-bucket/recording.flac',
    ),
    config=speech.types.RecognitionConfig(
        encoding='LINEAR16',
        language_code='en-US',
        sample_rate_hertz=44100,
    ),
)
retry_count = 100
while retry_count > 0 and not operation.complete:
    retry_count -= 1
    time.sleep(10)
    operation.poll()  # API call

for result in operation.results:
    for alternative in result.alternatives:
        print('=' * 20)
        print(alternative.transcript)
        print(alternative.confidence)
