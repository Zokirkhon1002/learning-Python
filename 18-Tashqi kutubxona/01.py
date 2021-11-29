# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 00:28:54 2021

@author: Zokirkhon
topic: Tashqi Kutubxona
"""
# # pip install googletrans
# from googletrans import Translator
# tarjimon = Translator();

# matnUz = "\n\nJavaScript va Python dunyodagi eng mashxur dasturlash tillari qatorida\n\n"


# """Istalgan matnni ingliz tiliga 
# tarjimon qilish uchun translate metodini chiqaramiz"""
# tarjima = tarjimon.translate(matnUz)

# # asl matn
# print(tarjima.origin)

# # tarjima
# print(tarjima.text)

# # Boshqa tilga tarjima qilish uchun des parametridan foydalanamiz
# tarjima_ru = tarjimon.translate(matnUz, dest='ru')
# print(tarjima_ru.text)


# # Ingliz tilidan tarjima
# matnEng = tarjima.text
# tarjima_uz = tarjimon.translate(matnUz, dest='uz')
# print(tarjima_uz.text)






###pip install requests
from pprint import pprint
import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from english_words import words
import wx


# sahifa = "https://kun.uz/news.main";
# r = requests.get(sahifa)
# pprint(r.text)





# rescountries API
# country = "uzbekistan"
# url = f"https://restcountries.ue/rest/v2/name/{country}"
# r = requests.get(url)
# r_json = r.json()[0]
# pprint(r_json.keys())
# pprint(r_json['capital'])





# sahifa = "https://kun.uz/news";
# r = requests.get(sahifa)
# # pprint(r.text)


# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
# news = soup.find_all(class_="big-news__title")
# print(news)








# ikki so'z o'rtasidagi o'xshashlik foizini topish
print(fuzz.ratio('salom', 'assalom'))
print(fuzz.ratio('salom', 'salim'))
























