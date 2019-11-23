import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

HIGH = True #HIGH-Pegel
LOW = False #LOW-Pegel

#Funktionsdefinition
def readAnalogData(adcChannel, SCLKPin, MOSIPin, MISOPin, CSPin):
    #Pegel vorbereiten
    GPIO.output(CSPin, HIGH)
    GPIO.output(CSPin, LOW)
    GPIO.output(SCLKPin, LOW)

    sendcmd = adcChannel
    sendcmd |= 0b00011000
    
    #senden Bitkombi
    for i in range(5):
        if (sendcmd & 0x10):
            GPIO.output(MOSIPin, HIGH)
        else:
            GPIO.output(MOSIPin, LOW)
        #negative Flanke
        GPIO.output(SCLKPin, HIGH)
        GPIO.output(SCLKPin, LOW)
        sendcmd <<=1


    #empfangen der daten des adc
    adcvalue = 0
    for i in range(11):
        GPIO.output(SCLKPin, HIGH)
        GPIO.output(SCLKPin, LOW)
        adcvalue <<= 1
        if(GPIO.input(MISOPin)):
            adcvalue |= 0x01
    time.sleep(0.5)
    return adcvalue


ADC_Channel = 0
SCLK = 26
MOSI = 13
MISO = 19
CS = 20

GPIO.setup(SCLK, GPIO.OUT)
GPIO.setup(MOSI, GPIO.OUT)
GPIO.setup(MISO, GPIO.IN)
GPIO.setup(CS, GPIO.OUT)

while True:
    print (readAnalogData(ADC_Channel, SCLK, MOSI, MISO, CS))
