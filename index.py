import src
import src.services.arcgis

app = src.create_flask_app()


def main():
    app.run()
    # print(src.services.arcgis.ArcGISService.get_hosp_data())


if __name__ == "__main__":
    main()
