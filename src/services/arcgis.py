import requests
import src.consts as consts

from typing import Optional
from jsonschema import validate
from jsonschema import ValidationError


def is_valid_schema(obj: dict, schema: dict) -> bool:
    result = True
    try:
        validate(instance=obj, schema=schema)
    except ValidationError:
        result = False
    return result


class ArcGISService:
    @staticmethod
    def send_request(url: str, params: dict):
        return requests.get(
            url,
            params=params,
            headers={
                "Content-Type": "application/json"
            }
        )
    
    @staticmethod
    def get_immunization_data() -> Optional[dict]:
        data = ArcGISService.send_request(
            consts.BASE_URL_VAX_COV,
            {
                "f": "json",
                "cacheHint": True,
                "resultOffset": 0,
                "resultRecordCount": 50,
                "where": "RHA='All'",
                "outFields": "*",
                "resultType": "standard",
                "spatialRel": "esriSpatialRelIntersects"
            }
        ).json()
        if not is_valid_schema(data, consts.PERCENT_SCHEMA):
            return None
        return data

    @staticmethod
    def get_doses_data() -> Optional[dict]:
        data = ArcGISService.send_request(
            consts.BASE_URL_INV_STATS,
            {
                "f": "json",
                "cacheHint": True,
                "resultOffset": 0,
                "resultRecordCount": 50,
                "where": "1=1",
                "outFields": "*",
                "resultType": "standard",
                "spatialRel": "esriSpatialRelIntersects"
            }
        ).json()
        if not is_valid_schema(data, consts.DOSES_SCHEMA):
            return None
        return data

    @staticmethod
    def get_cases_data() -> Optional[dict]:
        data = ArcGISService.send_request(
            consts.BASE_URL_NEW_CASES,
            {
                "f": "json",
                "cacheHint": True,
                "resultOffset": 0,
                "resultRecordCount": 50,
                "where": "(Area IN('All', 'Interlake-Eastern', 'Northern', 'Prairie Mountain Health', 'Southern Health-Santé Sud', 'Winnipeg')) AND (Area='All')",
                "outFields": "*",
                "resultType": "standard",
                "spatialRel": "esriSpatialRelIntersects"
            }
        ).json()
        if not is_valid_schema(data, consts.CASES_SCHEMA):
            return None
        return data
