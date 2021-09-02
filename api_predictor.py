import io
import os
import base64

import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

from inference import clf
from skimage.transform import resize
from flask_cors import CORS, cross_origin
from flask import Flask, request, make_response, jsonify


app = Flask(__name__)
# cors = CORS(app, resources={r"/*": {"origins": "*"}}, allow_headers='*')
cors = CORS(app, support_credentials=True)

@app.route('/')
def home():
    route = f'For testing purpose try one of this one:\n' \
            f'https://{request.host}/good_prediction\n' \
            f'https://{request.host}/bad_prediction'

    return route


@app.route('/good_prediction', methods=["POST"])
@cross_origin(supports_credentials=True)
def good_prediction():
    if request.is_json:
        req = request.get_json()
        return make_response(jsonify({'predicted_letter': 'A', 'certain': 0.9, 'real_letter': 'A'}, 200))

    return make_response(jsonify({'predicted_letter': 'A', 'certain': 0.9, 'real_letter': 'A'}, 200))


@app.route('/bad_prediction', methods=["POST"])
@cross_origin(supports_credentials=True)
def bad_prediction():
    if request.is_json:
        req = request.get_json()
        # return make_response(jsonify(req), 200)

        return make_response(jsonify({'predicted_letter': 'A', 'certain': 0.9, 'real_letter': 'A'}, 200))

    return make_response(jsonify({'predicted_letter': 'B', 'certain': 0.51, 'real_letter': 'A'}, 200))


@app.route("/json", methods=["POST"])
@cross_origin(supports_credentials=True)
def json(img):
    # if request.is_json:
    #     req = request.get_json()
    #     # response_body = {
    #     #     "message": "JSON received!",
    #     #     "sender": req.get("data")
    #     # }
    #
    #     try:
    #         img_decoded = base64.b64decode(req.get("data"))
    #         buffer = np.fromstring(img_decoded, np.float32)
    #         img = resize(buffer, (28, 28)).reshape(1, -1)
    #         return make_response(jsonify({'img': img}), 200)
    #     except Exception as ex:
    #         print(ex)
    #
    #     # res = make_response(jsonify({'resp': buffer}), 200)
    #
    #     return make_response(jsonify({'error': 'error'}), 400)
    # else:
    #     return make_response(jsonify({"message": "No JSON"}), 400)

    try:
        img_decoded = base64.b64decode(img)
        buffer = np.fromstring(img_decoded, np.float32)
        img = resize(buffer, (28, 28)).reshape(1, -1)
        return make_response(jsonify({'img': img}), 200)
    except Exception as ex:
        print(ex)


def json2(img):
    try:
        # img_decoded = base64.b64decode(img)
        # buffer = np.fromstring(str(img_decoded), np.int)
        # img = resize(buffer, (28, 28)).reshape(1, -1)
        # return make_response(jsonify({'img': img}), 200)

        # decoded = base64.b64decode(img)
        # image = bytearray(decoded)
        # image = np.asarray(bytearray(decoded), dtype="uint8")
        # image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        # plt.imshow(image)
        # plt.show()
        # image

        # with open("imageToSave.png", "wb") as fh:
        #     fh.write(base64.b64decode(img))

        image = Image.open(io.BytesIO(base64.urlsafe_b64decode(img)))
        image_np = np.array(image)
        image = resize(image_np, (28, 28)).reshape(1, -1)
        # plt.imshow(image, cmap='gray')
        # plt.show()
        with_255 = clf.predict(image * 255)
        without_255 = clf.predict(image)
        print(with_255)
        print(without_255)
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    try:
        port = int(os.environ.get('PORT'))
        app.run(host='0.0.0.0', port=port)

        # app.run(host='localhost')
    except Exception:
        print('Problems finding the PORT variable')
    # img = "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"
    # img2 = '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'
    # json2(img2)
