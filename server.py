# flask server for the web app

from flask import Flask, send_file, request

from transformer_tts import tts as transformer_tts
from azure_tts import tts as azure_tts

app = Flask(__name__)


@app.route('/tts', methods=['POST'])
def route_tts():
    params = request.get_json()
    type = params['type']
    text = params['text']
    speaker = params['speaker']

    if type == 'azure':
        b = azure_tts(text, speaker)
    elif type == 'transformer':
        b = transformer_tts(text, speaker)
    else:
        return "error", 500

    if b:
        return b.getvalue().hex()
    else:
        return "error", 500


if __name__ == '__main__':
    app.run()
