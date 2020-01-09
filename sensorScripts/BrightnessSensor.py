import RPi.GPIO as GPIO
import time
import logging

class BrightnessSensor:

	def __init__(self):
		self.pin_to_circuit = 11
	def Measure(self):
		GPIO.setmode(GPIO.BOARD)
		#TODO measure few times over a second and take average
		#TODO convert into some brightness value
		value = self.Rc_time(self.pin_to_circuit)
		logging.info(value)
		GPIO.cleanup()
		return value

	def Rc_time(self, pin_to_circuit):
		count = 0
		GPIO.setup(pin_to_circuit, GPIO.OUT)
		GPIO.output(pin_to_circuit, GPIO.LOW)
		time.sleep(0.1)
		GPIO.setup(pin_to_circuit, GPIO.IN)
		#Raise counter until pin goes high
		while(GPIO.input(pin_to_circuit) == GPIO.LOW and count<1500):
			count += 1
		return count
