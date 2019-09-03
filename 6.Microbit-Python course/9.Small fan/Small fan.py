from microbit import *
fun1 = Image("00990:90900:99999:00909:09900")
fun2 = Image("99009:09099:00900:99090:90099")
all_fun = [fun1, fun2]
while True:
    if button_a.is_pressed():
        while True:
            pin0.write_digital(1)
            display.show(all_fun, delay=100)
    else:
        display.show(Image.HEART)
        display.clear()
