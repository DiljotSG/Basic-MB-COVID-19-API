import requests
import src.consts as consts

from typing import Optional
from jsonschema import validate
from jsonschema import ValidationError

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
        validate(instance=data, schema=consts.PERCENT_SCHEMA)
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
        validate(instance=data, schema=consts.DOSES_SCHEMA)
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
        validate(instance=data, schema=consts.CASES_SCHEMA)
        return data
