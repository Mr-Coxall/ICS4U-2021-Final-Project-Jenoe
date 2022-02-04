#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on January 2022
# This program runs the Reminder Clock Program

import time
import board
import displayio
import terminalio
import constants
from adafruit_display_text.label import Label
from adafruit_bitmap_font import bitmap_font
from adafruit_matrixportal.network import Network
from adafruit_matrixportal.matrix import Matrix

BLINK = True
DEBUG = False

# Gets wifi details and account information from a secrets.py file
# to access adafruitio API
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise
print("Reminder Clock Program")
print("Time will be set for {}".format(secrets["timezone"]))

# Display setup
matrix = Matrix()
display = matrix.display
network = Network(status_neopixel=board.NEOPIXEL, debug=False)

# Drawing setup
group = displayio.Group()  # Create a Group
# Creates bitmap object (width, height, bit depth)
bitmap = displayio.Bitmap(64, 32, 2)
# Create the color palette to choose between different colours
color = displayio.Palette(4)  # Create a color palette
color[0] = 0x000000  # background
color[1] = 0xFFFFFF  # white
color[2] = 0xFF0000  # amber
color[3] = 0x85FF00  # green

# Create a TileGrid using the Bitmap and Palette
tile_grid = displayio.TileGrid(bitmap, pixel_shader=color)
# Add TileGrid to the group
group.append(tile_grid)
display.show(group)

# Set font
font = terminalio.FONT
clock_label = Label(font)

# This function sets the time
def update_time(*, hours=None, minutes=None, show_colon=False):
    # Gets the local time
    now = time.localtime()
    if hours is None:
        hours = now[3]
    if hours >= constants.NIGHT or hours < constants.MORNING:
        clock_label.color = color[1]
    # Daylight hours
    else:
        clock_label.color = color[1]
    # Time later than 12:59
    if hours > constants.MIL_TO_STAND:
        hours -= constants.MIL_TO_STAND
    # Time between 0:00 and 0:59
    elif not hours:
        hours = constants.MIL_TO_STAND
    if minutes is None:
        minutes = now[4]
    # Shows colon to separate hours from minutes
    if BLINK:
        colon = ":" if show_colon or now[5] % 2 else " "
    else:
        colon = ":"
    # Formats clock text
    clock_label.text = "{hours}{colon}{minutes:02d}".format(
        hours=hours, minutes=minutes, colon=colon
    )
    bbx, bby, bbwidth, bbh = clock_label.bounding_box
    # Center the time label
    clock_label.x = round(display.width / 2 - bbwidth / 2)
    clock_label.y = display.height // 2
    if DEBUG:
        print("Label bounding box: {},{},{},{}".format(bbx, bby, bbwidth, bbh))
        print("Label x: {} y: {}".format(clock_label.x, clock_label.y))

last_check = None
update_time(show_colon=True)  # Update time on the board
group.append(clock_label)  # add the clock label to the group

# Ensures that the board is taking the local time from the adafruit API
while True:
    if last_check is None or time.monotonic() > last_check + 3600:
        try:
            # Ensures that a colon is still there while updating
            update_time(
            show_colon=True
            )
            # Connects board to local time taken from the internet
            network.get_local_time()
            last_check = time.monotonic()
        except RuntimeError as e:
            print("Some error occured, retrying! -", e)
    update_time()
    time.sleep(1)
