import os
import sys
import time

from PIL import Image, ImageDraw
# from waveshare_epd import epd2in13bc

class Display:
    resolution = (298, 126)

    black_img = Image.new('1', resolution, 255)
    yellow_img = Image.new('1', resolution, 255)
    black = ImageDraw.Draw(black_img)
    yellow = ImageDraw.Draw(yellow_img)

    # software display stuff
    color_img = Image.new('RGB', resolution, 255)

    # hardware display stuff
    epd = None

    def show_on_software(self):
        self.black_img.convert('RGB').show()
        self.yellow_img.convert('RGB').show()
        pass

    def lazy_init_hardware(self):
        # time.sleep(2)
        # self.epd = epd2in13bc.EPD()
        # self.epd = _EPD_Stub()
        self.epd.init()
        self.epd.Clear()
        time.sleep(1)

    def show_on_hardware(self):
        if not self.epd:
            self.lazy_init_hardware()

        black_buff = self.epd.getbuffer(self.black_img)
        yellow_buff = self.epd.getbuffer(self.yellow_img)
        self.epd.display(black_buff, yellow_buff)
        time.sleep(2)
        self.epd.sleep()


class _EPD_Stub:
    def reset(self):
        pass

    def send_command(self, command):
        pass

    def send_data(self, data):
        pass

    def ReadBusy(self):
        pass

    def init(self):
        return 0

    def getbuffer(self, image):
        return []

    def display(self, imageblack, imagered):
        pass

    def Clear(self):
        pass

    def sleep(self):
        pass