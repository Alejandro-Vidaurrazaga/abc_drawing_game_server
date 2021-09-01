import os
import pandas as pd
from inference import clf
from flask import Flask, request, url_for, make_response, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    route = f'For testing purpose try one of this one:\n' \
            f'https://{request.host}/good_prediction\n' \
            f'https://{request.host}/bad_prediction'

    return route


@app.route('/good_prediction')
def good_prediction():
    return make_response(jsonify({'predicted_letter': 'A', 'certain': '0.9', 'real_letter': 'A'}, 200))


@app.route('/bad_prediction')
def bad_prediction():
    return make_response(jsonify({'predicted_letter': 'B', 'certain': '0.51', 'real_letter': 'A'}, 200))


if __name__ == '__main__':
    try:
        port = int(os.environ.get('PORT'))
        app.run(host='0.0.0.0', port=port)

        # app.run(host='localhost')
    except Exception:
        print('Problems finding the PORT variable')
