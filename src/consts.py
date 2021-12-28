BASE_URL_VAX_COV = "https://services.arcgis.com/mMUesHYPkXjaFGfS/arcgis/rest/services/mb_covid_vaccinations_coverage_02/FeatureServer/0/query"
BASE_URL_INV_STATS = "https://services.arcgis.com/mMUesHYPkXjaFGfS/arcgis/rest/services/mb_covid_vaccinations_inventory_stats_02/FeatureServer/0/query"
BASE_URL_NEW_CASES = "https://services.arcgis.com/mMUesHYPkXjaFGfS/arcgis/rest/services/mb_covid_cases_summary_statistics/FeatureServer/0/query"
BASE_URL_TP = "https://services.arcgis.com/mMUesHYPkXjaFGfS/arcgis/rest/services/mb_covid_5_day_positivity_rate/FeatureServer/0/query"

PERCENT_SCHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "objectIdFieldName": {
      "type": "string"
    },
    "uniqueIdField": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "isSystemMaintained": {
          "type": "boolean"
        }
      },
      "required": [
        "name",
        "isSystemMaintained"
      ]
    },
    "globalIdFieldName": {
      "type": "string"
    },
    "fields": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "sqlType": {
              "type": "string"
            },
            "length": {
              "type": "integer"
            },
            "domain": {
              "type": "null"
            },
            "defaultValue": {
              "type": "null"
            }
          },
          "required": [
            "name",
            "type",
            "alias",
            "sqlType",
            "length",
            "domain",
            "defaultValue"
          ]
        },
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "sqlType": {
              "type": "string"
            },
            "domain": {
              "type": "null"
            },
            "defaultValue": {
              "type": "null"
            }
          },
          "required": [
            "name",
            "type",
            "alias",
            "sqlType",
            "domain",
            "defaultValue"
          ]
        },
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "sqlType": {
              "type": "string"
            },
            "domain": {
              "type": "null"
            },
            "defaultValue": {
              "type": "null"
            }
          },
          "required": [
            "name",
            "type",
            "alias",
            "sqlType",
            "domain",
            "defaultValue"
          ]
        },
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "sqlType": {
              "type": "string"
            },
            "domain": {
              "type": "null"
            },
            "defaultValue": {
              "type": "null"
            }
          },
          "required": [
            "name",
            "type",
            "alias",
            "sqlType",
            "domain",
            "defaultValue"
          ]
        },
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "sqlType": {
              "type": "string"
            },
            "domain": {
              "type": "null"
            },
            "defaultValue": {
              "type": "null"
            }
          },
          "required": [
            "name",
            "type",
            "alias",
            "sqlType",
            "domain",
            "defaultValue"
          ]
        },
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "sqlType": {
              "type": "string"
            },
            "domain": {
              "type": "null"
            },
            "defaultValue": {
              "type": "null"
            }
          },
          "required": [
            "name",
            "type",
            "alias",
            "sqlType",
            "domain",
            "defaultValue"
          ]
        },
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "sqlType": {
              "type": "string"
            },
            "domain": {
              "type": "null"
            },
            "defaultValue": {
              "type": "null"
            }
          },
          "required": [
            "name",
            "type",
            "alias",
            "sqlType",
            "domain",
            "defaultValue"
          ]
        },
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "sqlType": {
              "type": "string"
            },
            "domain": {
              "type": "null"
            },
            "defaultValue": {
              "type": "null"
            }
          },
          "required": [
            "name",
            "type",
            "alias",
            "sqlType",
            "domain",
            "defaultValue"
          ]
        },
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "sqlType": {
              "type": "string"
            },
            "domain": {
              "type": "null"
            },
            "defaultValue": {
              "type": "null"
            }
          },
          "required": [
            "name",
            "type",
            "alias",
            "sqlType",
            "domain",
            "defaultValue"
          ]
        },
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "sqlType": {
              "type": "string"
            },
            "domain": {
              "type": "null"
            },
            "defaultValue": {
              "type": "null"
            }
          },
          "required": [
            "name",
            "type",
            "alias",
            "sqlType",
            "domain",
            "defaultValue"
          ]
        },
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "sqlType": {
              "type": "string"
            },
            "domain": {
              "type": "null"
            },
            "defaultValue": {
              "type": "null"
            }
          },
          "required": [
            "name",
            "type",
            "alias",
            "sqlType",
            "domain",
            "defaultValue"
          ]
        },
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "sqlType": {
              "type": "string"
            },
            "domain": {
              "type": "null"
            },
            "defaultValue": {
              "type": "null"
            }
          },
          "required": [
            "name",
            "type",
            "alias",
            "sqlType",
            "domain",
            "defaultValue"
          ]
        },
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "sqlType": {
              "type": "string"
            },
            "domain": {
              "type": "null"
            },
            "defaultValue": {
              "type": "null"
            }
          },
          "required": [
            "name",
            "type",
            "alias",
            "sqlType",
            "domain",
            "defaultValue"
          ]
        },
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "sqlType": {
              "type": "string"
            },
            "domain": {
              "type": "null"
            },
            "defaultValue": {
              "type": "null"
            }
          },
          "required": [
            "name",
            "type",
            "alias",
            "sqlType",
            "domain",
            "defaultValue"
          ]
        }
      ]
    },
    "exceededTransferLimit": {
      "type": "boolean"
    },
    "features": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "attributes": {
              "type": "object",
              "properties": {
                "RHA": {
                  "type": "string"
                },
                "Per_cent_Partially_Immunized_18": {
                  "type": "number"
                },
                "Per_cent_Fully_Immunized_18": {
                  "type": "number"
                },
                "Per_cent_With_Third_Dose_18": {
                  "type": "number"
                },
                "Per_cent_All_Immunized_18": {
                  "type": "number"
                },
                "Per_cent_Partially_Immunized_12": {
                  "type": "number"
                },
                "Per_cent_Fully_Immunized_12": {
                  "type": "number"
                },
                "Per_cent_With_Third_Dose_12": {
                  "type": "number"
                },
                "Per_cent_All_Immunized_12": {
                  "type": "integer"
                },
                "Per_cent_Partially_Immunized_5": {
                  "type": "number"
                },
                "Per_cent_Fully_Immunized_5": {
                  "type": "number"
                },
                "Per_cent_With_Third_Dose_5": {
                  "type": "number"
                },
                "Per_cent_All_Immunized_5": {
                  "type": "number"
                },
                "ObjectId": {
                  "type": "integer"
                }
              },
              "required": [
                "RHA",
                "Per_cent_Partially_Immunized_18",
                "Per_cent_Fully_Immunized_18",
                "Per_cent_With_Third_Dose_18",
                "Per_cent_All_Immunized_18",
                "Per_cent_Partially_Immunized_12",
                "Per_cent_Fully_Immunized_12",
                "Per_cent_With_Third_Dose_12",
                "Per_cent_All_Immunized_12",
                "Per_cent_Partially_Immunized_5",
                "Per_cent_Fully_Immunized_5",
                "Per_cent_With_Third_Dose_5",
                "Per_cent_All_Immunized_5",
                "ObjectId"
              ]
            }
          },
          "required": [
            "attributes"
          ]
        }
      ]
    }
  },
  "required": [
    "objectIdFieldName",
    "uniqueIdField",
    "globalIdFieldName",
    "fields",
    "features"
  ]
}

