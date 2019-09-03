from microbit import *
stop = Image("00900:09990:90909:09090:09090")
go = Image("00900:09990:90909:09090:90009")
while True:
    pin0.write_digital(1)
    pin1.write_digital(0)
    pin2.write_digital(0)
    display.show(stop)
    sleep(10000)
    pin0.write_digital(0)
    pin1.write_digital(1)
    pin2.write_digital(0)
    display.show(go)
    sleep(10000)
