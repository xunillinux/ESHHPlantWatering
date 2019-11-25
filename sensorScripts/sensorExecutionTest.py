from TemperatureSensor import TemperatureSensor
from BrightnessSensor import BrightnessSensor
from HumiditySensor import HumiditySensor

sensor = TemperatureSensor()
print("#Temperature Value#")
print (sensor.Measure())

print("#Brightness Value#")
sensor = BrightnessSensor()
print (sensor.Measure())

print("#Humidity Value#")
sensor = HumiditySensor()
print (sensor.Measure())