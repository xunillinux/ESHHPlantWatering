#!/usr/bin/python

# Import required libraries
import sys
import os
import RPi.GPIO as GPIO # GPIO library we need to use the GPIO pins
import time # time library for sleep function

# GPIO pins for pump
StepPinForward=32

# Function for turning water pump on to suck from tub & push to plants
def pumpforward():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(StepPinForward, GPIO.OUT)
    print "Pump running for 5s"
    time.sleep(3)
    GPIO.cleanup()
    time.sleep(3)
    print "sleep for 5s"

try:
    while True:
        pumpforward()
except KeyboardInterrupt:
    GPIO.cleanup()
