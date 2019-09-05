#!/usr/bin/env python3
from flask import Flask, request
from RPi import GPIO

# Create a flask app
app = Flask( __name__ )

# Define the pins
LED    = 18
BUTTON = 23

# Setup the GPIOs
GPIO.setmode( GPIO.BCM )
GPIO.setup( LED, GPIO.OUT )
GPIO.output( LED, True )

GPIO.setup( BUTTON, GPIO.IN )

@app.route( "/app/led", methods=["POST"] )
def ledcontroller():
    state = request.form["state"]

    if state == "on":
        GPIO.output( LED, False )
        return "LED is on"

    if state == "off":
        GPIO.output( LED, True )
        return "LED is off"

    return "LED unchanged"

@app.route( "/app/button/<nr>" )
def buttoncontroller( nr ):
    if nr == "0":
        if GPIO.input(BUTTON):
            return "1"
        else:
            return "0"

    return "invalid URL"
