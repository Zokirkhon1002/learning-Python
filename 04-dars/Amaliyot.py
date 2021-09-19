# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 17:03:20 2021

@author: Zokirkhon
"""

# Amaliyot
# Uyga vazifa





# # 1
# son = float(input("Iltimos juft son kiriting\n>>> "))
# print("Rahmat") if (son%2==0) else print("Bu juft son emas")




# # 2
# yosh = int(input("yoshingizni kiriting\n>>> "))
# if yosh<=4 or yosh>=60:
#     narh = 'bepul'
# elif yosh<=18:
#     narh = '10 000 so\'m bo\'ladi.'
# elif yosh>18:
#     narh = '20 000 so\'m bo\'ladi.'
# print(f"sizga kirish {narh}")



# # 3
# print("2ta son kiriting")
# s = []
# for i in range(2):
#     s.append(int(input(f"{i+1}-sonni kiriting\n>>> ")))
# if s[0] == s[1]:
#     print("kiritilgan ikki son teng ekan")
# if s[0] != s[1]:
#     print("kiritilgan ikki son teng emas ekan")
# if s[0] > s[1]:
#     print(f"{s[1]} sondan bu {s[0]} soni katta")
# if s[0] < s[1]:
#     print(f"{s[0]} sondan bu {s[1]} soni katta")





# # 4
# langs = ['html', 'css', 'javascript', 'python', 'java', 'c#', 'golang', 
#          'kotlin', 'c++', 'c', 'php']

# likedLangs = []
# bor_kurs = []
# yoq_kurs = []

# print("yaxshi ko'rgan 5ta dasturlash tilini kiriting")
# for n in range(5):
#     likedLangs.append(input(f"{n+1}-dasturlash tilini kiriting\n>>> ").lower())


# for lang in likedLangs:
#     if lang in langs:
#         bor_kurs.append(lang)
#     else:
#         yoq_kurs.append(lang)


# if bor_kurs:
#     print(f"O'quv markazimizda quyidagi dasturlash tillilari mavjud:😊\n")
#     for lang in bor_kurs:
#         print(lang)
#     print("Va istagan paytingiz boshlashingiz mumkin:)")
# else:
#     print("Siz yaxshi ko'rgan barcha dasturlash tillari,\nbizning O'quv markazimizda yo'q ekan. Ming bor uzr😔\n")


# if yoq_kurs:
#     print(f"O'quv markazimizda quyidagi dasturlash tillilari yo'q:😔\n")
#     for lang in yoq_kurs:
#         print(lang)
# else:
#     print("Siz yaxshi ko'rgan barcha dasturlash tillari,\nbizning O'quv markazimizda bor ekan.😊")







# # 5
# users = ['zokirkhon', "sayfulloxon", 'boburmirzo', 'abdulmalik', 'abdulaziz']

# newUser = input("Yangi login kiriting\n>>> ").lower()

# if newUser in users:
#     print("Uzur, bu nom bilan boshqa foydalanuvchi bor")
#     newLogin = input(f"iltimos yangi nom kiriting\n>>> ")
#     if newLogin in users:
#         print("Uzur, bu nom bilan boshqa foydalanuvchi bor")
#     else:
#         print(f"Xush kelibsiz, {newLogin.title()}")
# else:
#     print(f"Xush kelibsiz, {newUser.title()}")








# # 6
son = int(input("Butun son kiriting\n>>> "))
for n in range(2,11):
    if not son%n: print(f"kiritilgan {son} soni, {n} soniga qoldiqsiz bo'linadi")

























    
    
    
    
    
    
    
    
    
    
    
    
    