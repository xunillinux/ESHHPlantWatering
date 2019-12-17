import Adafruit_DHT

class TemperatureSensor:

	def __init__(self):
		self.sensor = Adafruit_DHT.DHT11
		self.PIN = 4

	def Measure(self):
		#TODO measure few times over a second and take average
		humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.PIN)
		return temperature