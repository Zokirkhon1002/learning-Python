# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 06:21:14 2021

@author: Zokirkhon
"""

# ism = "Zokirkhon \n";

# shahar = "Qo'qon\n";
# viloyat = "Farg'ona";

# print(ism,  shahar, viloyat)


# matn = "men yangi 😃😜 likni ko\'chirib oldim"
# smayl = "😜"
# print(matn)
# print(smayl)


# ism = 'Zokirkhon';
# familya = 'Kotibkhonov';
# ism_familya = f"Mening ismim: {ism}, familyam: {familya}";


# print('Mening ismim: ' + ism);
# print(familya + " " + ism);
# print(ism_familya)


# print("Salom Dunyo!")
# print("Salom \tDunyo!")
# print("Salom \nDunyo!")


# familya = familya.upper();
# print('Mening ismim: ' + ism.title());
# print(familya.lower() + " " + ism.lower());
# print(ism_familya.upper())
# print(ism_familya.capitalize())

# meva = '     apricot      '
# print("Men " + meva.lstrip() + "ni yaxshi ko'raman")
# print("Men " + meva.rstrip() + "ni yaxshi ko'raman")
# print("Men " + meva.strip() + "ni yaxshi ko'raman")
# print("Men " + meva + "ni yaxshi ko'raman")


# INPUTS

# Fname = input("Ismingizni kiriting iltimos\n>>>");
# print("Assalomu alaykum, " + Fname)


# Fname = input("Ismingiz nima?\n>>>") # foydalanuvchi ismini yangi
# print("Assalomu alaykum, " + Fname.title())







# barcha turdagi string methodlar

# print(ism.upper())
# print(ism.lower())
# print(ism.casefold())
# print(ism.center(20))
# print(ism.count('o')) # 1ta argument qabul qiladi,
# va uni textni ichida necha marotaba foydalanilganini
# sonini qaytaradi.
# print(ism.encode()) #The encode() method encodes 
#the string, using the specified encoding.
# If no encoding is specified, UTF-8 will be used.
# print(ism.endswith('n')) # The endswith() method returns 
# True if the string ends with the specified value,
# otherwise False.
#Syntax
#string.endswith(value, start, end)

# txt = "H\te\tl\tl\to"

# print(txt)
# print(txt.expandtabs())
# print(txt.expandtabs(2))
# print(txt.expandtabs(4))
# print(txt.expandtabs(10))
# txt = "Hello, welcome to my world."

# x = txt.find("welcome")
# print(x)
# txt = "For only {price:.2f} dollars!";
# print(txt.format(price = 50))

#shu yergacha ba'zilarini yozdik, qolganini o'qib o'tib ketdik
# amaliyotda inshaalloh sinaymiz





#uyga vazifa
kocha = 'Bog\'bon';
mahalla = 'Sog\'bon';
tuman = 'Bodomzor';
viloyat = 'Samarqand';
natija = f"{kocha.lower()} ko\'chasi, \n{mahalla.upper()} mahallasi, \n{tuman.capitalize()} tumani, \n{viloyat.title()} viloyati\n\n\n";

# kocha = input("Ko'changiz nomi?\n>>>")
# mahalla = input("Mahallangiz nomi?\n>>>")
# tuman = input("Tumaningiz nomi?\n>>>")
# viloyat = input("Viloyatingiz nomi?\n>>>")
# with_user_value = f"{kocha} ko\'chasi, \n{mahalla} mahallasi, \n{tuman} , \n{viloyat} viloyati";

print(natija)
# print(with_user_value)






