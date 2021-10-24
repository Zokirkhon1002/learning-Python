# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 17:00:45 2021

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
        self.fanlar = []
        self.fanlar_soni = 0
    
    def get_id(self):
        return self.idraqam
    def get_bosqich(self):
        return self.bosqich
    
    
    def fanga_yozil(self,yozilgan_fanlar):
        self.fanlar.append(yozilgan_fanlar)
        self.fanlar_soni += 1
    
    def remove_fan(self,removingFan):
        if removingFan in self.fanlar:
            self.fanlar.remove(removingFan)
            self.fanlar_soni -= 1
        else:
            return f"Uzr siz {removingFan} ga yozilmagansiz"
    
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familya}. "
        info += f"\n{self.get_bosqich()}-bosqich. ID raqam: {self.get_id()}"
        info += f"\nManzil: {self.manzil}."
        info += f"\nFanlar: {self.fanlar}"
        # info += f"\nFanlar: {[x.get_fanlar() for x in self.fanlar]}"
        info += f"\nFanlar soni: {self.fanlar_soni}"
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

class Fan:
    """Fan klasi"""
    def __init__(self,nomi,davomiyligi,darsSoati,add):
        """Fan haqidagi ma'lumotni to'ldiring"""
        self.nomi = nomi
        self.davomiyligi = davomiyligi
        self.darsSoati = darsSoati
        self.add = add
    def get_fan(self):
        """Fanni ko'rish"""
        fan = f"Fan nomi: {self.nomi}, \ndavomiyligi: {self.davomiyligi}, "
        fan += f"\ndars-soati: {self.darsSoati},"
        fan += f"\nqo'shimcha texnologiyalar: {self.add}"
        return fan;

Frontend = Fan("html,css,javaScript,bootstrap,sass,reactJS","6-oy","har kuni 5-soat","Git,Netlify,vsCode,replyIt")
Backend = Fan("javaScript,nodeJS,mongodb","6-oy","har kuni 5-soat","Git,Heroku,Netlify,vsCode")
Python = Fan("Python,django,nampy","6-oy","har kuni 5-soat","Git,Heroku,,Anaconda,Pycharm")

# print(Frontend.get_fan())


talaba1_manzil =Manzil(17,"Soli Adashev","Namangan Shahar","Namangan").get_manzil()
talaba1 = Talaba("Zokirkhon","Kotibkhonov","ff112233",1999,180421,talaba1_manzil)

talaba1.fanga_yozil(Frontend)
talaba1.fanga_yozil(Backend)
talaba1.fanga_yozil(Python)

talaba1.remove_fan(Python)

print(talaba1.get_info())