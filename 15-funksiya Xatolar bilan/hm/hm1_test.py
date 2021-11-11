import unittest
from hm1 import getMax

class GetMaxTest(unittest.TestCase):
    def test_getMax_1(self):
        self.assertEqual(getMax(11,15,1), 15)
        self.assertEqual(getMax(112,15,1), 112)
        self.assertEqual(getMax(11,15,19), 19)

unittest.main();