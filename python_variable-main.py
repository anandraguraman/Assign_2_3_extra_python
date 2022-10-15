# Imports go at the top
from microbit import *

counter = 0
# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
        counter = counter + 1
    if button_b.was_pressed():
        counter = counter - 1
    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll(counter)
