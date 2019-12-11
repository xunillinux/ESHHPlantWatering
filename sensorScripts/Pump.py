import sys
from RPi import GPIO
import time

class Pump:

    def __init__(self):
        self.PIN = 32

    def ExecutePump(self, waterAmountCl):
        seconds = self.ConvertWaterAmountInCLToSeconds(waterAmountCl)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.PIN, GPIO.OUT)
        time.sleep(seconds)
        GPIO.cleanup()

    def ConvertWaterAmountInCLToSeconds(self, waterAmountCl):
        return waterAmountCl / 2.5

    def Log(self):
        #TODO
        print("TODO")