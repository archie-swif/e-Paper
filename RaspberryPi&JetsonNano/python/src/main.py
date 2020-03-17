#!/usr/bin/python
# -*- coding:utf-8 -*-
import time

from PIL import Image, ImageDraw

from display.display import Display

try:
    # 298/126
    display = Display()
    #
    # display.black.rectangle((32, 0, 94, 126), fill=0)
    # display.yellow.rectangle((64, 0, 128, 126), fill=0)
    #
    # # display.show_on_hardware()
    # display.show_on_software()


    epd = display.epd
    epd.init()
    epd.Clear()

    # Drawing on the Horizontal image
    HBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
    HRYimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126  ryimage: red or yellow image
    drawblack = ImageDraw.Draw(HBlackimage)
    drawry = ImageDraw.Draw(HRYimage)
    drawblack.line((20, 50, 70, 100), fill=0)
    drawblack.line((70, 50, 20, 100), fill=0)
    drawblack.rectangle((20, 50, 70, 100), outline=0)
    drawry.line((165, 50, 165, 100), fill=0)
    drawry.line((140, 75, 190, 75), fill=0)
    drawry.arc((140, 50, 190, 100), 0, 360, fill=0)
    drawry.rectangle((80, 50, 130, 100), fill=0)
    drawry.chord((85, 55, 125, 95), 0, 360, fill=1)
    epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
    time.sleep(2)
    epd.init()
    epd.Clear()

    epd.sleep()

except IOError as e:
    print(e)

except KeyboardInterrupt:
    exit()
