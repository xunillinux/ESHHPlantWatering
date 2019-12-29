import json

from api.Controller import Controller
from sensorScripts.HumiditySensor import HumiditySensor
from sensorScripts.BrightnessSensor import BrightnessSensor
from sensorScripts.TemperatureSensor import TemperatureSensor
from sensorScripts.Camera import Camera
from sensorScripts.Pump import Pump
import logging

class Handler:

    def __init__(self):
        self.controller = Controller()
        self.humiditySensor = HumiditySensor()
        self.brightnessSensor = BrightnessSensor()
        self.temperatureSensor = TemperatureSensor()
        self.camera = Camera()
        self.pump = Pump()

    def ExecuteAllSensors(self):
        self.ExecuteBrightnessSensor()
        self.ExectueTemperatureSensor()
        self.ExecuteCamera()
        humidity = self.ExecuteHumiditySensor()
        if(self.HumidityBelowThreshhold(humidity)):
            self.ExecutePump()
    
    def ExecuteHumiditySensor(self):
        humidityValue = self.humiditySensor.Measure()
        self.controller.AddHumidityValue(humidityValue)
        logging.info("Handler.py: Executing HumiditySensor")
        return humidityValue
    
    def ExecuteBrightnessSensor(self):
        brightnessValue = self.brightnessSensor.Measure()
        self.controller.AddBrightnessValue(brightnessValue)
        logging.info("Handler.py: Executing BrightnessSensor")
        return brightnessValue
    
    def ExectueTemperatureSensor(self):
        temperatureValue = self.temperatureSensor.Measure()
        self.controller.AddTemperatureValue(temperatureValue)
        logging.info("Handler.py: Executing TemperatureSensor")
        return temperatureValue
    
    def ExecuteCamera(self):
        photo = self.camera.TakePhoto()
        self.controller.SetPhoto(photo)
        logging.info("Handler.py: Executing Camera")

    
    def ExecutePump(self):
        settings = json.loads(self.controller.GetSettings())
        waterAmountCl = settings[0]["pump_water_amount"]
        self.pump.ExecutePump(waterAmountCl)
        logging.info("Handler.py: Executing Pump")

    
    def HumidityBelowThreshhold(self, humidity):
        settings = json.loads(self.controller.GetSettings())
        print(settings)
        humidityThreshhold = settings[0]["humidity_threshhold"]
        return humidity < humidityThreshhold
    
