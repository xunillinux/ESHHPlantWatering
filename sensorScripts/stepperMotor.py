import time
import sys
from gpiozero import OutputDevice as stepper
IN1 = stepper(12)
IN2 = stepper(16)
IN3 = stepper(20)
IN4 = stepper(21)
stepPins = [IN1,IN2,IN3,IN4] # Motor GPIO pins</p><p>
stepDir = -1        # Set to 1 for clockwise
                           # Set to -1 for anti-clockwise
mode = 0            # mode = 1: Low Speed ==> Higher Power
                           # mode = 0: High Speed ==> Lower Power
if mode:              # Low Speed ==> High Power
  seq = [[1,0,0,1], # Define step sequence as shown in manufacturers datasheet
             [1,0,0,0], 
             [1,1,0,0],
             [0,1,0,0],
             [0,1,1,0],
             [0,0,1,0],
             [0,0,1,1],
             [0,0,0,1]]
else:                    # High Speed ==> Low Power 
  seq = [[1,0,0,0], # Define step sequence as shown in manufacturers datasheet
             [0,1,0,0],
             [0,0,1,0],
             [0,0,0,1]]
stepCount = len(seq)
if len(sys.argv)>1: # Read wait time from command line
  waitTime = int(sys.argv[1])/float(1000)
else:
  waitTime = 0.004    # 2 miliseconds was the maximun speed got on my tests
stepCounter = 0

while True:                          # Start main loop
  for pin in range(0,4):
    xPin=stepPins[pin]          # Get GPIO
    if seq[stepCounter][pin]!=0:
      xPin.on()
    else:
      xPin.off()
  stepCounter += stepDir
  if (stepCounter >= stepCount):
    stepCounter = 0
  if (stepCounter < 0):
    stepCounter = stepCount+stepDir
  time.sleep(waitTime)     # Wait before moving on</p>
