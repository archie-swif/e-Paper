#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13d
from PIL import Image

#Set output log level
logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in13d Demo")
    
    epd = epd2in13d.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear(0xFF)
    
    logging.info("3.read bmp file")
    Himage = Image.open(os.path.join(picdir, 'dots2.bmp'))
    epd.display(epd.getbuffer(Himage))
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    waveshare_epd.epdconfig.module_exit()
    exit()
