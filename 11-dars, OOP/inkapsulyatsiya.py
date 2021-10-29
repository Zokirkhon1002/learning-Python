# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 00:31:32 2021

@author: Zokirkhon
"""
from uuid import uuid4

class Avto:
    """Avtomobil klasi"""
    __num_avto = 0
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1
        
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
    def get_km(self):
        """Km ni qaytarish"""
        return self.__km
    def get_id(self):
        return self.__id
    def add_km(self,km):
        """Mashinaning km ga yana km qo'shish"""
        if km >= 0:
            self.__km += km
        else:
            print("Mashina km kamaytirib bo'lmaydi")

avto1 = Avto("GM","Malibu","Qora",2020,40_000,1000)
avto2 = Avto("GM","Gentra","Oq",2020,15_000,100)
avto3 = Avto("Hyundai","Palaside","Oq",2021,40_000,100)
