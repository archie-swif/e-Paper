#!/usr/bin/python
# -*- coding:utf-8 -*-
from display.display import Display

try:
    # 298/126
    display = Display()

    cell = 32;
    row = 1;

    row = 1
    display.black.rectangle((cell * row, cell * 0, cell * (row + 1), cell * 1))
    display.black.rectangle((cell * row, cell * 1, cell * (row + 1), cell * 2), fill=0, outline=0)
    display.black.rectangle((cell * row, cell * 2, cell * (row + 1), cell * 3), fill=0, outline=1)

    row = row + 1
    display.black.rectangle((cell * row, cell * 0, cell * (row + 1), cell * 1))
    display.black.rectangle((cell * row, cell * 1, cell * (row + 1), cell * 2), fill=1, outline=0)
    display.black.rectangle((cell * row, cell * 2, cell * (row + 1), cell * 3), fill=1, outline=1)

    # display.show_on_hardware()
    display.show_on_software()

except IOError as e:
    pass

except KeyboardInterrupt:
    exit()
