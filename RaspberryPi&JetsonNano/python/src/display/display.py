import logging
import os
import sys
import time

from PIL import Image, ImageDraw

from stub.EPD_Stub import EPD_STUB


class Display:
    black_img = None
    yellow_img = None
    black = None
    yellow = None

    # software display stuff
    color_img = None

    # hardware display stuff
    epd = None

    # hardware stub display stuff
    epd_stub = None

    def __init__(self):
        self.resolution = (104, 212)
        self.black_img = Image.new('1', self.resolution, 255)
        self.yellow_img = Image.new('1', self.resolution, 255)
        self.color_img = Image.new('RGB', self.resolution, 255)
        self.black = ImageDraw.Draw(self.black_img)
        self.yellow = ImageDraw.Draw(self.yellow_img)

    def print_symbol(self, symbol, line, char, draw):
        for y in range(len(symbol)):
            for x in range(len(symbol[y])):
                if symbol[y][x] == 1:
                    draw.point((x + char * 8, y + line * 8), fill=0)

    def show_on_software(self):
        # self.black_img.convert('RGB').show()
        # self.yellow_img.convert('RGB').show()

        yellow_color = (255, 255, 0)
        black_color = (0, 0, 0)

        self.color_img = self.black_img.convert('RGB')

        width, height = self.yellow_img.size
        for y in range(height):
            for x in range(width):
                if self.yellow_img.getpixel((x, y)) == 0:
                    self.color_img.putpixel((x, y), yellow_color)

        self.color_img.show()

    def lazy_init_hardware(self):
        from waveshare_epd import epd2in13bc
        self.epd = epd2in13bc.EPD()
        self.epd.init()
        self.epd.Clear()

    def show_on_hardware(self):
        if not self.epd:
            self.lazy_init_hardware()

        black_buff = self.epd.getbuffer(self.black_img)
        yellow_buff = self.epd.getbuffer(self.yellow_img)
        self.epd.display(black_buff, yellow_buff)

    def show_on_stub(self):
        self.epd_stub = EPD_STUB(self.resolution)

        black_buff = self.epd_stub.getbuffer(self.black_img)
        yellow_buff = self.epd_stub.getbuffer(self.yellow_img)
        self.epd_stub.display(black_buff, yellow_buff)


def sleep(self):
    self.epd.sleep()
