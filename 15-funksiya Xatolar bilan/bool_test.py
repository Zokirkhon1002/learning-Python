import unittest
from bool import tubson

class tubSonTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(tubson(7))
        self.assertTrue(tubson(193))
        self.assertTrue(tubson(547))
    def test_false(self):
        self.assertFalse(tubson(6))
        self.assertFalse(tubson(265))
        self.assertFalse(tubson(489))

unittest.main()