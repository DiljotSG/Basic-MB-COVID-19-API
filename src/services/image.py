from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from src.services.covid import COVIDService

Y_VALUES = [
    725,
    950,
    1175,
    1400,
    1625
]

class ImageService:

    def __init__(self) -> None:
        self.font = ImageFont.truetype("./resources/Poppins-Light.ttf", 60)
        self.date_font = ImageFont.truetype("./resources/Poppins-Light.ttf", 40)

    def get_daily_cases_image(self, new_deaths):
        self.image = Image.open("./resources/template-cases.png")
        self.draw = ImageDraw.Draw(self.image)
        self.width, self.height = self.image.size
        self.data = COVIDService.get_daily_data()

        self.__write_date()
        self.__write_line(str('{:,}'.format(self.data["New_Cases"])), Y_VALUES[0])
        self.__write_line(str('{:,}'.format(self.data["Active_Cases"])), Y_VALUES[1])
        self.__write_line(str('{:,}'.format(self.data["Total_Cases"])), Y_VALUES[2])
        self.__write_line(str('{:,}'.format(self.data["Recovered"])), Y_VALUES[3])

        msg = str('{:,}'.format(self.data["Deaths"]))
        if new_deaths != None:
            msg = str('{:,} / +{} new deaths'.format(self.data["Deaths"], new_deaths))
        self.__write_line(msg, Y_VALUES[4])

        return self.image

    def get_daily_vaxx_image(self):
        self.image = Image.open("./resources/template-vaxx.png")
        self.draw = ImageDraw.Draw(self.image)
        self.width, self.height = self.image.size
        self.data = COVIDService.get_daily_data()

        self.__write_date()
        self.__write_line(str('{:,}'.format(self.data["Total_Doses_Administered"])), Y_VALUES[0])
        self.__write_line(str('{:,}'.format(self.data["Doses_Scheduled_for_Today"])), Y_VALUES[1])
        self.__write_line(
            str('{:,}% (18+) / {:,}% (12+)'.format(self.data["Per_cent_Partially_Immunized_18"], self.data["Per_cent_Partially_Immunized_12"])),
            Y_VALUES[2]
        )
        self.__write_line(
            str('{:,}% (18+) / {:,}% (12+)'.format(self.data["Per_cent_Fully_Immunized_18"], self.data["Per_cent_Fully_Immunized_12"])),
            Y_VALUES[3]
        )
        self.__write_line(
            str('{:,}% (18+) / {:,}% (12+)'.format(self.data["Per_cent_All_Immunized_18"], self.data["Per_cent_All_Immunized_12"])),
            Y_VALUES[4]
        )
        return self.image
    
    def get_daily_data_image(self):
        self.image = Image.open("./resources/template-data.png")
        self.draw = ImageDraw.Draw(self.image)
        self.width, self.height = self.image.size
        self.data = COVIDService.get_daily_data()

        self.__write_date()
        self.__write_line(str('{:,}'.format(self.data["Active_Hospitalizations"])), Y_VALUES[0])
        self.__write_line(str('{:,}'.format(self.data["Total_Hospitalizations"])), Y_VALUES[1])
        self.__write_line(str('{:,}'.format(self.data["Active_ICU_Patients"])), Y_VALUES[2])
        self.__write_line(str('{:,}'.format(self.data["Total_ICU_Patients"])), Y_VALUES[3])
        self.__write_line(str('{:,}%'.format(self.data["Positivity_Rate"])), Y_VALUES[4])

        return self.image
    
    def __write_date(self):
        msg = str(self.data["Last_Update"])

        w, h = self.draw.textsize(msg, font=self.date_font)
        size = ((self.width-w)/2, 485) # delta = 225

        self.draw.text(size, msg, fill="black", font=self.date_font)

    def __write_line(self, msg, y):
        w, h = self.draw.textsize(msg, font=self.font)
        size = ((self.width-w)/2, y) # delta = 225

        self.draw.text(size, msg, fill="black", font=self.font)
