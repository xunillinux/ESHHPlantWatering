from sensorScripts.MCP3008 import MCP3008 
import logging

class HumiditySensor:

	def __init__(self):
		self.adc = MCP3008()
	
	def Measure(self):
		#TODO measure few times over a second and take average
		value = self.adc.read( channel = 0 )
		logging.info(value)
		return value
