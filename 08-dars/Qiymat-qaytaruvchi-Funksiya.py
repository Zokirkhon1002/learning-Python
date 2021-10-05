# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 23:52:46 2021

@author: Zokirkhon
"""


# # #1
# def toliq_ism_yasa(ism,familya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"ism: {ism}, familya: {familya}"
#     return toliq_ism;

# talaba1 = toliq_ism_yasa("Zokirkhon","Kotibkhonov")
# talaba2 = toliq_ism_yasa("Sayfullokhon","Ulug'xojaev")
# print(f"Koreada o'qiyotdan talabalar: \n1-{talaba1}, \n2-{talaba2}")








# # #2
# def toliq_ism_yasa(ism,familya, otasining_ismi=""):
#     """To'liq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"ism: {ism}, \nfamilya: {familya}, \nOtasining ismi: {otasining_ismi}"
#     else:
#         toliq_ism = f"ism: {ism}, familya: {familya}"
#     return toliq_ism.title();

# talaba1 = toliq_ism_yasa("Zokirkhon","Kotibkhonov", "Zokhidkhon O\'g\'li") 
# talaba2 = toliq_ism_yasa("Sayfullokhon","Ulug'xojaev")
# print(f"Koreada o'qiyotdan talabalar: \n1-{talaba1}, \n2-{talaba2}")









# # #3
# def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None):
#     """Mashina ma'lumotlarini qaytarib beruvchi funksiya"""
#     avto = {"kompaniya": kompaniya,
#             "model": model,
#             "rang": rangi,
#             "karobka": karobka,
#             "yili": yili,
#             "narhi":narhi}
#     return avto;
# avto1 = avto_info("GM","Malibu 2","Oq","Avtomat",2021,29500)
# avto2 = avto_info("GM","Gentra 2","Qora","Avtomat",2020)
# avtolar = [avto1, avto2];
# print("Onlayn bozordagi mavjud avtomashinalar:")
# for avto in avtolar:
#     if avto['narhi']:
#         narh = avto['narhi']
#     else:
#         narh = 'Noma\'lum'
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")






# # #4
# def oraliq(min,max,qadam=1):
#     """range funksiyasini o'zimiz yozdik"""
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min+=qadam
#     return sonlar;
# sonlar = oraliq(0,20,2)
# print(sonlar)








# # #5
# def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None):
#     """Mashina ma'lumotlarini qaytarib beruvchi funksiya"""
#     avto = {"kompaniya": kompaniya,
#             "model": model,
#             "rang": rangi,
#             "karobka": karobka,
#             "yili": yili,
#             "narhi":narhi}
#     return avto;

# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz")
# avtolar = [];
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting", end=" ")
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     karobka=input("Karobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
#     # Foydalanuvchi kiritgan ma'lumotlardan avto_info yordamida
#     # lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili, narhi))
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("yana avto qo'shasizmi? (yes/no): ")
#     if javob == 'no':
#         break


# print("\nSaloningizdagi avtolar:")
# for avto in avtolar:
#     if avto['narhi']:
#         narh = avto['narhi']
#     else:
#         narh = 'Noma\'lum'
#     print(f"{avto['rang'].title()}, {avto['model'].title()}, {avto['karobka'].title()} karobka. Narhi: {narh}")








### Amaliyot
### Uyga Vazifa


# import datetime
# x = datetime.datetime.now()
# year = x.year;


###1
###2

# def person_info(ism,familya,t_yil,t_joy,email="", tel_raqam='',):
#     """Ma'lumotlarni lug'at ko'rinishda qaytaruvchi funksiya"""
#     informations = {
#         "ism": ism,
#         "familya": familya,
#         "t_yil":t_yil,
#         "t_joy":t_joy,
#         "email":email,
#         "tel_raqam":tel_raqam
#         }
#     return informations;



# print("Ma'lumotlaringizni to'ldiring.")
# malumotlar = []
# while True:
#     ism=input("Ismingizni kiriting: ")
#     familya=input("Familyangizni kiriting: ")
#     t_yil=int(input("Tug'ilgan yilingizni kiriting: "))
#     t_joy=input("Tug'ilgan joyingizni kiriting: ")
#     email=input("Emailingizni kiriting: ")
#     tel_raqam=input("Telefon raqamingizni kiriting: ")
#     # Foydalanuvchi kiritgan ma'lumotlardan avto_info yordamida
#     # lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     malumotlar.append(person_info(ism,familya,t_yil,t_joy,email,tel_raqam))
#     # circle ni qaytarilishi yoki qaytarilmasligini so'raymiz
#     javob = input("Yana ma'lumotlar kiritasizmi? (yes/no): ")
#     if javob == "no":
#         break




# print("\nQuyidagi siz kiritgan shaxslar ma'lumotlari:")
# for malumot in malumotlar:
#     if malumot['email']:
#         email = malumot['email']
#     else:
#         email = 'Noma\'lum'
#     if malumot['tel_raqam']:
#         tel_raqam = malumot['tel_raqam']
#     else:
#         tel_raqam = 'Noma\'lum'
#     print(f"\nismi: {malumot['ism'].title()}"
#           f"\nfamilyasi: {malumot['familya'].title()}"
#           f"\nTu'gilgan yili: {malumot['t_yil']}"
#           f"\nYoshi: {year - malumot['t_yil']}"
#           f"\nTug'ilgan joyi: {malumot['t_joy'].title()}"
#           f"\nEmail: {malumot['email'].lower()}"
#           f"\nTelefon raqami: {malumot['tel_raqam']}"
#           )
    




###3
# def get_max(a,b,c):
#     """Return the max of three parametrs"""
#     if (a > b) and (a > c):
#         return a;
#     elif (b > a) and (b > c):
#         return b
#     else:
#         return c

# print(get_max(12,43,34))






###4
# def aylana_malumotlari(r):
#     PI = 3.14159;
#     aylana_info = {
#         'radius': r,
#         'diametr': 2*r,
#         'perimetr': 2 * PI * r,
#         'yuza': PI * r ** 2
#         }
#     return aylana_info;

# r = float(input("Aylananing radiusini kiriting: "))
# print(aylana_malumotlari(r))







###5

# def Tubson_qaytar(n):
#     """Agar Tub son qaytaradigan funksiya."""
    
    
#     def oraliq(min,max,qadam=1):
#         """range funksiyasi o'zimizniki, o'zbek tilida"""
#         sonlar = []
#         while min<max:
#             sonlar.append(min)
#             min+=qadam
#         return sonlar;
    
    
#     for i in oraliq(2,n):
#         if(n%i==0):
#             return f"Kiritilgan {n} soni Tubson emas"
#     return f"Kiritilgan: {n}  Tubson";



# print(Tubson_qaytar(1))
# print(Tubson_qaytar(4))
# print(Tubson_qaytar(5))
# print(Tubson_qaytar(7))
# print(Tubson_qaytar(9))
# print(Tubson_qaytar(11))
# print(Tubson_qaytar(13))
# print(Tubson_qaytar(15))







###6

##6.1
def Fiboanchi_qaytar(n):
    """nta fibochi sonlarni qaytaradi"""
    a = 1
    b = 0
    vaqtincha = 0
    fibochi_sonlar = []
    while n>=0:
        vaqtincha = a;
        a = a+b;
        b = vaqtincha;
        fibochi_sonlar.append(b)
        n-=1
    return fibochi_sonlar;



##6.2
# def Fiboanchi_qaytar(n):
#     """n-fibochi sonni qaytaradi"""
#     if n <= 1:
#         return 1;
#     else:
#         return Fiboanchi_qaytar(n-1)+Fiboanchi_qaytar(n-2)




##6.3
# def Fiboanchi_qaytar(n):
#     """nta fibochi sonlarni qaytaradi"""
#     fibochi_sonlar = []
#     for i in range(n):
#         if i<=1:
#             fibochi_sonlar.append(1)
#         else:
#             fibochi_sonlar.append(fibochi_sonlar[i-1]+fibochi_sonlar[i-2])
#     return fibochi_sonlar


n = int(input("son kiriting: "))
print(Fiboanchi_qaytar(n))
# print(sonlar)





























