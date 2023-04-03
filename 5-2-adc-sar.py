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
    a = 0
    for i in range(7, -1, -1):
        a += 2**i
        GPIO.output(dac, prever(a))
        time.sleep(0.05)
        if GPIO.input(comp) == 0:
            a -= 2**i
    return a

try: 
    while True:
        a = adc()
        if a != 0:
            print(a, '{:.2}v'.format(3.3*a/256))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()