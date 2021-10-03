# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 01:29:28 2021

@author: Zokirkhon
"""




# # #1
# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")

# salom_ber()








# # #2
# def salom_ber(ism):
#     """foydalanuvchini ismini so'rab unga 
#         salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")

# salom_ber("Zokirkhon")
# salom_ber("Sayfullokhon")

# salom_ber()
# print(salom_ber.__doc__)
# print(print.__doc__)







# # #3
# def toliq_ism(ism,familya):
#     """Foydalanuvchi ism va familyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familyasi: {familya.title()}")

# toliq_ism("Zokirkhon","Kotibkhonov")







# # #4
import datetime
x = datetime.datetime.now()
year = x.year;



# def yosh_hisobla(ism,t_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {year - t_yil} yoshda")

# yosh_hisobla("Zokirkhon", 1999)


# # yosh_hisobla(1999, "Zokirkhon") # xatolik yuz beradi

# #buni oldini olish uchun esa bu shaklda kiritishimiz mumkin.

# yosh_hisobla(t_yil=1999, ism="Zokirkhon")








# # #5
# def yosh_hisobla(t_yil, joriy_yil=year):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"{joriy_yil - t_yil} yoshdasiz")

# yosh_hisobla(1995,2020)
# yosh_hisobla(1995)



# tyil = int(input("Tug'ilgan yilingizni kiriting:\n>>> "))
# yosh_hisobla(tyil)










# # #Uyga Vazifa
# # #Amaliyot


# # #1
# def yosh_hisobla(ism,t_yil):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"{ism.title()}, {year - t_yil} yoshdasiz")

# ism = input("Ismingizni kiriting:\n>>> ")
# tyil = int(input("Tug'ilgan yilingizni kiriting:\n>>> "))
# yosh_hisobla(ism,tyil)








# # #2
# def kvadrat_kub_qaytar(son):
#     """Kiritilgan sonning kvadrati va kubini qaytarib beruvchi funksiya"""
#     print(f"{son} ning kvadrati: {son**2}.\nKubi esa: {son**3}.")

# son = int(input("Biror butun son kiriting:\n>>> "))
# kvadrat_kub_qaytar(son)







# # #3
# def juft_yoki_toq_qaytar(son):
#     """Kiritilgan sonning juft yoki toq ekanligini qaytaradigan funksiya"""
#     if son%2==0:
#         print(f"Kiritilgan {son}, juft son ekan")
#     else:
#         print(f"Kiritilgan {son}, toq son ekan")

# son = int(input("Biror butun son kiriting:\n>>> "))
# juft_yoki_toq_qaytar(son)









# # #4
# def katta_son_qaytar(n1,n2):
#     """2ta butun son qabul qiladi va kattasini qaytaradi, 
#         agar 2tasi ham teng bo'lsa "Sonlar teng" yozuv qaytaradigan
#         funksiya!"""
#     if n1>n2:
#         print(f"Kiritilgan {n1} soni katta ekan")
#     elif n1<n2:
#         print(f"Kiritilgan {n2} soni katta ekan")
#     else:
#         print(f"Kiritilgan sonlar teng ekan {n1} = {n2}")

# n1 = int(input("Ikkita son kiriting:\n>>> "))
# n2 = int(input("Ikkita son kiriting:\n>>> "))
# katta_son_qaytar(n1,n2)












# # #5
# def consolega_chiqar(x,y):
#     """2ta butun son qabul qiladi va ularni console ga chiqaradi"""
#     print(f"Kiritilgan x= {x}, y= {y}")

# x = int(input("Birinchi son kiriting. X = \n>>> "))
# y = int(input("Ikkinchi son kiriting. Y = \n>>> "))
# consolega_chiqar(x,y)









# # #6
# def consolega_chiqar(x=6,y=5):
#     """2ta butun son qabul qiladi va ularni console ga chiqaradi"""
#     print(f"Kiritilgan x= {x}, y= {y}")

# consolega_chiqar()







# # #7
result = ''
def bolinish_alomatlari(n):
    for x in range(2,11):
        if not n % x:
            print(f"{n} soni {x} ga qoldiqsiz bo'linadi")


n = int(input("Biror son kiriting. n = \n>>> "))
bolinish_alomatlari(n)




























