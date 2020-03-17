#!/usr/bin/python
# -*- coding:utf-8 -*-
import time

from PIL import Image, ImageDraw

from display.display import Display

try:
    # 298/126
    display = Display()

    display.black.rectangle((32, 0, 128, 104), fill=0)
    display.yellow.rectangle((64, 0, 160, 104), fill=0)

    # display.show_on_hardware()
    display.show_on_software()

except IOError as e:
    print(e)

except KeyboardInterrupt:
    exit()
