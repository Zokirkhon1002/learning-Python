# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 11:33:02 2021

@author: Zokirkhon
topic: Mini Project2
"""

import requests
import googletrans

url = "https://api.adviceslip.com/advice"
r = requests.get(url)
advice = r.json()['slip']['advice']


translator = googletrans.Translator()
tarjima = translator.translate(advice, dest='uz')
print(tarjima.origin)
print(tarjima.text)
