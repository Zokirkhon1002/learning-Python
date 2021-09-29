# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 18:50:49 2021

@author: Zokirkhon
"""

# ism = input("Ismingiz nima?\n>>> ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida?\n>>> "
# yosh = input(savol)
# height = input("Bo'yingiz necha metr?\n>>> ")


# # while
# son = 1
# while son<=5:
#     print(son, end=" ")
#     son+=1
# print("Dastur tugatildi")




# while and input
# print("kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting:\n"
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing:\n>>> "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)

# print("Dastur tugatildi!")







# # ishora
# print("kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting:\n"
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing:\n>>> "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:print(float(qiymat)**2)

# print("Dastur tugatildi!")





# # break while
# print("kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting:\n"
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing:\n>>> "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:print(float(qiymat)**2)

# print("Dastur tugatildi!")





# # break for
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")





# # continue for
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")




# # continue while
# son = 0
# while son<10:
#     son +=1
#     if son%2!=0:
#         continue
#     else:
#         print(son)







# # infinite loop
# son = 0
# while son<10:
#    # # # son +=1 # mana bu yo'qligi uchun abadiy circle bo'lib qoldi
#     if son%2!=0:
#         continue
#     else:
#         print(son)






# # infinite loop
# son = 0
# while son<10:
#     if son%2!=0:
#         continue
#     else:
#         print(son)
#     son +=1 # mana bu yo'qligi uchun abadiy circle bo'lib qoldi








# # infinite loop
# son = 1
# while son>0:
#     son +=1
#     if son%2!=0:
#         continue
#     else:
#         print(son)








# # Amaliyot
# # Uyga vazifa

# # #1
# savol = "Iltimos ismingizni kiriting\n>>> ";
# ism = input(savol)
# liked_books = []
# while True:
#     savol = f"Assalomu alaykum {ism.title()}, yaxshi ko'rgan kitoblaringizni nomini kiriting\n"
#     savol += f"{ism.title()}, Eslatma!  agar stop so'zini yozsangiz, dastur to'xtaydi\n>>> "
#     qiymat = input(savol)
#     if qiymat == "stop":
#         break
#     else:
#         liked_books.append(qiymat)

# print(f"siz yaxshi ko'rgan kitoblar ro'yxati:\n {liked_books}")






# # #2
# ism = input("Iltimos ismingizni kiriting:\n>>> ")
# savol = f"Assalomu alaykum {ism}, Muzeyga xush kelibsiz!\n"
# savol += f"{ism.title()}, Eslatma! exit yoki quit so'zini kiritsangiz dastut to'xtaydi."
# information = {}
# result = ''
# while True:
#     print(savol)
#     qiymat = input(f"{ism.title()}, Iltimos yoshingizni kiriting:\n>>> ")
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     else:
#         qiymat = int(qiymat)
#         if qiymat < 7:
#             result = "siz uchun Muzeyga kirish 2 000 so'm bo'ladi.\n\n"
#         elif qiymat >= 65:
#             result = "siz ga kirish bepul"
#         elif qiymat >= 7 and qiymat < 18:
#             result = "siz uchun Muzeyga kirish 3 000 so'm bo'ladi.\n\n"
#         elif qiymat >= 18 and qiymat < 65:
#             result = "siz uchun Muzeyga kirish 10 000 so'm bo'ladi.\n\n"
#         print(result)
# print('dastur to\'xtatildi!')




# # #3
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing):\n>>> "

while True:
    qiymat = input(savol)
    if qiymat.lower() =='exit':
        break
    elif int(qiymat)<0:
        continue
    elif int(qiymat)<0:
        print("Iltimos musbat son kiriting")
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")


    



































