import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 16]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
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

def volume(n):
    n = int(n / 256 * 10)
    mas = [0] * 8
    for i in range(n - 1):
        mas[i] = 1
    return mas

try: 
    while True:
        a = adc()
        if a != 0:
            GPIO.output(leds, volume(a))
            print(int(a / 256 * 10))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()