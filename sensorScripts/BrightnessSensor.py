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
		value = self.convertToPercentage(value)
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
		while(GPIO.input(pin_to_circuit) == GPIO.LOW and count<7500):
			count += 1
		return count

	def convertToPercentage(self, x):
		#genius algorithm!
		temp = x * -2
		temp = temp / 145
		temptemp = 3000/29
		temp = temp + temptemp
		if (temp < 0):
			temp = 0
		elif (temp > 100):
			temp = 100
		return int(temp)
