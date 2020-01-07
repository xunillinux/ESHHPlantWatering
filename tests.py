import unittest
from sensorScripts.Pump import Pump

class SimpleTestCase(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.pump = Pump()

    def tearDown(self):
        """Call after every test case."""

    def testA(self):
        """Test case A. note that all test method names must begin with 'test.'"""
        assert self.pump.ConvertWaterAmountInCLToSeconds(10) == 4, "bar() not calculating values correctly"


if __name__ == "__main__":
    unittest.main() # run all tests
