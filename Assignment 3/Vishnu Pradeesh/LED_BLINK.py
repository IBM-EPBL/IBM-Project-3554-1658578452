import RPI.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)    // setting RPi in BOARD mode
GPIO.setup(10,GPIO.OUT,initial = GPIO.LOW)   // setting GPIO pin 10 as Output and initialize with 0

while True:
	GPIO.output(10,GPIO.HIGH)   //setting GPIO pin 10 as High
	sleep(1)                   // Sleep for 1 sec
	GPIO.output(10,GPIO.LOW)    // setting GPIO pin 10 as Low
	sleep(1)