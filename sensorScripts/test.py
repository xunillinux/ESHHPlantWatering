#from TemperatureSensor import TemperatureSensor
#from BrightnessSensor import BrightnessSensor
from HumiditySensor import HumiditySensor
#from Camera import Camera

#sensor = TemperatureSensor()
#print (sensor.Measure())


#sensor = BrightnessSensor()
#print (sensor.Measure())

sensor = HumiditySensor()
print (sensor.Measure())
