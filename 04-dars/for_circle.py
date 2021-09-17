# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 12:08:46 2021

@author: Zokirkhon
"""



# mehmonlar = ['Sayfulloxon', 'Zokirkhon', 'Abdulhamid', 'Murodillo', 'Boburmirzo']

# for i in mehmonlar:
#     print("Assalomu alaykum", i)


# for mehmon in mehmonlar:
    # print(f"Hurmatli {mehmon}, sizni 20-sentyabr kuni nahorga oshga taklif qilamiz")
    # print("Hurmat bilan, Palonchiyevlar oilasi\n")


# sonlar bilan ham ishlab ko'ramiz
# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")




# circle orqali ro'yxatni sonlar bilan to'ldiramiz
# sonlar = list(range(11)) 
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)

# print(sonlar)
# print(sonlar_kvadrati)

# friends = []
# print("5 ta eng yaqin do'stingiz kim?:")
# for friend in range(5):
#     friends.append(input(f"{friend+1} do'stingizni kiriting: \n>>>"))
# print(friends)




#  Amaliyot # uyga vazifa

# ismlar_royxati = ['Sayfulloxon', 'Zokirkhon', 'Abdulhamid', 'Murodillo', 'Boburmirzo']
# n = 0
# for each in ismlar_royxati:
#     print(f"Salom do'stim {each}, Qandaysiz?")
#     n +=1
# print(f"kod {n} marotaba takrorlandi")


# toqSonlar = list(range(11,100,2))
# for kub in toqSonlar:
#     print(f"{kub} sonining kubi {kub**3} ga teng")
    
# print(toqSonlar)



# SevimliKinolar = []
# print("Sevimli kinolaringizdan 5 donasini kiriting iltimos")
# for each in range(5):
#     SevimliKinolar.append(input(f"{each+1}-kinoning nomi nima?\n>>>"))

# print(f"Sizning sevimli kinolaringiz ro'yxati\nbu yerda: {SevimliKinolar}")


number = int(input("Bugun nechta odam bilan ko\'rishdingiz?\n>>>"))
u_odamlar = []
n = 0;
for each in range(number):
    n+=1
    u_odamlar.append(input(f"{n}-odamning ismini kiriting iltimos\n>>>"))
print(f'siz ko\'rishgan odamlar soni: {n}ta \nva ularning ismlari: {u_odamlar}')









