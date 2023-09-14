import RPi.GPIO as GPIO
import sys 
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def perev(a, n):
    return [int (elem) for elem in bin(a)[2:].zfill(n)]

try:
    while (True):
        a = input('input 0-255')
        if a == 'q':
            sys.exit()
        elif a.isdigit() and 0 <= int(a) and int(a) <= 255:
            GPIO.output(dac, perev(int(a), 8))
            time.sleep(2)
            print("{:.4f".format(int(a) / 256 * 3.3))
        elif not a.isdigit():
            print('input number 0-255')
    
except ValueError:
    print('input number 0-255')
except KeyboardInterrupt:
    print('done')
finally: 
    GPIO.output(dac, 0)
    GPIO.cleanup()