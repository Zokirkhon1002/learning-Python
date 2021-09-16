# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 06:42:04 2021

@author: Zokirkhon
"""



# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# print(mevalar)

# narhlar = [12000, 18000, 10900, 22000, 25000]
# print(narhlar)

# sonlar = ['bir', 'ikki', 3, 4, 5]
# print(sonlar)

# ismlar = []
# print(ismlar)

# print(f"Binichi meva: {mevalar[0]}")
# print(f"Ikkinchi meva: {mevalar[1]}")
# print(f"Ikkinchi meva: {mevalar[-1]}\n")

# print(f"Birinchi meva: {mevalar[0].title()}")
# print(f"Ikkinchi meva: {mevalar[1].upper()}")
# print(f"Ikkinchi meva: {mevalar[-1].upper()}\n")

# print(narhlar[2] + narhlar[3], "\n")

# car_models = ['Toyota', "GM", "Volvo", "BMW", 'Hyundai', "Kia", "Volkswagen"]
# print(car_models[-1], '\n')

# mevalar[0] = 'anor';
# print(mevalar[0].title(), '\n')

# narhlar[3] = narhlar[3]+2000
# print(narhlar[3])


# .append() -ro'yxatning oxiriga element qo'shish
# Fruits = ['olma', 'anjir', 'shaftoli', "o'rik"]
# Fruits.append("tarvuz")
# print('\n', Fruits)

# cars = []
# cars.append("Lacetti")
# cars.append("Nexia 3")
# cars.append("Cobalt")
# print(cars)

# .insert() -ro'yxatning boshiga element qo'shish
# hozircha 2ta argument qabul qiladi, 
# 1-si indeksi
# # 20-si qo'shiladigan element
# mashinalar = []
# mashinalar.insert(2, "Lacetti")
# mashinalar.insert(0, "Nexia 3")
# mashinalar.insert(1, "Cobalt")
# mashinalar.insert(3, "Malibu")
# print(mashinalar)
# del  -> indeks yordamida elementni o'chirish


# del mashinalar[2];
# print(mashinalar)
# mashinalar.insert(0, "Lacetti")
# print(mashinalar)

# .remove() -> esa elementni nomi yordamida
# mashinalar.remove("Lacetti")
# print(mashinalar)
# mashinalar.insert(1, "Malibu")
# print(mashinalar)

#agar bizda birxil elementdan bir nechta bo'lsa
# remove va del method lari birinchi elementni o'chiradi
# mashinalar.remove("Malibu")
# print(mashinalar)

# listning ichidan biror elementni sug'urib olish
# .pop() biror elementni sug'urib oladi;
# .pop() ga indeks bermasak, oxiridan sug'urib oladi

# bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"];
# print(bozorlik)
# mahsulot = bozorlik.pop(1)
# print(mahsulot)
# print(bozorlik)
# print("Men " + mahsulot + " sotib oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)

# uyga vazifa

# 1
# friends = ["abdulhamid", "Abdulaziz", "Azamjon", "Boburmirzo"]
# print(friends[0], "how are you?")
# print(friends[-3], "I miss you my friend")
# print(friends[2], "how is your family?")
# print(friends[-1], "What have you been upto dately?")
# print(len(friends))

# 2
# nums = [1,2,10,20,13,66,77,112,-14,-5, 15.0]
# print(len(nums))
# nums[1] = 6;
# print(nums[1])
# print(nums[0]+nums[-4])
# print(nums[1]+nums[-9])
# print(nums[2]+nums[4])
# print(nums[7]-nums[4])
# print(nums[3]+nums[10])
# print(nums[6]/nums[3])
# print(nums[5]+nums[-1])
# print(nums[4]*nums[1])
# print(nums[1]**nums[3])
# print(nums[7]/nums[0])




# 3

# t_shaxslar = ["Alisher Navoiy", "Imom Buxoriy", "Shayx Muhammad Sodiq Muhammad Yusuf", "Jaloliddin Rumiy", "Yunus Emro", "Salohiddin Ayyubiy", "Amir Temur", "Bahouddin Naqshbandiy"]
# print(len(t_shaxslar))
# SalohiddinAyyubiy = t_shaxslar.pop(-3)
# AmirTemur = t_shaxslar.pop(-2)
# BahouddinNaqshBandiy = t_shaxslar.pop(-1)
# YunusEmro = t_shaxslar.pop(4)
# JaloliddinRumiy = t_shaxslar.pop(3)
# Hazrat = t_shaxslar.pop(2)
# ImomBuxoriy = t_shaxslar.pop(1)
# AlisherNavoiy = t_shaxslar.pop(0)


# z_shaxslar = ["Anvar aka Ustoz", "Abror Muxtor Aliy", "Muhammadali aka", "Temur aka", "Umid aka", "Saidbek aka", "Ulug'bek aka", "Murod aka"]
# print(len(z_shaxslar))
# UmidjonIshmuhammedov = z_shaxslar.pop(-4)
# SaidbekArslonov = z_shaxslar.pop(-3)
# UlugbekSamigjanov = z_shaxslar.pop(-2)
# MuradBuildings = z_shaxslar.pop(-1)
# TemurAka = z_shaxslar.pop(3)
# MuhammadAliAka = z_shaxslar.pop(2)
# AbrorMuxtorAliy = z_shaxslar.pop(1)
# AnvarAkaUstoz = z_shaxslar.pop(0)



# print(f"Men tarixiy shaxslardan {JaloliddinRumiy} r.alayhi bilan, zamonaviy shaxslardan esa Ustoz {AbrorMuxtorAliy} domla bilan suhbat qilishni istar edim. \n")
# print(f"Men tarixiy shaxslardan {AlisherNavoiy} r.alayhi bilan, zamonaviy shaxslardan esa Ustoz {MuhammadAliAka} bilan suhbat qilishni istar edim. \n")
# print(f"Men tarixiy shaxslardan {ImomBuxoriy} r.alayhi bilan, zamonaviy shaxslardan esa Ustoz {AnvarAkaUstoz} Ustoz bilan suhbat qilishni istar edim. \n")
# print(f"Men tarixiy shaxslardan {Hazrat} r.alayhi bilan, zamonaviy shaxslardan esa Ustoz {TemurAka} bilan suhbat qilishni istar edim. \n")
# print(f"Men tarixiy shaxslardan {BahouddinNaqshBandiy} r.alayhi bilan, zamonaviy shaxslardan esa Ustoz {UmidjonIshmuhammedov} bilan suhbat qilishni istar edim. \n")
# print(f"Men tarixiy shaxslardan {AmirTemur} r.alayhi bilan, zamonaviy shaxslardan esa Ustoz {MuradBuildings} bilan suhbat qilishni istar edim. \n")
# print(f"Men tarixiy shaxslardan {YunusEmro} r.alayhi bilan, zamonaviy shaxslardan esa Ustoz {UlugbekSamigjanov} bilan suhbat qilishni istar edim. \n")
# print(f"Men tarixiy shaxslardan {SalohiddinAyyubiy} r.alayhi bilan, zamonaviy shaxslardan esa Ustoz {SaidbekArslonov} bilan suhbat qilishni istar edim. \n")



# 4
mehmonlar = []
Friends = []
Friends.append("Abdulloh")
Friends.append("Abdulhamid")
Friends.append("Abdulhamid")
Friends.append("Abdulaziz")
Friends.append("Azamjon")
Friends.append("Abdulhamid")
Friends.append("Sayfulloxon")
# print(Friends)
Friends.insert(2, "Zokirkhon")
Friends.remove("Abdulhamid")
# print(Friends)
del Friends[2]
# print(Friends)
mehmonlar.append(Friends.pop(0));
mehmonlar.insert(1, "Zokikhon")
mehmonlar.insert(2, Friends.pop(3))
mehmonlar.insert(3, Friends[2])
del mehmonlar[0]
mehmonlar.remove("Azamjon")
print(mehmonlar)






