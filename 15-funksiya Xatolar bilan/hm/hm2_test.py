import unittest
from hm2 import getCapitalized

class TestGetCapitalized(unittest.TestCase):
    def test_getCapitalized(self):
        self.assertEqual(getCapitalized("zokirkhon kotibkhonov"),"Zokirkhon Kotibkhonov")
        self.assertEqual(getCapitalized("khurshidbek alisherov"),"Khurshidbek Alisherov")
        self.assertEqual(getCapitalized("sayfullokhon ulukhodjaev"),"Sayfullokhon Ulukhodjaev")

unittest.main()