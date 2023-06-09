#!/Users/johan/fun/finnish_sentences/bin/python

import json
import urllib.request

def request(action, **params):
    return {'action': action, 'params': params, 'version': 6}

def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode('utf-8')
    response = json.load(urllib.request.urlopen(urllib.request.Request('http://localhost:8765', requestJson)))
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']

def makeNote(mening, filnamn, audio, anteckningar):
    return {'deckName': 'Egna finska',
            'modelName': 'Egna finska',
            'fields': {
                "mening": mening,
                "anteckningar": anteckningar
            },
            'audio': [{
                "filename": filnamn,
                "path": audio,
                "fields": ["audio"]
            }]}

def addNote(mening, filnamn, audio):
    invoke('addNote', note=makeNote(mening, filnamn, audio, ""))

if __name__ == '__main__':
    addNote("Hyvää päivää", "testfil.mp3", "/Users/johan/fun/finnish_sentences/testfil.mp3")
