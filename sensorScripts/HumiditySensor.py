from MCP3008 import MCP3008 

class HumiditySensor:

    def __init__(self):
        self.adc = MCP3008()
    
    def Measure(self):
        #TODO measure few times over a second and take average
        value = self.adc.read( channel = 0 )
	print (value)
        convertedValue = value / 1023.0 * 3.3

    def Log(self):
        #TODO
        print("TODO")
