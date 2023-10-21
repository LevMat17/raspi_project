import RPi.GPIO as GPIO
import time

PIN=3

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.IN)

while(1):
    time.sleep(1)
    print(GPIO.input(PIN))