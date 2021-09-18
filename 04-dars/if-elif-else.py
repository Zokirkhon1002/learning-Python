# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 10:22:18 2021

@author: Zokirkhon
"""

# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai', 'toyoto']

# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())


# ism = "Ali"

# print(ism.lower() == 'ali')


# ism = input("Ismingiz nima? \n>>> ")
# if ism.lower() != 'zokirkhon':
#     print(f"Uzr, {ism.title()} biz Zokirkhonni kutyapmiz.")
# else:
#     print(f"Salom {ism.title()}")



# javob = float(input("12x6 nechchiga teng?\n>>> "))
# if javob != 72:
#     print("Javob xato!")


# yosh = int(input("yoshingiz nechchida?\n>>> "))
# if yosh >= 18:
#     print("Xush kelibsiz!")
# else:
#     print("Kirish mumkin emas!")



# login = input("Yangi login tanlang:\n>>> ")
# if len(login) <= 5:
#     print("login 5 harfdan ko'proq bo'lishi shart!")


from datetime import date
todays_date = date.today()

yearNow = todays_date.year
monthNow = todays_date.month
dayNow = todays_date.day


# yil = int(input("Tug'ilgan yilingizni kiriting iltimos\n>>> "))
# if yearNow-yil<18:
#     print(f"yoshingiz {yearNow-yil}da ekan.")
#     print("Kirish mumkin emas!")
# else:
#     print("Xush kelibsiz!")



# yosh = int(input("Yoshingiz nechchida?\n>>> "))
# if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")



# x, y = 70, 50
# print("x katta y dan") if x>y else print("y katta x dan")




#Amaliyot qismi
#Uyga Vazifa


# #1
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())


# #2
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())



# #3
# name = input("Iltimos, ismingizni kiriting\n>>> ");
# if name.lower() == 'admin':
#     print(f"Xush kelibsiz, {name.title()}. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {name.title()}.")




# #4
# print("Foydalanuvchi iltimos 2ta son kiriting:")
# x = int(input("1-sonni kiriting\n>>> "))
# y = int(input("2-sonni kiriting\n>>> "))
# if x==y: print(f"siz kiritgan sonlar teng ekan. {x}=={y}")



# #5
# x = int(input("Iltimos biror son kiriting\n>>> "))
# if x<0:
#     print(f"siz kiritgan {x} Manfiy son ekan")
# else:
#     print(f"siz kiritgan {x} Musbat son ekan")


import math


# #6
# x = float(input("Iltimos biror son kiriting\n>>> "))
# if x>=0:
#     print(f"siz kiritgan sonning ildizi: {math.sqrt(x)}")
# else:
#     print("Iltimos Musbat son kiriting.")











