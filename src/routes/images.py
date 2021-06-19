import os
import flask
import base64

from io import BytesIO
from flask import request
from flask import Blueprint
from flask import send_file
from flask_cors import CORS
from flask_cors import cross_origin

from src.response_codes import HttpCodes
from src.services.image import ImageService

mod = Blueprint('images', __name__)
cors = CORS(mod)
imageService = ImageService()

@mod.route("cases", methods=["GET"])
@cross_origin()
def get_image_cases():
    code = HttpCodes.HTTP_200_OK
    new_deaths = request.args.get("new_deaths", type=int)
    new_deaths = None if new_deaths < 0 else new_deaths

    image = imageService.get_daily_cases_image(new_deaths)

    if os.environ.get("IS_LAMBDA"):
        # Return a base64 encoded image in plaintext
        response = flask.Response()
        data = base64.b64encode(serve_pil_image(image)).decode('utf-8')
        response.headers.set('Content-Type', 'text/plain')
        response.data = format(data)
        return response, code

    return serve_pil_image(image), code
    

@mod.route("vaxx", methods=["GET"])
@cross_origin()
def get_image_vaxx():
    code = HttpCodes.HTTP_200_OK
    image = imageService.get_daily_vaxx_image()

    if os.environ.get("IS_LAMBDA"):
        # Return a base64 encoded image in plaintext
        response = flask.Response()
        data = base64.b64encode(serve_pil_image(image)).decode('utf-8')
        response.headers.set('Content-Type', 'text/plain')
        response.data = format(data)
        return response, code

    return serve_pil_image(image), code

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'PNG')
    img_io.seek(0)
    if os.environ.get("IS_LAMBDA"):
        return img_io.read()
    return send_file(img_io, mimetype='image/png')
