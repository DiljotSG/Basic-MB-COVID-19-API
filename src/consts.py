BASE_URL_VAX_COV = "https://services.arcgis.com/mMUesHYPkXjaFGfS/arcgis/rest/services/mb_covid_vaccinations_coverage/FeatureServer/0/query"
BASE_URL_INV_STATS = "https://services.arcgis.com/mMUesHYPkXjaFGfS/arcgis/rest/services/mb_covid_vaccinations_inventory_stats/FeatureServer/0/query"
BASE_URL_NEW_CASES = "https://services.arcgis.com/mMUesHYPkXjaFGfS/arcgis/rest/services/mb_covid_cases_summary_statistics/FeatureServer/0/query"

PERCENT_SCHEMA = {
	"definitions": {},
	"$schema": "http://json-schema.org/draft-07/schema#", 
	"$id": "https://example.com/object1623946779.json", 
	"title": "Root", 
	"type": "object",
	"required": [
		"features"
	],
	"properties": {
		"features": {
			"$id": "#root/features", 
			"title": "Features", 
			"type": "array",
			"default": [],
			"items":{
				"$id": "#root/features/items", 
				"title": "Items", 
				"type": "object",
				"required": [
					"attributes"
				],
				"properties": {
					"attributes": {
						"$id": "#root/features/items/attributes", 
						"title": "Attributes", 
						"type": "object",
						"required": [
							"RHA",
							"Per_cent_Partially_Immunized_18",
							"Per_cent_Fully_Immunized_18",
							"Per_cent_All_Immunized_18",
							"Per_cent_Partially_Immunized_12",
							"Per_cent_Fully_Immunized_12",
							"Per_cent_All_Immunized_12",
							"ObjectId"
						],
						"properties": {
							"RHA": {
								"$id": "#root/features/items/attributes/RHA", 
								"title": "Rha", 
								"type": "string",
								"default": "",
								"pattern": "^.*$"
							},
							"Per_cent_Partially_Immunized_18": {
								"$id": "#root/features/items/attributes/Per_cent_Partially_Immunized_18", 
								"title": "Per_cent_partially_immunized_18", 
								"type": "number",
								"default": 0.0
							},
							"Per_cent_Fully_Immunized_18": {
								"$id": "#root/features/items/attributes/Per_cent_Fully_Immunized_18", 
								"title": "Per_cent_fully_immunized_18", 
								"type": "number",
								"default": 0.0
							},
							"Per_cent_All_Immunized_18": {
								"$id": "#root/features/items/attributes/Per_cent_All_Immunized_18", 
								"title": "Per_cent_all_immunized_18", 
								"type": "number",
								"default": 0.0
							},
							"Per_cent_Partially_Immunized_12": {
								"$id": "#root/features/items/attributes/Per_cent_Partially_Immunized_12", 
								"title": "Per_cent_partially_immunized_12", 
								"type": "number",
								"default": 0.0
							},
							"Per_cent_Fully_Immunized_12": {
								"$id": "#root/features/items/attributes/Per_cent_Fully_Immunized_12", 
								"title": "Per_cent_fully_immunized_12", 
								"type": "number",
								"default": 0.0
							},
							"Per_cent_All_Immunized_12": {
								"$id": "#root/features/items/attributes/Per_cent_All_Immunized_12", 
								"title": "Per_cent_all_immunized_12", 
								"type": "integer",
								"default": 0
							},
							"ObjectId": {
								"$id": "#root/features/items/attributes/ObjectId", 
								"title": "Objectid", 
								"type": "integer",
								"default": 0
							}
						}
					}

				}
			}

		}
	}
}

DOSES_SCHEMA = {
	"definitions": {},
	"$schema": "http://json-schema.org/draft-07/schema#", 
	"$id": "https://example.com/object1623946859.json", 
	"title": "Root", 
	"type": "object",
	"required": [
		"features"
	],
	"properties": {
		"features": {
			"$id": "#root/features", 
			"title": "Features", 
			"type": "array",
			"default": [],
			"items":{
				"$id": "#root/features/items", 
				"title": "Items", 
				"type": "object",
				"required": [
					"attributes"
				],
				"properties": {
					"attributes": {
						"$id": "#root/features/items/attributes", 
						"title": "Attributes", 
						"type": "object",
						"required": [
							"Total_Doses_Administered",
							"Supersite_FIT_Pop_Up_Clinic",
							"Doses_Delivered_to_First_Nation",
							"Doses_Delivered_to_Doctors_and_",
							"Doses_Received_in_Last_48_Hours",
							"Doses_Scheduled_for_Today",
							"Days_worth_of_inventory",
							"ObjectId"
						],
						"properties": {
							"Total_Doses_Administered": {
								"$id": "#root/features/items/attributes/Total_Doses_Administered", 
								"title": "Total_doses_administered", 
								"type": "integer",
								"default": 0
							},
							"Supersite_FIT_Pop_Up_Clinic": {
								"$id": "#root/features/items/attributes/Supersite_FIT_Pop_Up_Clinic", 
								"title": "Supersite_fit_pop_up_clinic", 
								"type": "integer",
								"default": 0
							},
							"Doses_Delivered_to_First_Nation": {
								"$id": "#root/features/items/attributes/Doses_Delivered_to_First_Nation", 
								"title": "Doses_delivered_to_first_nation", 
								"type": "integer",
								"default": 0
							},
							"Doses_Delivered_to_Doctors_and_": {
								"$id": "#root/features/items/attributes/Doses_Delivered_to_Doctors_and_", 
								"title": "Doses_delivered_to_doctors_and_", 
								"type": "integer",
								"default": 0
							},
							"Doses_Received_in_Last_48_Hours": {
								"$id": "#root/features/items/attributes/Doses_Received_in_Last_48_Hours", 
								"title": "Doses_received_in_last_48_hours", 
								"type": "integer",
								"default": 0
							},
							"Doses_Scheduled_for_Today": {
								"$id": "#root/features/items/attributes/Doses_Scheduled_for_Today", 
								"title": "Doses_scheduled_for_today", 
								"type": "integer",
								"default": 0
							},
							"Days_worth_of_inventory": {
								"$id": "#root/features/items/attributes/Days_worth_of_inventory", 
								"title": "Days_worth_of_inventory", 
								"type": "integer",
								"default": 0
							},
							"ObjectId": {
								"$id": "#root/features/items/attributes/ObjectId", 
								"title": "Objectid", 
								"type": "integer",
								"default": 0
							}
						}
					}

				}
			}

		}
	}
}

