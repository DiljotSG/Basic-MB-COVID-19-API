from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from src.services.covid import COVIDService
from src.consts import Y_VALUES

class ImageService:

    def __init__(self) -> None:
        self.font = ImageFont.truetype("./resources/Poppins-Light.ttf", 60)
        self.date_font = ImageFont.truetype("./resources/Poppins-Light.ttf", 40)

    def get_daily_cases_image(self, new_deaths):
        self.data = COVIDService.get_daily_data()
        self.image = Image.open("./resources/template-cases.png")
        self.width, self.height = self.image.size
        self.draw = ImageDraw.Draw(self.image)
        messages = [
            str('{:,}'.format(self.data["New_Cases"])),
            str('{:,}'.format(self.data["Active_Cases"])),
            str('{:,}'.format(self.data["Total_Cases"])),
            str('{:,}'.format(self.data["Recovered"])),
            str('Total: {:,}'.format(self.data["Deaths"])) if new_deaths is None else str('New: {:,} / Total: {:,}'.format(new_deaths, self.data["Deaths"]))
        ]
        self.__write_data(messages)
        return self.image

    def get_daily_vaxx_image(self):
        self.data = COVIDService.get_daily_data()
        self.image = Image.open("./resources/template-vaxx.png")
        self.width, self.height = self.image.size
        self.draw = ImageDraw.Draw(self.image)
        messages = [
            str('{:,}'.format(self.data["Total_Doses_Administered"])),
            str('{:,}'.format(self.data["Doses_Scheduled_for_Today"])),
            str('{:,}% (12+) / {:,}% (5+)'.format(self.data["Per_cent_Partially_Immunized_12"], self.data["Per_cent_Partially_Immunized_5"])),
            str('{:,}% (12+) / {:,}% (5+)'.format(self.data["Per_cent_Fully_Immunized_12"], self.data["Per_cent_Fully_Immunized_5"])),
            str('{:,}% (12+) / {:,}% (5+)'.format(self.data["Per_cent_With_Third_Dose_12"], self.data["Per_cent_With_Third_Dose_5"]))
        ]
        self.__write_data(messages)
        return self.image
    
    def get_daily_data_image(self):
        self.data = COVIDService.get_daily_data()
        self.image = Image.open("./resources/template-data.png")
        self.draw = ImageDraw.Draw(self.image)
        self.width, self.height = self.image.size
        messages = [
            str('{:,}'.format(self.data["Active_Hospitalizations"])),
            str('{:,}'.format(self.data["Total_Hospitalizations"])),
            str('{:,}'.format(self.data["Active_ICU_Patients"])),
            str('{:,}'.format(self.data["Total_ICU_Patients"])),
            str('{:,}%'.format(self.data["Positivity_Rate"]))
        ]
        self.__write_data(messages)
        return self.image
    
    def __write_date(self):
        msg = str(self.data["Last_Update"])
        w, h = self.draw.textsize(msg, font=self.date_font)
        size = ((self.width-w)/2, 485)
        self.draw.text(size, msg, fill="black", font=self.date_font)

    def __write_line(self, msg, y):
        w, h = self.draw.textsize(msg, font=self.font)
        size = ((self.width-w)/2, y) # delta = 225
        self.draw.text(size, msg, fill="black", font=self.font)
    
    def __write_data(self, messages):
        self.__write_date()
        for i, msg in enumerate(messages):
            self.__write_line(msg, Y_VALUES[i])
