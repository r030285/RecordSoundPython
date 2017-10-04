import io
from google.cloud import speech
client = speech.SpeechClient()
config = speech.types.RecognitionConfig(
    encoding='LINEAR16',
    language_code='pt-BR',
    sample_rate_hertz=16000,
)
with io.open('output.wav', 'rb') as stream:
    requests = [speech.types.StreamingRecognizeRequest(
        audio_content=stream.read(),
    )]

config = speech.types.StreamingRecognitionConfig(config=config)
responses = client.streaming_recognize(config,requests)
print responses
for response in responses:
    print response
    for result in response:
        print result
        for alternative in result.alternatives:
            print('=' * 20)
            print('transcript: ' + alternative.transcript)
            print('confidence: ' + str(alternative.confidence))
            print('is_final:' + str(result.is_final))
