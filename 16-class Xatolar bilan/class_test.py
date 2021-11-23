import unittest
from Class import Car


class CarTest(unittest.TestCase):
    """Car klassini tekshirish uchun test"""
    def setUp(self):
        """Test fayli yuklash"""
        self.make = "GM"
        self.model = "Malibu"
        self.year = 2021
        self.price = 40_000
        self.km = 10_000
        self.avto1 = Car(self.make, self.model, self.year)
        self.avto2 = Car(self.make, self.model, self.year, price=self.price, km=self.km)
    
    def test_create(self):
        
        # Qiymatlar mavjudligini asserIsNotNone metodi yordamida tekshirish
        self.assertIsNotNone(self.avto1.make)
        self.assertEqual(self.make, self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertEqual(self.model, self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        self.assertEqual(self.year, self.avto1.year)
        
        # Qiymat mavjud emasligini asserIsNone metodi yordamida tekshirish
        self.assertIsNone(self.avto1.price)
        
        # Qiymat tengligini assertEqual metodi yordamida tekshirish
        self.assertEqual(0,self.avto1.get_km())
        
        # avto2 narhini tekshirish
        self.assertEqual(self.price,self.avto2.price)
    
    def test_set_price(self):
        new_price = 45_000
        self.avto2.set_price(new_price)
        self.assertEqual(new_price, self.avto2.price)
    
    def test_add_km(self):
        #1 musbat qiymat berib tekshirib ko'ramiz.
        self.avto1.add_km(self.km)
        self.assertEqual(self.km, self.avto1.get_km())
        
        #2 manfiy qiymat berib tekshirib ko'ramiz.
        new_km = -500
        try:
            self.avto1.add_km(new_km)
        except ValueError as err:
            self.assertEqual(type(err), ValueError)
    
    def test_get_info(self):
        avto1_info = "GM Malibu 2021-yil 0km yurgan"
        self.assertEqual(avto1_info, self.avto1.get_info())
        
        # avto1 narhi va km o'zgartirib ko'ramiz.
        self.avto1.set_price(50_000)
        self.avto1.add_km(10_000)
        avto1_info = "GM Malibu 2021-yil 10000km yurgan Narhi: 50000"
        self.assertEqual(avto1_info, self.avto1.get_info())

unittest.main();