#!/usr/bin/env python3
from flask import Flask, request
from RPi import GPIO

# Create a flask app
app = Flask( __name__ )

# Define the pin
LED = 18

# Set it up
GPIO.setmode( GPIO.BCM )
GPIO.setup( 18, GPIO.OUT )

@app.route( "/app/led/<state>" )
def ledcontroller( state ):
    if state == "on":
        GPIO.output( LED, False )
        return "LED is on"

    if state == "off":
        GPIO.output( LED, True )
        return "LED is off"

    return "LED unchanged"
