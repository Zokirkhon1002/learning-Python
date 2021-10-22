# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 23:48:34 2021

@author: Zokirkhon
"""

class Talaba:
    def __init__(self,ism,familya,tyil):
        self.ism = ism
        self.familya = familya
        self.tyil = tyil
        self.bosqich = 1
    
    
    def tanishtir(self):
        """Talabaning ism-familiyasini va tug'ilgan yilini qaytaradi."""
        return f"Ismim: {self.ism}. Familyam: {self.familya}. Tug'ilgan yilim: {self.tyil}.  {self.bosqich}-bosqich talabi"
    
    def get_age(self,hozirgiYil):
        """Talabaning ismini qaytaradi"""
        return hozirgiYil - self.tyil;
    
    def last_name(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familya
    
    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familya}"
    
    def get_name(self):
        return self.ism
    
    def get_bosqich(self):
        return self.bosqich
    
    def set_bosqich(self, yangi_bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = yangi_bosqich
    
    def update_bosqich(self):
        """Talabaning bosqichini bittaga ko'paytirish"""
        self.bosqich += 1
    
    """
    pass OPERATORI
    Pythonda hech qanday vazifani bajarmaydigan pass operatori mavjud. 
    Bu operatordan bo'sh metodlar yaratishda foydalanish mumkin. 
    Misol uchun siz klassingiz uchun muhim metodlarni bilasiz, 
    lekin metod badani hali tayyor emas. 
    Agar metod badanini bo'sh qoldirsangiz, 
    Python IndentationError xatosini qaytaradi. 
    Shunday xolatlarda, 
    funksiya badaniga pass operatorini qo'yib ketishimiz mumkin:
    
    """
    
    def describe():
        pass
    
    def get_email():
        pass
    """
    Yuqoridagi klassimizda describe() va get_email() funksiyalar 
    badani hali tayyor emas, bo'shliqni to'ldirish 
    uchun esa pass operatoridan foydalanganmiz.
    
    pass operatoridan if-else, for, 
    while operatorlari badanida ham foydalanish mumkin.
    """


talaba1 = Talaba("Zokirkhon","Kotibkhonov",1999)
talaba2 = Talaba("Sayfullokhon","Ulukhodjaev",2000)
talaba3 = Talaba("Khurshidbek","Alisherov",2001)

# print(talaba1.get_name())
# print(talaba1.get_age(2021))
# print(talaba1.last_name())
# talaba1.set_bosqich(2) # 2 bosqich bo'ldi
# talaba1.update_bosqich() # 3 bosqich bo'ldi
# print(talaba1.tanishtir())


class Club():
    """Klub uchun klass"""
    
    def __init__(self,name):
        self.name = name
        self.talabalar_soni = 0
        self.talabalar = []
    
    def add_student(self,talaba):
        """Klubga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
    
    def get_students(self):
        """Klub ga yozilgan talabalar haqida ma'lumot"""
        return [x.tanishtir() for x in self.talabalar]
    
    def get_students_num(self):
        """Klubga yozilgan talabalar soni"""
        return self.talabalar_soni


klub1 = Club("Aikido");
print(klub1.__dict__)
print(klub1.__dict__.keys())
# print(dir(Club))
# print(dir(Talaba))







# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False ]
    # list_method = []
    # for method in dir(klass):
    #     if not method.startswith("__"):
    #         list_method.append(method)
    

    # for each in list_method:
    #     print(each)
    
    
    # return list_method


# print(see_methods(Talaba))
    












































