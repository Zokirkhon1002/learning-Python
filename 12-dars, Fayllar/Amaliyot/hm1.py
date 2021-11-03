# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 23:25:28 2021

@author: Zokirkhon
HomeWork
"""


###1
# learned = "Bugun faylar bilan ishlashni o'rgandik.\n"
# with open("learned.txt","w") as fayl:
#     fayl.write(learned)
    




###2
# file = "learned.txt"
# with open(file) as faylN:
#     text = faylN.readlines()
# text = [txt.rstrip() for txt in text]
# print(text)






###3
# import pickle
# file_name = "pi_m.txt"
# with open(file_name) as file:
#     pi = file.read()
# pi = pi.rstrip()
# pi = pi.replace("\n","")
# pi = pi.replace(" ","")
# # print(pi)

# birth_date = '15011999'
# print(birth_date in pi)


# pi = float(pi)
# print(pi)


# newFile = "pi_float.pickle"
# with open(newFile,'wb') as fayl:
#     pickle.dump(pi,fayl)









###4

while True:
    book = input("Eslatma! To'xtash uchun Enter tugmasini bosing.\nYaxshi ko'rgan kitobingizni kiritng: ")
    if not book: break;
    with open("f_books.txt","a") as fayl:
        text = input("")
        fayl.write(book+'\n')

























