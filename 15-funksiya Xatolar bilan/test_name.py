# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 02:13:20 2021

@author: Zokirkhon
"""

import unittest # test case
from name import get_full_name

##1
class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        name  = get_full_name("zokirkhon","kotibkhonov")
        self.assertEqual(name, "Zokirkhon Kotibkhonov")
    def test_otasining_ismi(self):
        name  = get_full_name("zokirkhon","zokhidkhon ugli","kotibkhonov")
        self.assertEqual(name,"Zokirkhon Kotibkhonov Zokhidkhon Ugli")

unittest.main()