# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 05:13:25 2021

@author: Zokirkhon
Topic: how to test classes
"""



class Car:
    """(self,make,model,year,km=0,price=None)"""
    def __init__(self,make,model,year,km=0,price=None):
        self.make = make
        self.model = model
        self.year = year
        self.__km = km
        self.price = price
    
    def set_price(self,price):
        self.price = price
    
    def add_km(self,km):
        """Mashinaning km ga yana km qo'shish"""
        if km>=0:
            self.__km += km
        else:
            raise ValueError("km can't be negative")
    
    def get_info(self):
        info = f"{self.make.upper()} {self.model.title()} {self.year}-yil {self.__km}km yurgan"
        if self.price:
            info += f" Narhi: {self.price}"
        return info;
    
    def get_km(self):
        return self.__km;