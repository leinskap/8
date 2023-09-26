import RPi.GPIO as gpio
dac = [8, 11, 7, 1, 0, 5, 12, 6]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
def decToBinary(decimal):
    return [int(x) for x in bin(decimal)[2:].zfill(8)]
try:
    while(True):
        a = input()
        if a=='q':
            break
        elif (a.isnumeric() and float(a)%1==0 and int(a)>=0 and int(a)<256):
            a = int(a)
            gpio.output(dac,decToBinary(a))
            print("Предполагаемое значение напряжения: ", ('{:.4f}'.format(3.3/256 * a)))
        elif any(x.isalpha() for x in a):
            print('не числовое значение')
        elif float(a)<0:
            print('отрицательное число') 
        elif float(a)%1!=0:
            print('не целое число')
        elif float(a)>255:
            print('значение превышает возможности 8-разрядного ЦАП')
finally:
    gpio.output(dac, 0)