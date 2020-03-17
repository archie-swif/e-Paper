#!/usr/bin/python
# -*- coding:utf-8 -*-
import time

from PIL import Image, ImageDraw

from display.display import Display

try:
    # 298/126
    display = Display()

    display.black.rectangle((0, 32, 104, 96), fill=0)
    display.yellow.rectangle((0, 64, 104, 160), fill=0)
    display.black.rectangle((0, 128, 104, 192), fill=0)

    display.show_on_hardware()
    # display.show_on_software()
    # display.show_on_stub()

except IOError as e:
    print(e)

except KeyboardInterrupt:
    exit()
