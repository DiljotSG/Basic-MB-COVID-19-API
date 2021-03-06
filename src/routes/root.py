from flask import jsonify
from flask import Blueprint
from flask_cors import CORS
from flask_cors import cross_origin

from src.response_codes import HttpCodes
from src.services.covid import COVIDService

mod = Blueprint('root', __name__)
cors = CORS(mod)


@mod.route("", methods=["GET"])
@cross_origin()
def get_root():
    result = COVIDService.get_daily_data()
    code = HttpCodes.HTTP_200_OK
    return jsonify(result), code
