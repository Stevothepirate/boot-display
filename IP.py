#!/usr/bin/python

# Import Python sleep command from time library
from time import sleep

# Import driver for LCD screen from Adafruit library
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

# Import 'OS' & 'commands' Python librarys for Linux support
import os
import commands

# Run IP.sh script in the operating system to update IPe.txt & IPw.txt files
#os.system("./IP.sh")

# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
lcd = Adafruit_CharLCDPlate()

# Set the contents of IPe.txt to the variable called IPe
status, IPe = commands.getstatusoutput("cat /home/pi/i2c-disp/IPe.txt")

# Set the contents of IPw.txt to the variable called IPw
status, IPw = commands.getstatusoutput("cat /home/pi/i2c-disp/IPw.txt")

# Set a variable called 'host' containg the system hostname
status, host = commands.getstatusoutput("hostname")

# Clear display and show greeting, pause 5 sec (\n moves to next line)
lcd.clear()
lcd.message("     " + host)
sleep(5)

# Clears the display again and then displays IP address for 5 seconds
lcd.clear()
lcd.message("e " + IPe + "\nw " + IPw)
sleep(5)

# Cycle through backlight colors
#col = (lcd.RED , lcd.YELLOW, lcd.GREEN, lcd.TEAL,
#       lcd.BLUE, lcd.VIOLET, lcd.ON   , lcd.OFF)
#for c in col:
#    lcd.backlight(c)
#   sleep(.5)

# Poll buttons, display message & set backlight accordingly
btn = ((lcd.LEFT  , 'Left', lcd.BLUE),
       (lcd.UP    , 'Up', lcd.BLUE),
       (lcd.DOWN  , 'Down', lcd.BLUE),
       (lcd.RIGHT , 'Right', lcd.BLUE),
       (lcd.SELECT, 'Select', lcd.BLUE))
prev = -1
while True:
    for b in btn:
        if lcd.buttonPressed(b[0]):
            if b is not prev:
                lcd.clear()
                lcd.message(b[1])
                lcd.backlight(b[2])
                prev = b
            break
