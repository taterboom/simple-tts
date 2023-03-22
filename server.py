# flask server for the web app

from flask import Flask, send_file

from tts import tts

app = Flask(__name__)


@app.route('/tts/<text>/<speaker>')
def tts_route(text, speaker):
    filename = tts(text, speaker)
    return send_file(filename, mimetype='audio/mp3')


if __name__ == '__main__':
    app.run()