CASES_SCHEMA = {
	"definitions": {},
	"$schema": "http://json-schema.org/draft-07/schema#", 
	"$id": "https://example.com/object1623946891.json", 
	"title": "Root", 
	"type": "object",
	"required": [
		"features"
	],
	"properties": {
		"features": {
			"$id": "#root/features", 
			"title": "Features", 
			"type": "array",
			"default": [],
			"items":{
				"$id": "#root/features/items", 
				"title": "Items", 
				"type": "object",
				"required": [
					"attributes"
				],
				"properties": {
					"attributes": {
						"$id": "#root/features/items/attributes", 
						"title": "Attributes", 
						"type": "object",
						"required": [
							"Date",
							"Last_Update",
							"RHA",
							"Area",
							"Area_Name",
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
							"Total_ICU_Patients",
							"Population",
							"Rate",
							"ObjectId"
						],
						"properties": {
							"Date": {
								"$id": "#root/features/items/attributes/Date", 
								"title": "Date", 
								"type": "integer",
								"default": 0
							},
							"Last_Update": {
								"$id": "#root/features/items/attributes/Last_Update", 
								"title": "Last_update", 
								"type": "string",
								"default": "",
								"pattern": "^.*$"
							},
							"RHA": {
								"$id": "#root/features/items/attributes/RHA", 
								"title": "Rha", 
								"type": "string",
								"default": "",
								"pattern": "^.*$"
							},
							"Area": {
								"$id": "#root/features/items/attributes/Area", 
								"title": "Area", 
								"type": "string",
								"default": "",
								"pattern": "^.*$"
							},
							"Area_Name": {
								"$id": "#root/features/items/attributes/Area_Name", 
								"title": "Area_name", 
								"type": "string",
								"default": "",
								"pattern": "^.*$"
							},
							"Total_Tests": {
								"$id": "#root/features/items/attributes/Total_Tests", 
								"title": "Total_tests", 
								"type": "integer",
								"default": 0
							},
							"Daily_Tests": {
								"$id": "#root/features/items/attributes/Daily_Tests", 
								"title": "Daily_tests", 
								"type": "integer",
								"default": 0
							},
							"Total_Cases": {
								"$id": "#root/features/items/attributes/Total_Cases", 
								"title": "Total_cases", 
								"type": "integer",
								"default": 0
							},
							"Active_Cases": {
								"$id": "#root/features/items/attributes/Active_Cases", 
								"title": "Active_cases", 
								"type": "integer",
								"default": 0
							},
							"Recovered": {
								"$id": "#root/features/items/attributes/Recovered", 
								"title": "Recovered", 
								"type": "integer",
								"default": 0
							},
							"Deaths": {
								"$id": "#root/features/items/attributes/Deaths", 
								"title": "Deaths", 
								"type": "integer",
								"default": 0
							},
							"New_Cases": {
								"$id": "#root/features/items/attributes/New_Cases", 
								"title": "New_cases", 
								"type": "integer",
								"default": 0
							},
							"Active_Hospitalizations": {
								"$id": "#root/features/items/attributes/Active_Hospitalizations", 
								"title": "Active_hospitalizations", 
								"type": "integer",
								"default": 0
							},
							"Total_Hospitalizations": {
								"$id": "#root/features/items/attributes/Total_Hospitalizations", 
								"title": "Total_hospitalizations", 
								"type": "integer",
								"default": 0
							},
							"Active_ICU_Patients": {
								"$id": "#root/features/items/attributes/Active_ICU_Patients", 
								"title": "Active_icu_patients", 
								"type": "integer",
								"default": 0
							},
							"Total_ICU_Patients": {
								"$id": "#root/features/items/attributes/Total_ICU_Patients", 
								"title": "Total_icu_patients", 
								"type": "integer",
								"default": 0
							},
							"Population": {
								"$id": "#root/features/items/attributes/Population", 
								"title": "Population", 
								"type": "null",
								"default": None
							},
							"Rate": {
								"$id": "#root/features/items/attributes/Rate", 
								"title": "Rate", 
								"type": "number",
								"default": 0.0
							},
							"ObjectId": {
								"$id": "#root/features/items/attributes/ObjectId", 
								"title": "Objectid", 
								"type": "integer",
								"default": 0
							}
						}
					}

				}
			}

		}
	}
}
