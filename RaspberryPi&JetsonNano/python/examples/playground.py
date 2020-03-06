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
import traceback

from random import seed
from random import randint

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in13bc Demo")
    
    epd = epd2in13bc.EPD()
    logging.info("init and Clear")
    epd.init()
    #epd.Clear()
    #time.sleep(1)
    
    # Drawing on the image
    logging.info("Drawing")    
    #font20 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)
    #font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    
    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...") 
    HBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
    HRYimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126  ryimage: red or yellow image  
    drawblack = ImageDraw.Draw(HBlackimage)
    drawry = ImageDraw.Draw(HRYimage)

    for dum in range(0,100):
	epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
	for dum2 in range(0,25):
	    x = randint(1,epd.height-1)
	    y = randint(1,epd.height-1)
    	    drawry.point((x-1,y), fill=0)
    	    drawry.point((x+1,y), fill=0)
    	    drawry.point((x,y-1), fill=0)
    	    drawry.point((x,y+1), fill=0)

	    x = randint(1,epd.height-1)
	    y = randint(1,epd.height-1)
	    drawblack.point((x,y), fill=0)

  
    #drawblack.text((10, 0), 'hello world', font = font20, fill = 0)

    #drawry.line((70, 50, 20, 100), fill = 0)
    #drawry.arc((140, 50, 190, 100), 0, 360, fill = 0)
    #drawry.rectangle((80, 50, 130, 100), fill = 0)
    #drawry.chord((85, 55, 125, 95), 0, 360, fill =1)


    time.sleep(2)
    
    logging.info("Goto Sleep...")
    epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13bc.epdconfig.module_exit()
    exit()
