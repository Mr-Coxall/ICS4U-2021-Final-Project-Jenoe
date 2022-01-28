#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on January 2022
# This program prints the current time

import time

t = time.localtime()
current_time = time.strftime("%H:%M", t)
print(current_time)