DOSES_SCHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "objectIdFieldName": {
      "type": "string"
    },
    "uniqueIdField": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "isSystemMaintained": {
          "type": "boolean"
        }
      },
      "required": [
        "name",
        "isSystemMaintained"
      ]
    },
    "globalIdFieldName": {
      "type": "string"
    },
    "fields": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "sqlType": {
              "type": "string"
            },
            "domain": {
              "type": "null"
            },
            "defaultValue": {
              "type": "null"
            }
          },
          "required": [
            "name",
            "type",
            "alias",
            "sqlType",
            "domain",
            "defaultValue"
          ]
        },
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "sqlType": {
              "type": "string"
            },
            "domain": {
              "type": "null"
            },
            "defaultValue": {
              "type": "null"
            }
          },
          "required": [
            "name",
            "type",
            "alias",
            "sqlType",
            "domain",
            "defaultValue"
          ]
        },
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "alias": {
              "type": "string"
            },
            "sqlType": {
              "type": "string"
            },
            "domain": {
              "type": "null"
            },
            "defaultValue": {
              "type": "null"
            }
          },
          "required": [
            "name",
            "type",
            "alias",
            "sqlType",
            "domain",
            "defaultValue"
          ]
        }
      ]
    },
    "features": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "attributes": {
              "type": "object",
              "properties": {
                "Total_Doses_Administered": {
                  "type": "integer"
                },
                "Doses_Scheduled_for_Today": {
                  "type": "integer"
                },
                "ObjectId": {
                  "type": "integer"
                }
              },
              "required": [
                "Total_Doses_Administered",
                "Doses_Scheduled_for_Today",
                "ObjectId"
              ]
            }
          },
          "required": [
            "attributes"
          ]
        }
      ]
    }
  },
  "required": [
    "objectIdFieldName",
    "uniqueIdField",
    "globalIdFieldName",
    "fields",
    "features"
  ]
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

TP_SCHEMA = {
	"definitions": {},
	"$schema": "http://json-schema.org/draft-07/schema#", 
	"$id": "https://example.com/object1624136171.json", 
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
							"Positivity_Rate",
							"ObjectId"
						],
						"properties": {
							"Date": {
								"$id": "#root/features/items/attributes/Date", 
								"title": "Date", 
								"type": "integer",
								"default": 0
							},
							"Positivity_Rate": {
								"$id": "#root/features/items/attributes/Positivity_Rate", 
								"title": "Positivity_rate", 
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

Y_VALUES = [
    725,
    950,
    1175,
    1400,
    1625
]
