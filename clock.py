#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on January 2022
# This program prints the current time

from datetime import datetime
import pytz

tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.now(tz_NY)
print(datetime_NY.strftime("%H:%M"))