# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 21:19:24 2021

@author: Zokirlhon
Amaliyot
Uyga vazifa
"""


### 1
class Avto():
    """Yagni Avtomobile yasash uchun klass"""
    def __init__(self,model,color,price,brand,made_in):
        """Avtomobile ning xususiyatlarini kiriting"""
        self.model = model
        self.color = color
        self.price = price
        self.brand = brand
        self.made_in = made_in
        self.km = 0
    
    def get_model(self):
        """Avtomobile ning modelini ko'rish"""
        return self.model
    
    def get_color(self):
        """Avtomobile ning rangini ko'rish"""
        return self.color
    
    def get_price(self):
        """Avtomobile ning narhini ko'rish"""
        return self.price
    
    def get_brand(self):
        """Avtomobile ning brendini ko'rish"""
        return self.brand
    
    def get_made_in(self):
        """Avtomobile ning qayerda ishlab chiqarilganini ko'rish"""
        return self.made_in
    
    def get_km(self):
        """Avtomobile ning qancha km yurganini ko'rish ko'rish"""
        return self.km
    
    def get_info(self):
        return (f"Avtomobilning modeli: {self.model}"
                f"\nAvtomobilning rangi: {self.color}"
                f"\nAvtomobilning narhi: {self.price}"
                f"\nAvtomobilning brendi: {self.brand}"
                f"\nAvtomobilning ishlab chiqariilgan joyi: {self.made_in}"
                f"\nAvtomobilning yurgan km: {self.km}")
    
    def update_km(self,km):
        """Avtomobile ga km qo'shish\n Eslatma! siz kmdan km ayira olmaysiz."""
        if km>0:
            self.km += km
        else:
            return f"Siz km dan {km} ni ayira olmaysiz."


mashina1 = Avto("Palaside","white",35_000,"Hyundai","South Korea")
mashina2 = Avto("Kia 8","Black",30_000,"Kia","South Korea")
mashina3 = Avto("Malibu","white",33_000,"Chevrolet","Uzbekistan")
mashina4 = Avto("Gentra","Gray",18_000,"Chevrolet","Uzbekistan")
# mashina1.update_km(1000)
# mashina2.update_km(500)
# mashina3.update_km(400)
# mashina4.update_km(1100)
print(mashina4.get_info())


































