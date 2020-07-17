from microbit import *

while True:
    if button_a.is_pressed():
        while True:
            pin0.write_digital(1)
            display.show(Image.HEART)
            sleep(1000)
            display.show(Image.HEART_SMALL)
            sleep(1000)
    else:
        display.show(Image.HAPPY)
        display.clear()