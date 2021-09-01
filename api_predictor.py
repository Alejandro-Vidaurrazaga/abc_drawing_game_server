import base64
import os
import numpy as np
import pandas as pd
from flask_cors import CORS
from inference import clf
from flask import Flask, request, url_for, make_response, jsonify

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def home():
    route = f'For testing purpose try one of this one:\n' \
            f'https://{request.host}/good_prediction\n' \
            f'https://{request.host}/bad_prediction'

    return route


@app.route('/good_prediction')
def good_prediction():
    return make_response(jsonify({'predicted_letter': 'A', 'certain': 0.9, 'real_letter': 'A'}, 200))


@app.route('/bad_prediction', methods=["POST"])
def bad_prediction():
    if request.is_json:
        req = request.get_json()

        return make_response(jsonify({'asdasd': 'asdasdasd'}), 200)

    return make_response(jsonify({'predicted_letter': 'B', 'certain': 0.51, 'real_letter': 'A'}, 200))


@app.route("/json", methods=["POST"])
def json():
    if request.is_json:
        req = request.get_json()
        # response_body = {
        #     "message": "JSON received!",
        #     "sender": req.get("data")
        # }

        # img_decoded = base64.b64decode(req.get("data"))
        # buffer = np.fromstring(img_decoded, np.float32)
        # res = make_response(jsonify({'resp': buffer}), 200)

        return make_response(jsonify(req), 400)
    else:
        return make_response(jsonify({"message": "No JSON"}), 400)


if __name__ == '__main__':
    try:
        port = int(os.environ.get('PORT'))
        app.run(host='0.0.0.0', port=port)

        # app.run(host='localhost')
    except Exception:
        print('Problems finding the PORT variable')
