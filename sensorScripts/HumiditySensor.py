from sensorScripts.MCP3008 import MCP3008 
import logging

class HumiditySensor:

	def __init__(self):
		self.adc = MCP3008()
	
	def Measure(self):
		#TODO measure few times over a second and take average
		value = self.adc.read( channel = 0 )
		value = self.convertToPercentage(value)
		logging.info(value)
		return value
	
	def convertToPercentage(self, x):
		#genius algorithm!
		temp = x * -2
		temp = temp / 9
		temp = temp + 200
		if (temp < 0):
			temp = 0
		elif (temp > 100):
			temp = 100
		return int(temp)
