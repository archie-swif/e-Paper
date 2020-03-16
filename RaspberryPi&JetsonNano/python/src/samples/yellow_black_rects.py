#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13bc
import time
from PIL import Image, ImageDraw, ImageFont

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in13bc Demo")

    epd = epd2in13bc.EPD()
    epd.init()
    epd.Clear()
    time.sleep(1)

    # Drawing on the image
    logging.info("Drawing")
    font20 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)

    # Drawing on the Horizontal image
    black_image = Image.new('1', (epd.height, epd.width), 255)  # 298*126
    yellow_image = Image.new('1', (epd.height, epd.width), 255)  # 298*126  ryimage: red or yellow image
    draw_blk = ImageDraw.Draw(black_image)
    draw_ylw = ImageDraw.Draw(yellow_image)

    cell = 32

    row = 1
    draw_blk.rectangle((cell * row, cell * 0, cell * (row + 1), cell * 1))
    draw_blk.rectangle((cell * row, cell * 1, cell * (row + 1), cell * 2), fill=0, outline=0)
    draw_blk.rectangle((cell * row, cell * 2, cell * (row + 1), cell * 3), fill=0, outline=1)

    row = row + 1
    draw_blk.rectangle((cell * row, cell * 0, cell * (row + 1), cell * 1))
    draw_blk.rectangle((cell * row, cell * 1, cell * (row + 1), cell * 2), fill=1, outline=0)
    draw_blk.rectangle((cell * row, cell * 2, cell * (row + 1), cell * 3), fill=1, outline=1)

    row = row + 1
    draw_ylw.rectangle((cell * row, cell * 0, cell * (row + 1), cell * 1))
    draw_ylw.rectangle((cell * row, cell * 1, cell * (row + 1), cell * 2), fill=0, outline=0)
    draw_ylw.rectangle((cell * row, cell * 2, cell * (row + 1), cell * 3), fill=0, outline=1)

    row = row + 1
    draw_ylw.rectangle((cell * row, cell * 0, cell * (row + 1), cell * 1))
    draw_ylw.rectangle((cell * row, cell * 1, cell * (row + 1), cell * 2), fill=1, outline=0)
    draw_ylw.rectangle((cell * row, cell * 2, cell * (row + 1), cell * 3), fill=1, outline=1)

    # draw_blk.text((10, 0), 'hello world', font=font20, fill=0)
    # draw_blk.line((70, 50, 20, 100), fill=0)
    # draw_ylw.line((165, 50, 165, 100), fill=0)
    # draw_ylw.arc((140, 50, 190, 100), 0, 360, fill=0)
    # draw_ylw.rectangle((80, 50, 130, 100), fill=0)
    # draw_ylw.chord((85, 55, 125, 95), 0, 360, fill=1)
    # draw_ylw.point((100,100), fill=0);

    epd.display(epd.getbuffer(black_image), epd.getbuffer(yellow_image))

    time.sleep(2)
    epd.sleep()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in13bc.epdconfig.module_exit()
    exit()
