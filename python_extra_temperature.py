# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    current_temperature = temperature()
    display.scroll(current_temperature)
    sleep(1000)
    display.clear()
