from io import BytesIO

from flask import jsonify
from flask import Blueprint
from flask import send_file
from flask_cors import CORS
from flask_cors import cross_origin

from src.response_codes import HttpCodes
from src.services.covid import COVIDService
from src.services.image import ImageService

mod = Blueprint('root', __name__)
cors = CORS(mod)
imageService = ImageService()

@mod.route("", methods=["GET"])
@cross_origin()
def get_root():
    result = COVIDService.get_daily_data()
    code = HttpCodes.HTTP_200_OK
    return jsonify(result), code

@mod.route("image", methods=["GET"])
@cross_origin()
def get_image():
    code = HttpCodes.HTTP_200_OK
    image = imageService.get_daily_image()
    return serve_pil_image(image), code

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')
