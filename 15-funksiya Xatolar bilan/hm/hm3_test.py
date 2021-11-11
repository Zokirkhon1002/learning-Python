import unittest
from hm3 import getEvenNumbers

class TestGetEvenNumbers(unittest.TestCase):
    def test_getEvenNumbers(self):
        self.assertEqual(getEvenNumbers(list(range(1, 10))), [2, 4, 6, 8])
        self.assertEqual(getEvenNumbers(list(range(1, 20))), [2, 4, 6, 8, 10,12,14,16,18])
        self.assertEqual(getEvenNumbers(list(range(1, 30))), [2, 4, 6, 8, 10,12,14,16,18,20,22,24,26,28])
        self.assertEqual(getEvenNumbers(list(range(1, 40))), [2, 4, 6, 8, 10,12,14,16,18,20,22,24,26,28,30,32,34,36,38])
        self.assertEqual(getEvenNumbers(list(range(1, 50))), [2, 4, 6, 8, 10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48])
        self.assertEqual(getEvenNumbers(list(range(1, 15))), [2, 4, 6, 8, 10,12,14])

unittest.main();