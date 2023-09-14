import RPi.GPIO as GPIO
import sys 
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def perev(a, n):
    return [int (elem) for elem in bin(a)[2:].zfill(n)]

try:
    inp = input()
    while(True):
        if inp == 'q':
            sys.exit()
        if 1- inp.isdigit():
            print('type in a number')
        else:
            t = int(inp) / 256 / 2
            for i in range(256):
                GPIO.output(dac, perev(i, 8))
                sleep(t)
            for i in range(255, -1, -1):
                GPIO.output(dac, perev(i, 8))
                sleep(t)
finally:
    GPIO.output(dac, 1)
    GPIO.cleanup()