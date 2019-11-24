#!/usr/bin/env python3
from flask import Flask, request
from RPi import GPIO
from api import Controller

app = Flask( __name__ )

self.api_controller = Controller()

@app.route( "/api/GetHumidityValues", methods=["GET"] )
def GetHumidityValues():
    return self.api_controller.GetHumidityValues()

@app.route( "/api/GetBrightnessValues", methods=["GET"] )
def GetBrightnessValues():
    return self.api_controller.GetBrightnessValues()

@app.route( "/api/GetTemperatureValues", methods=["GET"] )
def GetTemperatureValues():
    return self.api_controller.GetTemperatureValues()

@app.route( "/api/GetFotos", methods=["GET"] )
def GetFotos():
    return self.api_controller.GetFotos()

@app.route( "/api/GetSettings", methods=["GET"] )
def GetSettings():
    return self.api_controller.GetSettings()

@app.route( "/api/SetSettings", methods=["POST"] )
def SetSettings():
    humidity_threshhold = request.args.get('humidity_threshhold', 0)
    pump_water_amount  = request.args.get('pump_water_amount', 0)
    api_controller.SetSettings(humidity_threshhold, pump_water_amount)