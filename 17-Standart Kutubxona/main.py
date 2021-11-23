# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 09:16:57 2021

@author: Zokirkhon
Topic: Songi so'z
"""

import datetime as dt

# ### datetime
# hozir = dt.datetime.now()
# print(hozir)
# ### Sanani ajratib olish
# print(hozir.date())
# ### vaqtni ajratib olish
# print(hozir.time())
# ### soatni ajratib olish
# print(hozir.hour)
# ### minutni ajratib olish
# print(hozir.minute)
# ### sekundni ajratib olish
# print(hozir.second)




# ### date()
# bugun = dt.date.today()
# print(f"Bugungi sana: {bugun}")
# ertaga = dt.date(2021,11,22)
# print(f"Ertangi sana: {ertaga}")




### time()
# hozir = dt.datetime.now();
# vaqtHozir = hozir.time()
# print(f"Hozir soat: {vaqtHozir}")
# vaqtKeyin = dt.time(22,45,30)
# print(vaqtKeyin)






### Sanalar orasidagi farq
# bugun = dt.date.today()
# ramazon = dt.date(2022,3,31)
# farq = ramazon - bugun
# print(farq)
# print(f"Ramazonga {farq.days} kun qoldi")






### Soatlar orasidagi farq
# hozir = dt.datetime.now();
# lesson = dt.datetime(2021,11,25,13,20,00)
# farq = lesson - hozir;
# sekundlar = farq.seconds;
# minutlar = int(sekundlar/60)
# soatlar = int(minutlar/60)
# print(sekundlar)
# print(minutlar)
# print(soatlar)
# print(f"Dars boshlanishiga {farq.days} kunu {soatlar} soat qoldi")



import math


# PI = math.pi
# print(f"PI ning qiymati: {PI}")
# E = math.e
# print(f"E ning qiymati: {E}")



# # trigonometriya
# math.sin(math.pi/2)
# math.cos(0)
# math.tan(math.pi)

# # Radianlar va burchaklar o'rtasida konvervatsiya
# print(math.degrees(math.pi/2))
# print(math.radians(90))



from pprint import pprint
import json
import pip._vendor.requests as requests

# fileName = "bemor.json"
# with open(fileName, "r") as file:
#     data = json.load(file)
# print(data)
# pprint(data)

r = requests.get("https://api.github.com/users/Zokirkhon1002")
pprint(r.json())









































