#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import sys

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
import time
from PIL import Image, ImageDraw
from waveshare_epd import epd2in13bc

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in13bc_d3m0")

    # -------------------------------------------------------
    epd = epd2in13bc.EPD()
    epd.init()

    # Init black and yellow screens
    logging.info("Screen init")
    b_image = Image.new('1', (epd.height, epd.width), 255)  # 298*126
    y_image = Image.new('1', (epd.height, epd.width), 255)  # 298*126  ryimage: red or yellow image
    black_screen = ImageDraw.Draw(b_image)
    yellow_screen = ImageDraw.Draw(y_image)

    # -------------------------------------------------------
    # yellow_screen.point((100, 100), fill=0)
    # yellow_screen.line((70, 50, 20, 100), fill = 0)
    # yellow_screen.arc((140, 50, 190, 100), 0, 360, fill = 0)
    # yellow_screen.rectangle((80, 50, 130, 100), fill = 0)
    # yellow_screen.chord((85, 55, 125, 95), 0, 360, fill =1)
    # font20 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)
    # yellow_screen.text((10, 0), 'hello world', font=font20, fill=0)
    # -------------------------------------------------------

    epd.Clear()

    yellow_screen.rectangle((25, 25, 125, 125), fill=0)
    black_screen.rectangle((150, 25, 250, 125), fill=0)

    # -------------------------------------------------------
    epd.display(epd.getbuffer(b_image), epd.getbuffer(y_image))
    time.sleep(2)
    epd.sleep()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    waveshare_epd.epdconfig.module_exit()
    exit()
