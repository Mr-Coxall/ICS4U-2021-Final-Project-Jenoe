#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on January 2022
# This program prints the current time

from datetime import datetime
import pytz

# Set timezone to EST for daylight savings
tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.now(tz_NY)
# Returns datetime to print on LED Matrix
print(datetime_NY.strftime("%H:%M"))