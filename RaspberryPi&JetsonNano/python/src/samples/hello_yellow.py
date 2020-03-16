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
from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in13bc Demo")
    
    epd = epd2in13bc.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    time.sleep(1)
    
    # Drawing on the image
    logging.info("Drawing")    
    font20 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    
    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...") 
    HBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
    HRYimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126  ryimage: red or yellow image  
    drawblack = ImageDraw.Draw(HBlackimage)
    drawry = ImageDraw.Draw(HRYimage)
    drawry.text((10, 0), 'hello lilashik <3', font = font20, fill = 0)
    drawblack.text((10, 20), '2.13inch e-Paper bc', font = font20, fill = 0)
    epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
    time.sleep(2)
    
    # Drawing on the Vertical image
    logging.info("Goto Sleep...")
    epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    waveshare_epd.epdconfig.module_exit()
    exit()
