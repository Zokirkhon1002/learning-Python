# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 22:01:59 2021

@author: Zokirkhon
"""

class Shaxs():
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familya,passport,tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familya = familya
        self.passport = passport
        self.tyil = tyil
    def get_info(self):
        """Shaxs haqida ma'lumot qaytaradi."""
        info = f"{self.ism} {self.familya}. "
        info += f"Passport: {self.passport}, {self.tyil}-yilda tug'ilgan"
        return info;
    def get_age(self,hozirgi_yil):
        """Shaxsning yoshini qaytaruvchi method."""
        return hozirgi_yil - self.tyil

###super class1
class Talaba(Shaxs):
    """Talaba klasi"""
    def __init__(self,ism,familya,passport,tyil,idraqam,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism,familya,passport,tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
    
    def get_id(self):
        return self.idraqam
    def get_bosqich(self):
        return self.bosqich
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familya}. "
        info += f"\n{self.get_bosqich()}-bosqich. ID raqam: {self.get_id()}"
        info += f"\nManzil: {self.manzil}."
        return info;

class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
        
    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyat, {self.tuman}, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil


talaba1_manzil =Manzil(17,"Soli Adashev","Namangan Shahar","Namangan").get_manzil()
talaba1 = Talaba("Zokirkhon","Kotibkhonov","ff112233",1999,180421,talaba1_manzil)


print(talaba1.get_info())