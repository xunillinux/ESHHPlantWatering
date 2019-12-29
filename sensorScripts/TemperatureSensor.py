import Adafruit_DHT

class TemperatureSensor:

	def __init__(self):
		self.sensor = Adafruit_DHT.DHT11
		self.PIN = 4

	def Measure(self):
		# Tries 15 times to get a sensor reading (waiting 2 seconds between each retry)
		humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.PIN)
		return temperature if temperature is not None else 0