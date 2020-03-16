import os
import sys
import time

from PIL import Image, ImageDraw


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
        from waveshare_epd import epd2in13bc
        self.epd = epd2in13bc.EPD()
        self.epd.init()

    def show_on_hardware(self):
        if not self.epd:
            self.lazy_init_hardware()

        black_buff = self.epd.getbuffer(self.black_img)
        yellow_buff = self.epd.getbuffer(self.yellow_img)
        self.epd.display(black_buff, yellow_buff)
        self.epd.sleep()
        time.sleep(2)