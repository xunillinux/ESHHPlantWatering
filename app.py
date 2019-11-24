#!/usr/bin/env python3
from flask import Flask, request
from RPi import GPIO
import sys
sys.path.append('.')
sys.path.append('./api')
sys.path.append('./Handler')

from Controller import Controller
from Handler import Handler

app = Flask( __name__ )

api_controller = Controller()
handler = Handler()

@app.route( "/app/GetHumidityValues", methods=["GET"] )
def GetHumidityValues():
    return api_controller.GetHumidityValues()

@app.route( "/app/GetBrightnessValues", methods=["GET"] )
def GetBrightnessValues():
    return api_controller.GetBrightnessValues()

@app.route( "/app/GetTemperatureValues", methods=["GET"] )
def GetTemperatureValues():
    return api_controller.GetTemperatureValues()

@app.route( "/app/GetPhotos", methods=["GET"] )
def GetPhotos():
    return api_controller.GetPhotos()

@app.route( "/app/GetSettings", methods=["GET"] )
def GetSettings():
    return api_controller.GetSettings()

@app.route( "/app/SetSettings", methods=["POST"] )
def SetSettings():
    humidity_threshhold = request.args.get('humidity_threshhold', 0)
    pump_water_amount  = request.args.get('pump_water_amount', 0)
    api_controller.SetSettings(humidity_threshhold, pump_water_amount)

@app.route( "/app/ActivatePump", methods=["POST"] )
def ActivatePump():
    handler.ExecutePump()
    return "OK"