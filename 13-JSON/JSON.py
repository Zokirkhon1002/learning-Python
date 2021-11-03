# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 00:15:23 2021

@author: Zokirkhon
theme: JSON
"""

import json
import requests

# x = 10
# x_json = json.dumps(x)


# y = 5.5
# y_json = json.dumps(y)

# m = True
# m_json = json.dumps(m)


# sonlar = (12,45,23,67)
# sonlar_json = json.dumps(sonlar)




# bemor = {
#     "ism": "Alijon Valiyev", 
#     "yosh": 30,
#     "oila": True, 
#     "farzandlar": [
#         "Ahmad", 
#         "Bonu"
#         ],
#     "allergiya": None,
#     "dorilar": [
#         {
#             "nomi": "Analgin",
#             "miqdori": 0.5
#             }, 
#         {
#             "nomi": "Panadol",
#             "miqdori": 1.2
#             }
#         ]
#     }

# bemor_json = json.dumps(bemor, indent = 4)
# print(bemor_json)

# with open('sonlar.json','w')as f:
#     json.dump(sonlar, f)



# bemor2 = json.loads(bemor_json)
# print(bemor2)











###wikipedia api
# wikiapi = "https://uz.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=Alisher%20Navoiy"


name = input("Kim haqida bilmoqchisiz?: ").split()






wikiapi = f"https://uz.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles={name[0].capitalize()}%20{name[1].capitalize()}"
response = requests.get(wikiapi)

AlisherNavoiy = json.dumps(response.json(), indent = 4)

print(AlisherNavoiy)

# print(json.loads(AlisherNavoiy))









### faylardan ochish
# filename = 'bemor.json'
# with open(filename) as f:
#     bemor = json.load(f)
# print(bemor)
# print(type(bemor))




















