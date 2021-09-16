# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 08:55:46 2021

@author: Zokirkhon
"""

# Tartiblash

# cars = ['bmw', 'mercedes ebnz', 'volvo', 'general motors', 'toyota', 'chevrolet', 'audi']
# cars.sort()
# print(cars)

# Katta va kichik harflar bilan farqli bo'ladi

# cars = ['Bmw', 'mercedes ebnz', 'volvo', 'General motors', 'toyota', 'chevrolet', 'audi']
# cars.sort()
# print(cars)



# teskari tartib

# cars = ['bmw', 'mercedes ebnz', 'volvo', 'general motors', 'toyota', 'chevrolet', 'audi']
# cars.sort(reverse=True)
# print(cars)



# asl o'zgaruvchisini o'zgartirmasdan tartiblash

# cars = ['bmw', 'mercedes ebnz', 'volvo', 'general motors', 'toyota', 'chevrolet', 'audi']
# print(sorted(cars))
# print(cars)



# sorted() methodi
# asl o'zgaruvchisini o'zgartirmasdan teskari tartiblash

# cars = ['bmw', 'mercedes ebnz', 'volvo', 'general motors', 'toyota', 'chevrolet', 'audi']
# print(sorted(cars, reverse=True))
# print(cars)


# sonlar bilan ham 

# ages = [12, 98, 34, 65, 34,76, 11]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))


#Ro'yxatni ortidan boshlab chiqarish

# mevalar = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
# mevalar.reverse()
# print(mevalar)

#Ro'yxat uzunligini chiqarish

# print(f"Elementlar soni: {len(mevalar)}")



# #range() va list() orqali yangi list yozish mumkin

# sonlar = list(range(0,10))
# print(sonlar)


# # range() va qadam, ya'ni (even va odd)

# juftSonlar = list(range(0,21,2))
# toqSonlar = list(range(1,20,2))
# print(F"juft sonlar ro'yxati: {juftSonlar}")
# print(F"juft sonlar ro'yxati: {toqSonlar}")


# # max() min() sum() methodlari

# narhlar  = [12_000, 22_500, 9_800, 5_600, 9_934, 32_874]
# arzon_narh = min(narhlar)
# qimmat_narh = max(narhlar)
# jami = sum(narhlar)
# print(f"Eng arzon narh: {arzon_narh}.\nEng qimmat narh: {qimmat_narh}.\nJami: {jami}" )



# # Ro'yxatni kesish

# cars = ['bmw', 'mercedes ebnz', 'volvo', 'general motors', 'toyota', 'chevrolet', 'audi']
# my_cars = cars[0:3]
# print(my_cars)
# my_cars = cars[2:5]
# print(my_cars)
# my_cars = cars[:5]
# print(my_cars)
# my_cars = cars[3:]
# print(my_cars)




# Ro'yxatdan nusxa olish

# cars = ['bmw', 'mercedes ebnz', 'volvo', 'general motors', 'toyota', 'chevrolet', 'audi']
# myCars = cars[:]
# myCars.append("Tesla")
# myCars.append("Hyundai")
# myCars.remove("volvo")
# del myCars[4]
# print(f"bu birinchi cars ro'yxati: {cars}")
# print(f"bu ikkichi myCars ro'yxati: {myCars}")





# TUPLES o'zgarmas listga o'xshash

# toys = ('bus', 'car', 'bear', 'snake', 'lizard')
# print(toys)
# print(type(toys))


# tuple turdagilarni (list) turdagi method lar bilan o'zgartirish yoki
# o'chirib bo'lmaydi
# lekin bir yo'li bor uni listga ugurub keyin yana qaytarish:
    
    
    
# toys = list(toys)
# print(toys)
# print(type(toys))
# toys.append("Teddy")
# toys.remove("bus")
# del toys[0]
# print(toys)
# print(type(toys))


# toys = tuple(toys)
# print(toys)
# print(type(toys))







# UYGA VAZIFA AMALIYOT

# some countries that I know
# knownCountries = ["Uzbekistan", "Turkey", "Malasia", "Indonesia", "South Korea", "Japan"]
# print(knownCountries)
# print(len(knownCountries))
# print(sorted(knownCountries))
# print(sorted(knownCountries,reverse=True))
# print(knownCountries)
# knownCountries.reverse()
# print(knownCountries)
# knownCountries.sort()
# print(knownCountries)
# knownCountries.sort(reverse=True)
# print(knownCountries)




# juft_sonlar = list(range(120,1200,2))
# print(juft_sonlar)
# print(f"umumiy yig'indi: {sum(juft_sonlar)}")
# katta = max(juft_sonlar)
# kichik = min(juft_sonlar)
# ayirma = katta - kichik
# print(f"max - min = {ayirma}")
# print(f"ro'yxatdagi elementlar soni: {len(juft_sonlar)}")
# print(f"boshidan 20ta sonlar: {juft_sonlar[:21]}")
# print(f"o'rtasidan 20ta sonlar: {juft_sonlar[260:281]}")
# print(f"oxiridan 20ta sonlar: {juft_sonlar[519:]}")


taomlar = ['Shashlik', 'Palov', 'Somsa', 'Manti', 'Chuchvara', 'Qotirma', 'Mastava']
nonushta = taomlar[:]
nonushta.remove('Somsa');
nonushta.remove('Manti');
nonushta.remove('Chuchvara');
del nonushta[2]
nonushta.append('issiq non va qaymoq')
nonushta.insert(4,'mevalar')
print(taomlar)
print(nonushta)
nonushta = tuple(nonushta)
print(nonushta)

