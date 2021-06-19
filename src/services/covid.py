from src.services.arcgis import ArcGISService

class COVIDService:
    @staticmethod
    def get_daily_data() -> dict:
        result = {}

        doses = COVIDService.__get_parsed_doses_data()
        vaxx = COVIDService.__get_parsed_immunization_data()
        cases = COVIDService.__get_parsed_cases_data()
        result.update(doses)
        result.update(vaxx)
        result.update(cases)

        return result

    @staticmethod
    def __get_parsed_doses_data() -> dict:
        data = ArcGISService.get_doses_data()["features"][0]["attributes"]
        keys = [
            "Total_Doses_Administered",
            "Doses_Scheduled_for_Today"
        ]
        return dict((k,v) for k,v in data.items() if k in keys)

    @staticmethod
    def __get_parsed_immunization_data() -> dict:
        data = ArcGISService.get_immunization_data()["features"][0]["attributes"]
        keys = [
            "Per_cent_Partially_Immunized_18",
            "Per_cent_Fully_Immunized_18",
            "Per_cent_All_Immunized_18",
            "Per_cent_Partially_Immunized_12",
            "Per_cent_Fully_Immunized_12",
            "Per_cent_All_Immunized_12"
        ]
        return dict((k,v) for k,v in data.items() if k in keys)

    @staticmethod
    def __get_parsed_cases_data() -> dict:
        data = ArcGISService.get_cases_data()["features"][0]["attributes"]
        print(data)
        keys = [
            "Last_Update",
            "Total_Tests",
            "Daily_Tests",
            "Total_Cases",
            "Active_Cases",
            "Recovered",
            "Deaths",
            "New_Cases",
            "Active_Hospitalizations",
            "Total_Hospitalizations",
            "Active_ICU_Patients",
            "Total_ICU_Patients"
        ]
        return dict((k,v) for k,v in data.items() if k in keys)
