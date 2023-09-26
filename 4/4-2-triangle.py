import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
numbers=[x for x in range (0,256)]
gpio.setup(dac, gpio.OUT)

gpio.output(dac, 0)
gpio.cleanup()