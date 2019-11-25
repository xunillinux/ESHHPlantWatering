import sys
sys.path.append('.')
sys.path.append('./api')
sys.path.append('./sensorScripts')

import json

from Controller import Controller
from HumiditySensor import HumiditySensor
from BrightnessSensor import BrightnessSensor
from TemperatureSensor import TemperatureSensor
from Camera import Camera
from Pump import Pump

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
        #TODO LOG
        return humidityValue
    
    def ExecuteBrightnessSensor(self):
        brightnessValue = self.brightnessSensor.Measure()
        self.controller.AddBrightnessValue(brightnessValue)
        #TODO LOG
        return brightnessValue
    
    def ExectueTemperatureSensor(self):
        temperatureValue = self.temperatureSensor.Measure()
        self.controller.AddTemperatureValue(temperatureValue)
        #TODO LOG
        return temperatureValue
    
    def ExecuteCamera(self):
        photo = self.camera.TakePhoto()
        self.controller.SetPhoto(photo)
        #TODO LOG
    
    def ExecutePump(self):
        settings = json.loads(self.controller.GetSettings())
        waterAmountCl = settings[0]["pump_water_amount"]
        self.pump.ExecutePump(waterAmountCl)
        #TODO LOG
    
    def HumidityBelowThreshhold(self, humidity):
        settings = json.loads(self.controller.GetSettings())
        humidityThreshhold = settings[0]["humidity_threshhold"]
        return humidity < humidityThreshhold

    def Log(self):
        #TODO
        print("TODO")

    
