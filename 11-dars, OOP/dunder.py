# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 00:31:32 2021

@author: Zokirkhon
"""
from uuid import uuid4


class Avto:
    """Avtomobil klasi"""
    __num_avto = 0

    def __init__(self, make, model, rang, yil, narh, km=0):
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

    def add_km(self, km):
        """Mashinaning km ga yana km qo'shish"""
        if km >= 0:
            self.__km += km
        else:
            print("Mashina km kamaytirib bo'lmaydi")

    def __str__(self):
        return f"Avto: {self.make} {self.model} {self.rang} {self.yil} {self.narh} {self.__km}"

    def __repr__(self):
        """ Shunisi ko'proq tavsiya qilinadi"""
        return f"Avto: {self.make} {self.model} {self.rang} {self.yil} {self.narh} {self.__km}"

    def __eq__(self, y):
        return self.narh == y.narh

    def __lt__(self, y):
        return self.narh < y.narh

    def __le__(self, y):
        return self.narh <= y.narh


# print(avto1)
# print(avto1 == avto2)
# print(avto1 == avto3)
# print(avto1 < avto2)
# print(avto1 > avto2)
# print(avto1 <= avto2)
# print(avto1 >= avto2)


class AvtoSalon:
    """Avtosalon klassi"""

    def __init__(self, name):
        self.name = name
        self.avto_list = []

    def __repr__(self):
        return f"Avto salon: {self.name}"

    def __getitem__(self, index):
        return self.avto_list[index]

    def __setitem__(self, index, value):
        self.avto_list[index] = value

    def __call__(self,*value):
        if value:
            for i in value:
                self.avto_list.append(i);
        else:
            return [i for i in self.avto_list]
    
    def __add__(self,y):
        if isinstance(y,AvtoSalon):
            yangiSalon = AvtoSalon(f"{self.name} {y.name}")
            yangiSalon.avto_list = self.avto_list + y.avto_list;
            return yangiSalon;
        elif isinstance(y,Avto):
            self.add_avto(y)

    def add_avto(self, *avto):
        """Avtolar qo'shish"""
        for i in avto:
            if isinstance(i, Avto):
                self.avto_list.append(i)
            else:
                print("Avto obyekt kiriting")


salon1 = AvtoSalon("MaxAvto")
avto1 = Avto("GM", "Malibu", "Qora", 2020, 40_000, 1000)
avto2 = Avto("GM", "Gentra", "Oq", 2020, 15_000, 100)
avto3 = Avto("Hyundai", "Palaside", "Oq", 2021, 40_000, 100)
salon1.add_avto(avto1, avto2, avto3)
# print(salon1[0])
# print(salon1[:])
salon1[0] = Avto("BMW", "X5", "white", 2020, 43_000, 0)
# print(avto1)

avto4 = Avto("Kia", "kia 5", "white", 2021, 32_000, 100)
# print(salon1(avto4))

salon2 = AvtoSalon("Avto Lider")
salon2.add_avto(avto1, avto2, avto3)




































