import os
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


# @app.route("/json", methods=["POST"])
# @cross_origin(supports_credentials=True)
# def json(img):
#     # if request.is_json:
#     #     req = request.get_json()
#     #     # response_body = {
#     #     #     "message": "JSON received!",
#     #     #     "sender": req.get("data")
#     #     # }
#     #
#     #     try:
#     #         img_decoded = base64.b64decode(req.get("data"))
#     #         buffer = np.fromstring(img_decoded, np.float32)
#     #         img = resize(buffer, (28, 28)).reshape(1, -1)
#     #         return make_response(jsonify({'img': img}), 200)
#     #     except Exception as ex:
#     #         print(ex)
#     #
#     #     # res = make_response(jsonify({'resp': buffer}), 200)
#     #
#     #     return make_response(jsonify({'error': 'error'}), 400)
#     # else:
#     #     return make_response(jsonify({"message": "No JSON"}), 400)
#
#     try:
#         img_decoded = base64.b64decode(img)
#         buffer = np.fromstring(img_decoded, np.float32)
#         img = resize(buffer, (28, 28)).reshape(1, -1)
#         return make_response(jsonify({'img': img}), 200)
#     except Exception as ex:
#         print(ex)


# def json2(img):
#     try:
#         # img_decoded = base64.b64decode(img)
#         # buffer = np.fromstring(str(img_decoded), np.int)
#         # img = resize(buffer, (28, 28)).reshape(1, -1)
#         # return make_response(jsonify({'img': img}), 200)
#
#         # decoded = base64.b64decode(img)
#         # image = bytearray(decoded)
#         # image = np.asarray(bytearray(decoded), dtype="uint8")
#         # image = cv2.imdecode(image, cv2.IMREAD_COLOR)
#         # plt.imshow(image)
#         # plt.show()
#         # image
#
#         # with open("imageToSave.png", "wb") as fh:
#         #     fh.write(base64.b64decode(img))
#
#         image = Image.open(io.BytesIO(base64.urlsafe_b64decode(img)))
#         image_np = np.array(image)
#         image = resize(image_np, (28, 28)).reshape(1, -1)
#         # plt.imshow(image, cmap='gray')
#         # plt.show()
#         # with_255 = clf.predict(image * 255)
#         # without_255 = clf.predict(image)
#         # print(with_255)
#         # print(without_255)
#     except Exception as ex:
#         print(ex)


if __name__ == '__main__':
    try:
        port = int(os.environ.get('PORT'))
        app.run(host='0.0.0.0', port=port)
    except Exception:
        print('Problems finding the PORT variable')
        # app.run(host='localhost')
