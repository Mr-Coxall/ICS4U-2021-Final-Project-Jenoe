#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on January 2022
# This program runs the Reminder Clock Program

import adafruit_display_text.label
import board
import displayio
import framebufferio
import rgbmatrix
import terminalio

# Replaces previous displays with new display being created
displayio.release_displays()

# Creates martix object
matrix = rgbmatrix.RGBMatrix(
    width=64, height=32, bit_depth=1,
    rgb_pins=[board.D6, board.D5, board.D9, board.D11, board.D10, board.D12],
    addr_pins=[board.A5, board.A4, board.A3, board.A2],
    clock_pin=board.D13, latch_pin=board.D0, output_enable_pin=board.D1)

# Associates RGB matrix with a display to enable displayio features
display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)

# Create two lines of text to scroll
line = adafruit_display_text.label.Label(
    terminalio.FONT,
    color=0xff0000,
    text="Hello, World!")
line.x = display.width
line.y = 8

# Apply scroll text effect
while True:
    scroll(line)
    display.refresh(minimum_frames_per_second=0)