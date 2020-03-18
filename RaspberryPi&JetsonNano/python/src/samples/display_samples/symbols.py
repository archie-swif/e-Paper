#!/usr/bin/python
# -*- coding:utf-8 -*-
import time

from PIL import Image, ImageDraw

from display.display import Display
from display.symbols import Symbols

try:
    # w=104 h=212
    display = Display()

    A = Symbols.get_symbol('A')
    X = Symbols.get_symbol('X')
    NOT_A = Symbols.get_symbol('!A')

    display.print_symbol(A, 1, 0, display.black)
    display.print_symbol(X, 1, 1, display.black)
    display.print_symbol(NOT_A, 1, 2, display.black)

    display.print_symbol(A, 2, 0, display.yellow)
    display.print_symbol(X, 2, 1, display.yellow)
    display.print_symbol(NOT_A, 2, 2, display.yellow)

    display.black.rectangle((0, 24, 23, 31), fill=0)
    display.print_symbol(A, 3, 0, display.yellow)
    display.print_symbol(X, 3, 1, display.yellow)
    display.print_symbol(A, 3, 2, display.black)
    display.print_symbol(NOT_A, 3, 2, display.yellow)

    # display.show_on_hardware()
    display.show_on_software()
    # display.show_on_stub()

except IOError as e:
    print(e)

except KeyboardInterrupt:
    exit()
