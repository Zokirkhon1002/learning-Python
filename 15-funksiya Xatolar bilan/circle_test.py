import unittest
from circle import getArea, getPerimetr


class CircleTest(unittest.TestCase):
    def test_are(self):
        self.assertAlmostEqual(getArea(5),78.53975,3) # default precision is 7, but we can change it in settings with ,3;
    def test_Perimetr(self):
        self.assertAlmostEqual(getPerimetr(5),31.4159)

unittest.main()