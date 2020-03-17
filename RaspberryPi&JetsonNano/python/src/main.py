#!/usr/bin/python
# -*- coding:utf-8 -*-
import time

from PIL import Image, ImageDraw

from display.display import Display
from display.symbols import Symbols

try:
    # w=104 h=212
    display = Display()

    line = 0;
    char = 0;

    A = Symbols.get_symbol('A')
    X = Symbols.get_symbol('X')

    display.print_symbol(A, 1, 0, display.black)
    display.print_symbol(X, 1, 1, display.black)
    display.print_symbol(A, 2, 0, display.yellow)
    display.print_symbol(X, 2, 1, display.yellow)

    # display.yellow.ellipse((0, 0, 10, 10), fill=0)

    display.show_on_hardware()
    # display.show_on_software()
    # display.show_on_stub()

except IOError as e:
    print(e)

except KeyboardInterrupt:
    exit()
