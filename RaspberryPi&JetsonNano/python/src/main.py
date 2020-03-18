#!/usr/bin/python
# -*- coding:utf-8 -*-
import random
import time

from PIL import Image, ImageDraw

from display.display import Display
from display.symbols import Symbols

try:
    # w=104 h=212
    display = Display()

    X = Symbols.get_symbol('X')
    for i in range(0, 1000):
        display.print_symbol(X, random.randrange(0, 27), random.randrange(0, 13), display.black)
        display.print_symbol(X, random.randrange(0, 27), random.randrange(0, 13), display.yellow)
        display.show_on_hardware()

    # display.show_on_stub()
    # display.show_on_software()


except IOError as e:
    print(e)

except KeyboardInterrupt:
    exit()
