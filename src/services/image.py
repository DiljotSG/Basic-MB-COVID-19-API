from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from src.services.covid import COVIDService

class ImageService:

    def __init__(self) -> None:
        self.font = ImageFont.truetype("./resources/Poppins-Light.ttf", 60)
        self.date_font = ImageFont.truetype("./resources/Poppins-Light.ttf", 40)

    def get_daily_cases_image(self):
        self.image = Image.open("./resources/template-cases.png")
        self.draw = ImageDraw.Draw(self.image)
        self.width, self.height = self.image.size
        self.data = COVIDService.get_daily_data()

        self.__write_date()
        self.__write_new_cases()
        self.__write_active_cases()
        self.__write_total_cases()
        self.__write_recovered()
        self.__write_deaths()

        return self.image

    def get_daily_vaxx_image(self):
        self.image = Image.open("./resources/template-vaxx.png")
        self.draw = ImageDraw.Draw(self.image)
        self.width, self.height = self.image.size
        self.data = COVIDService.get_daily_data()

        self.__write_date()
        self.__write_doses_administered()
        self.__write_doses_scheduled()
        self.__write_total_vaxx()
        self.__write_partial_vaxx()
        self.__write_full_vaxx()

        return self.image
    
    def __write_date(self):
        msg = str(self.data["Last_Update"])
    
        w, h = self.draw.textsize(msg, font=self.date_font)
        size = ((self.width-w)/2, 485) # 225

        self.draw.text(size, msg, fill="black", font=self.date_font)

    def __write_doses_administered(self):
        msg = str('{:,}'.format(self.data["Total_Doses_Administered"]))
    
        w, h = self.draw.textsize(msg, font=self.font)
        size = ((self.width-w)/2, 725) # 225

        self.draw.text(size, msg, fill="black", font=self.font)

    def __write_new_cases(self):
        msg = str('{:,}'.format(self.data["New_Cases"]))
    
        w, h = self.draw.textsize(msg, font=self.font)
        size = ((self.width-w)/2, 725) # 225

        self.draw.text(size, msg, fill="black", font=self.font)
    
    def __write_doses_scheduled(self):
        msg = str('{:,}'.format(self.data["Doses_Scheduled_for_Today"]))
    
        w, h = self.draw.textsize(msg, font=self.font)
        size = ((self.width-w)/2, 950)

        self.draw.text(size, msg, fill="black", font=self.font)

    def __write_active_cases(self):
        msg = str('{:,}'.format(self.data["Active_Cases"]))
    
        w, h = self.draw.textsize(msg, font=self.font)
        size = ((self.width-w)/2, 950)

        self.draw.text(size, msg, fill="black", font=self.font)

    def __write_total_vaxx(self):
        msg = str('{:,}% (18+) / {:,}% (12+)'.format(self.data["Per_cent_All_Immunized_18"], self.data["Per_cent_All_Immunized_12"]))
    
        w, h = self.draw.textsize(msg, font=self.font)
        size = ((self.width-w)/2, 1175)

        self.draw.text(size, msg, fill="black", font=self.font)

    def __write_total_cases(self):
        msg = str('{:,}'.format(self.data["Total_Cases"]))
    
        w, h = self.draw.textsize(msg, font=self.font)
        size = ((self.width-w)/2, 1175)

        self.draw.text(size, msg, fill="black", font=self.font)
    
    def __write_partial_vaxx(self):
        msg = str('{:,}% (18+) / {:,}% (12+)'.format(self.data["Per_cent_Partially_Immunized_18"], self.data["Per_cent_Partially_Immunized_12"]))
    
        w, h = self.draw.textsize(msg, font=self.font)
        size = ((self.width-w)/2, 1400)

        self.draw.text(size, msg, fill="black", font=self.font)
    
    def __write_recovered(self):
        msg = str('{:,}'.format(self.data["Recovered"]))
    
        w, h = self.draw.textsize(msg, font=self.font)
        size = ((self.width-w)/2, 1400)

        self.draw.text(size, msg, fill="black", font=self.font)

    def __write_full_vaxx(self):
        msg = str('{:,}% (18+) / {:,}% (12+)'.format(self.data["Per_cent_Fully_Immunized_18"], self.data["Per_cent_Fully_Immunized_12"]))
    
        w, h = self.draw.textsize(msg, font=self.font)
        size = ((self.width-w)/2, 1625)

        self.draw.text(size, msg, fill="black", font=self.font)
    
    def __write_deaths(self):
        msg = str('{:,}'.format(self.data["Deaths"]))
    
        w, h = self.draw.textsize(msg, font=self.font)
        size = ((self.width-w)/2, 1625)

        self.draw.text(size, msg, fill="black", font=self.font)
