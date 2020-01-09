import unittest
from sensorScripts.Pump import Pump
from sensorScripts.HumiditySensor import HumiditySensor

class SimpleTestCase(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.pump = Pump()
        self.humiditySensor = HumiditySensor()

    def tearDown(self):
        """Call after every test case."""

    def testPumpConvertWaterAmountInClToSeconds(self):
        assert self.pump.ConvertWaterAmountInCLToSeconds(10) == 4, "bar() not calculating values correctly"

    def testHumidityconvertToPercentageMinVal(self):
        assert self.humiditySensor.convertToPercentage(901) == 0

    def testHumidityconvertToPercentageMaxVal(self):
        assert self.humiditySensor.convertToPercentage(449) == 100

if __name__ == "__main__":
    unittest.main() # run all tests
