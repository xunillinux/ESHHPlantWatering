import RPi.GPIO as GPIO
import time
import random
import logging

class Led:

    def __init__(self):
        self.P_RED = 29
        self.P_GREEN = 31
        self.P_BLUE = 33
        self.fPWM = 50 
	

    def setup(self):
        global pwmR, pwmG, pwmB
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.P_RED, GPIO.OUT)
        GPIO.setup(self.P_GREEN, GPIO.OUT)
        GPIO.setup(self.P_BLUE, GPIO.OUT)
        pwmR = GPIO.PWM(self.P_RED, self.fPWM)
        pwmG = GPIO.PWM(self.P_GREEN, self.fPWM)
        pwmB = GPIO.PWM(self.P_BLUE, self.fPWM)
        pwmR.start(0)
        pwmG.start(0)
        pwmB.start(0)

    def setColor(self, r, g, b):
        pwmR.ChangeDutyCycle(int(r / 255 * 100))
        pwmG.ChangeDutyCycle(int(g / 255 * 100))
        pwmB.ChangeDutyCycle(int(b / 255 * 100))

    def SetLedColorRed(self):
        self.setup()
        r = 255
        g = 0
        b = 0
        logging.info("R: " + str(r) + " G: "+str(g)+" B: "+str(b))
        self.setColor(r,g,b)
        time.sleep(5)
        self.setColor(0,0,0)
        GPIO.cleanup()

    def SetLedColorGreen(self):
        self.setup()
        r = 0
        g = 255
        b = 0
        logging.info(" R: "+str(r)+" G: "+str(g)+" B: "+str(b))
        self.setColor(r, g, b)
        time.sleep(5)
        self.setColor(0,0,0)
        GPIO.cleanup()

