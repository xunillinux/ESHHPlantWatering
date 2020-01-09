import json

from api.Controller import Controller
from sensorScripts.HumiditySensor import HumiditySensor
from sensorScripts.BrightnessSensor import BrightnessSensor
from sensorScripts.TemperatureSensor import TemperatureSensor
from sensorScripts.Camera import Camera
from sensorScripts.Pump import Pump
from sensorScripts.led import Led
import logging

class Handler:

    def __init__(self):
        self.controller = Controller()
        self.humiditySensor = HumiditySensor()
        self.brightnessSensor = BrightnessSensor()
        self.temperatureSensor = TemperatureSensor()
        self.camera = Camera()
        self.pump = Pump()
        self.succesfullyExecutedAllSensors = True
        self.led = Led()

    def ExecuteAllSensors(self):
        self.succesfullyExecutedAllSensors = True
        self.ExecuteBrightnessSensor()
        self.ExectueTemperatureSensor()
        self.ExecuteCamera()
        humidity = self.ExecuteHumiditySensor()
        if(self.HumidityBelowThreshhold(humidity)):
            self.ExecutePump()
        if(self.succesfullyExecutedAllSensors == False):
            self.SetLedColorRed()
        else:
            self.SetLedColorGreen()
    
    def ExecuteHumiditySensor(self):
        logging.info("Handler.py: Executing HumiditySensor")
        humidityValue = self.humiditySensor.Measure()
        logging.info(humidityValue)
        self.controller.AddHumidityValue(humidityValue)
        if(humidityValue == 0):
            self.succesfullyExecutedAllSensors = False
        return humidityValue
    
    def ExecuteBrightnessSensor(self):
        logging.info("Handler.py: Executing BrightnessSensor")
        brightnessValue = self.brightnessSensor.Measure()
        self.controller.AddBrightnessValue(brightnessValue)
        if(brightnessValue == 0):
            self.succesfullyExecutedAllSensors = False
        return brightnessValue
    
    def ExectueTemperatureSensor(self):
        logging.info("Handler.py: Executing TemperatureSensor")
        temperatureValue = self.temperatureSensor.Measure()
        self.controller.AddTemperatureValue(temperatureValue)
        return temperatureValue
    
    def ExecuteCamera(self):
        logging.info("Handler.py: Executing Camera")
        photoPath = self.camera.TakePhoto()
        if(photoPath == ""):
            self.succesfullyExecutedAllSensors = False
        self.controller.SetPhoto(photoPath)

    
    def ExecutePump(self):
        logging.info("Handler.py: Executing Pump")
        settings = json.loads(self.controller.GetSettings())
        waterAmountCl = settings[0]["pump_water_amount"]
        self.pump.ExecutePump(waterAmountCl)

    def SetLedColorRed(self):
        self.led.SetLedColorRed()
    
    def SetLedColorGreen(self):
        self.led.SetLedColorGreen()
    
    def HumidityBelowThreshhold(self, humidity):
        settings = json.loads(self.controller.GetSettings())
        humidityThreshhold = settings[0]["humidity_threshhold"]
        return humidity < humidityThreshhold
    
