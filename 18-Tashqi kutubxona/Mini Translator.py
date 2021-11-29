# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 01:30:36 2021

@author: Zokirkhon
topic: mini project
"""
# pip install googletrans==3.1.0a0
# please write above sentence in command Promt(cmd)

from googletrans import Translator
google = Translator();

msg = "please enter a sentence in order to translate. (to exit write: \"q\")"

while True:
    text = input(msg+"\n>>> ")
    if text.lower() == 'q':
        break;
    else:
        translateToUz = google.translate(text, dest='uz')
        translateToKo = google.translate(text, dest='ko')
        translateToEn = google.translate(text, dest='en')
        print(f"Uzbek: {translateToUz.text}\n")
        print(f"Korean: {translateToKo.text}\n")
        print(f"English: {translateToEn.text}")


        