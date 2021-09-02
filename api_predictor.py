import base64
import io
import os
import string
import numpy as np
from PIL.Image import Image
from flask_cors import CORS, cross_origin
from flask import Flask, request, make_response, jsonify
from skimage.color import rgb2gray, rgba2rgb
from skimage.transform import resize
from inference import clf

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


def fix_input_image(str_img):
    image = Image.open(io.BytesIO(base64.urlsafe_b64decode(str_img)))
    image_np = np.array(image)
    image_np = rgb2gray(rgba2rgb(image_np))
    image = resize(image_np, (28, 28))

    squarer2 = lambda t: 0 if t == 255 else t
    squarer = lambda t: (int((t + 1) * 255 / 2) - 255) * -1
    vfunc = np.vectorize(squarer)
    image = vfunc(image)
    vfunc = np.vectorize(squarer2)
    image = vfunc(image)

    dic_letters = {i: letter for i, letter in enumerate(string.ascii_uppercase)}
    row = image.reshape((1, -1))

    return dic_letters[clf.predict(row)[0]], clf.predict_proba(np.max(row))


@app.route("/json", methods=["POST"])
@cross_origin(supports_credentials=True)
def json():
    if request.is_json:
        try:
            req = request.get_json()
            letter, certain = fix_input_image(req.get("data"))

            return make_response(jsonify({'letter': letter, 'certain': certain}), 200)
        except Exception as ex:
            print(ex)
        return make_response(jsonify({'error': ex}), 400)
    else:
        return make_response(jsonify({"message": "No JSON"}), 400)


if __name__ == '__main__':
    try:
        port = int(os.environ.get('PORT'))
        app.run(host='0.0.0.0', port=port)
    except Exception:
        print('Problems finding the PORT variable')
        # app.run(host='localhost')
