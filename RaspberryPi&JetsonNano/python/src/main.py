#!/usr/bin/python
# -*- coding:utf-8 -*-
from display.display import Display

try:
    # 298/126
    display = Display()

    display.black.rectangle((32, 0, 94, 126), fill=0)
    display.yellow.rectangle((64, 0, 128, 126), fill=0)

    # display.show_on_hardware()
    display.show_on_software()

except IOError as e:
    print(e)

except KeyboardInterrupt:
    exit()
