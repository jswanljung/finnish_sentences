#!/Users/johan/fun/finnish_sentences/bin/python
import os
from google.cloud import texttospeech as tts
os.environ['GOOGLE_APPLICATION_CREDENTIALS']="/Users/johan/fun/finnish_sentences/scenic-genre-382411-895c56667741.json"

def save_finnish_audio(text, filename):
    client = tts.TextToSpeechClient()
    input = tts.SynthesisInput()
    input.text = text
    voice = tts.VoiceSelectionParams()
    voice.language_code = "fi-FI"
    audio_config = tts.AudioConfig()
    audio_config.audio_encoding = tts.AudioEncoding.MP3
    request = tts.SynthesizeSpeechRequest(
        input=input,
        voice=voice,
        audio_config=audio_config,
    )

    response = client.synthesize_speech(request=request)
    with open(filename, 'wb') as fout:
        fout.write(response.audio_content)

if __name__ == '__main__':
    test_sentence = "Venäjän päätöslauselma­ehdotus hylättiin, ja useat neuvoston jäsenmaat katsoivat ehdotuksen Venäjän yrityksenä kääntää huomio pois sen hyökkäyksestä Ukrainaan."
    save_finnish_audio(test_sentence, 'testfil.mp3')
