import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 16]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def prever(a):
    return[int(elem) for elem in bin(a)[2:].zfill(8)]

def adc():
    for a in range(256):
        signal = prever(a)
        GPIO.output(dac, signal)
        compvalue = GPIO.input(comp)
        time.sleep(0.05)
        if compvalue == 0:
            return a

try: 
    while True:
        a = adc()
        if a != 0:
            print(a, '{:.2}v'.format(3.3*a/256))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()