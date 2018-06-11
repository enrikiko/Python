import unittest
from math import pi
from areaCircle import circle_area

class TestCirclesArea(unittest.TestCase):
    def test_area(self):
        #Test area when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

    def test_values(self):
        #Test area when radius < 0
        self.assertRaises(ValueError, circle_area, -2)

    def test_type(self):
        #Test aera when radius != number
        self.assertRaises(TypeError, circle_area, 1 + 3j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "Radius")
