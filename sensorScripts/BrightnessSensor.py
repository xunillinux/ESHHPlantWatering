import RPi.GPIO as GPIO
import time

class BrightnessSensor:

    def __init__(self):
        self.pin_to_circuit = 7

    def Measure(self):
		GPIO.setmode(GPIO.BOARD)
        #TODO measure few times over a second and take average
		print(self.rc_time(pin_to_circuit))
		GPIO.cleanup()


	def rc_time (self, pin_to_circuit):
		count = 0

		#Output on the pin for
		GPIO.setup(pin_to_circuit, GPIO.OUT)
		GPIO.output(pin_to_circuit, GPIO.LOW)
		time.sleep(0.1)

		#Change the pin back to input 
		GPIO.setup(pin_to_circuit, GPIO.IN)

		#Count until the pin goes high
		while (GPIO.input(pin_to_circuit) == GPIO.LOW):
				count += 1
		return count

    def Log(self):
        #TODO
        print("TODO")