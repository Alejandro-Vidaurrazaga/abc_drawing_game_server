import io
import os
import base64

import cv2
import numpy as np
import skimage
from PIL import Image
from matplotlib import pyplot as plt
from skimage import data
from skimage.color import rgb2gray, rgba2rgb

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

import string

letters = list(string.ascii_uppercase)
dict_number_to_letter = {}
for num in range(26):
    dict_number_to_letter[num]=letters[num]

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
        image_np = rgb2gray(rgba2rgb(image_np))
        # image = resize(image_np, (28, 28)).reshape(1, -1)

        image = resize(image_np, (28, 28))
        plt.imshow(image, cmap='gray')
        plt.show()
        return
        with_255 = clf.predict(image * 255)
        without_255 = clf.predict(image)
        print(dict_number_to_letter[with_255[0]])
        print(dict_number_to_letter[without_255[0]])
        print(clf.predict_proba(image))
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    # try:
    #     port = int(os.environ.get('PORT'))
    #     app.run(host='0.0.0.0', port=port)
    #
    #     # app.run(host='localhost')
    # except Exception:
    #     print('Problems finding the PORT variable')
    img = "iVBORw0KGgoAAAANSUhEUgAAAEcAAACUCAYAAADBGjSeAAAAAXNSR0IArs4c6QAAA5tJREFUeF7tnDGS0zAUhn+xFR0cAEpauAAz0HAuOBYdzHAAKGnhAtBRsDGTbMhudm3p6UmyZefbKjMry9Kn7z0924mDTn/DcPt5058GKTyyzDDcNBp2ko6fLYdtqs1OCldjMwrSxRgTWdEwKgZwTsgeAgLOmU/ngIDzINhuAQFnNBPdAAJOHM7Fb+UTu1i4m4DY0s8pncGZKgNyCsTxemH5kjFnDqfR7gxVcY5RvcI5pI7sy6PKcGS+blnGpjxAteHsN0BDn8ugOV5Hmg0yTCSP9grgXEvKuSqPreTW4NjzTwNzDrWlod/+Q8swiVxzek/KmJPQ0rbgLcwhrOJL033OMd0WbmRO73ln0bDqfcdaFk7nlxG2HatVWG0iKQMn9sAmXafa4vNhP93vWMkLUMzxm+O15nDGycesaVvnaJGeW8Ic1+3FOzPrObTK4STjcr2V8uJweg6t5eF0XO8AJxL1XcDp9ToLOK3MGb5Kelmp4uiw5ikyJ31wHrjeap70/CJFYGkBeB/dtuAUFoApr+aE5VvoCXN8naVwjP/fC6n9GDuA40M6x1FTcKwhtW9nuO0xx1Tqn6MUzuFm7FYBlcL5JoVXW/15QCGcs+8Umh6U1Ze/XY8V4RwibFOAKsOxPQ9qt9Z1e24A5/8A0+V53anU760hnPuD7QLWcWe1FZ4zwmluVPVH0AvAqa9/qx6BEyELHOD4Ag9zMAdzfAQwx8eNnIM5mOMjgDk+buQczMEcHwHM8XEj52AO5vgIYI6PGzkHczDHRwBzfNzIOZiDOT4CmOPjRs7BHMzxEcAcHzdyDuZgjo8A5vi4kXMwB3N8BDDHx42cgzmY4yOAOT5u5BzMwRwfAczxcSPnYM4i5uinFJ77Tt3/UYVh1ftLocsWoBROx6+6KwOzP7r0FTHVf5FbPqV6PWCOY7fKeCeF7Qfs9dZzvp6mzPkh6ZltGBcHZ4/F+noF4MQi89JeS4U5ka0cOMBJ7DiRfEFCBk5+EUjOIeeQc2x1/lgrcg45x2cP5mAO5vgIYI6PGzkHczDHRwBzfNzIOZiDOT4CmOPjRs7BHMzxEcAcH7cKOUdfpPDad/q+j6oB548UHvc9Td/oYnD+SrqydbvNb1rE4HyX9AI4owSGd5I+AmeSgPV5ud5K4ZMN5HpaJb54ZIbzWQpv1jNt20hrwfklhae2U66nVS04v6XwZD3Tto20FhzCKsKbhDwB54MU3ttEXVerf+xGj1RfrehdAAAAAElFTkSuQmCC"
    images = [img]
    for j, i in enumerate(images):
        print(f'Image {j}')
        json2(i)
        print()
