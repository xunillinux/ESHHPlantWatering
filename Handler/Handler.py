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
        logging.info("Handler.py: Executing HumiditySensor")
        humidityValue = self.humiditySensor.Measure()
        logging.info(humidityValue)
        self.controller.AddHumidityValue(humidityValue)
        return humidityValue
    
    def ExecuteBrightnessSensor(self):
        logging.info("Handler.py: Executing BrightnessSensor")
        brightnessValue = self.brightnessSensor.Measure()
        self.controller.AddBrightnessValue(brightnessValue)
        return brightnessValue
    
    def ExectueTemperatureSensor(self):
        logging.info("Handler.py: Executing TemperatureSensor")
        temperatureValue = self.temperatureSensor.Measure()
        self.controller.AddTemperatureValue(temperatureValue)
        return temperatureValue
    
    def ExecuteCamera(self):
        logging.info("Handler.py: Executing Camera")
        photoPath = self.camera.TakePhoto()
        self.controller.SetPhoto(photoPath)

    
    def ExecutePump(self):
        logging.info("Handler.py: Executing Pump")
        settings = json.loads(self.controller.GetSettings())
        waterAmountCl = settings[0]["pump_water_amount"]
        self.pump.ExecutePump(waterAmountCl)

    
    def HumidityBelowThreshhold(self, humidity):
        settings = json.loads(self.controller.GetSettings())
        print(settings)
        humidityThreshhold = settings[0]["humidity_threshhold"]
        return humidity < humidityThreshhold
    
