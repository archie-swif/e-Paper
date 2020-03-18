#!/usr/bin/python
# -*- coding:utf-8 -*-
import time

from PIL import Image, ImageDraw

from display.display import Display

try:
    # w=104 h=212
    display = Display()

    display.black.ellipse((26, 26, 78, 78), fill=0)
    display.yellow.ellipse((26, 52, 78, 104), fill=0)

    # display.show_on_hardware()
    display.show_on_software()
    # display.show_on_stub()

except IOError as e:
    print(e)

except KeyboardInterrupt:
    exit()
