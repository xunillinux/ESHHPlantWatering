import sys
sys.path.append('.')
sys.path.append('./api')
sys.path.append('./sensorScripts')

from Controller import Controller
from HumiditySensor import HumiditySensor
from BrightnessSensor import BrightnessSensor
from TemperatureSensor import TemperatureSensor

class Handler:

    def __init__(self):
        self.controller = Controller()
        self.humiditySensor = HumiditySensor()
        self.brightnessSensor = brightnessSensor()
        self.temperatureSensor = TemperatureSensor()
    
    def ExecuteHumiditySensor(self):
        humidityValue = self.humiditySensor.Measure()
        self.controller.AddHumidityValue(humidityValue)
        return humidityValue
    
    def ExecuteBrightnessSensor(self):
        brightnessValue = self.brightnessSensor.Measure()
        self.controller.AddBrightnessValue(brightnessValue)
        return brightnessValue
    
    def ExectueTemperatureSensor(self):
        temperatureValue = self.temperatureSensor.Measure()
        self.controller.AddTemperatureValue(temperatureValue)
        return temperatureValue
    
    def ExecuteCamera(self):
        photo = self.camera.TakePhoto()
        self.controller.SetPhoto(photo)
        #TODO
        print("TODO")
    
    def ExecutePump(self):
        #TODO
        print("TODO")
    
    def Log(self):
        #TODO
        print("TODO")

    
