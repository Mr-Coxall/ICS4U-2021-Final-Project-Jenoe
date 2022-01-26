#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on January 2022
# This program calls Google Sheets API

import gspread

# Accessing Google Spreadsheet service account
sa = gspread.service_account()
# Accessing Gooogle Spreadsheet file
sh = sa.open("ReminderClock")

# Accessing sheet within file
wks = sh.worksheet("Reminder Data")

# Gets Reminder Text
print(wks.acell('A2').value)

# Gets Time Value from spreadsheet and converts it into datetime value
print(wks.cell(2, 2).value)