#!/usr/bin/env python3

from flask import Flask, request

import logging
logging.basicConfig(filename='apilogfile.log',level=logging.DEBUG)

from api.Controller import Controller
from Handler.Handler import Handler

api_controller = Controller()
handler = Handler()

app = Flask( __name__ )


@app.route('/app')
def apiDefinition():
    return 'API Definition: GetHumidityValues, TODO'

@app.route( "/app/GetHumidityValues", methods=["GET"] )
def GetHumidityValues():
    logging.info("app.py: API-call GetHumidityValues")
    return api_controller.GetHumidityValues()

@app.route( "/app/GetBrightnessValues", methods=["GET"] )
def GetBrightnessValues():
    logging.info("app.py: API-call GetBrightnessValues")
    return api_controller.GetBrightnessValues()

@app.route( "/app/GetTemperatureValues", methods=["GET"] )
def GetTemperatureValues():
    logging.info("app.py: API-call GetTemperatureValues")
    return api_controller.GetTemperatureValues()

@app.route( "/app/GetPhotos", methods=["GET"] )
def GetPhotos():
    logging.info("app.py: API-call GetPhotos")
    return api_controller.GetPhotos()

@app.route( "/app/GetSettings", methods=["GET"] )
def GetSettings():
    logging.info("app.py: API-call GetSettings")
    return api_controller.GetSettings()

@app.route( "/app/SetSettings", methods=["POST"] )
def SetSettings():
    humidity_threshhold = request.args.get('humidity_threshhold', 0)
    pump_water_amount  = request.args.get('pump_water_amount', 0)
    logging.info("app.py: API-call SetSettings(humidity_threshhold=%s,pump_water_amount=%s)" % (humidity_threshhold,pump_water_amount))
    api_controller.SetSettings(humidity_threshhold, pump_water_amount)

@app.route( "/app/ActivatePump", methods=["POST"] )
def ActivatePump():
    logging.info("app.py: API-call ActivatePump")
    handler.ExecutePump()
    return "OK"

if (__name__ == "__main__"):
    app.run(host='0.0.0.0')
