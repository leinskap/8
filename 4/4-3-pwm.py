import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
leds = [2, 3, 4, 17, 10, 22, 9]
gpio.setup(27, gpio.OUT)
gpio.setup(21, gpio.OUT)
gpio.setup(leds, gpio.OUT)
gpio.output(leds, 1)

p = gpio.PWM(21, 1000)

p.start(0)
try:
    while(True):
        dutyCycle=int(input())
        p.start(dutyCycle)
        print('предполагаемое значение напряжения:', 3.3/100 * dutyCycle)
        input()
        break
finally:
    p.stop()
    gpio.cleanup()
