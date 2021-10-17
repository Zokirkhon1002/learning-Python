# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 02:11:32 2021

@author: Zokirkhon

Telegrambot: to latin and to Cyrillic
token: 2086228212:AAF73VCedEyCqTA_S7iwZ8n5HFmwVvTLQL8
"""
import telebot
from lugat import to_cyrillic as t_c, to_latin as t_l;


TOKEN = "2086228212:AAF73VCedEyCqTA_S7iwZ8n5HFmwVvTLQL8";
bot = telebot.TeleBot(TOKEN, parse_mode=None);



@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alaykum, Xush kelibsiz!"
    javob += "\nBu botning vazifasi: "
    javob += "kiril harflarini lotinga yoki lotin harflarini kirilga ugurib berishdan iborat."
    bot.reply_to(message, javob)


def lugat(javob):
    if javob.isascii():
        javob = t_c(javob)
    else:
        javob = t_l(javob)
    return javob


@bot.message_handler(func=lambda message: True)
def echo_all(msg):
    bot.reply_to(msg, lugat(msg.text))


bot.infinity_polling()



