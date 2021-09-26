# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 22:41:21 2021

@author: Zokirkhon
"""

# methods
# # items() lug'atning ichidagi barcha ma'lumotlarni ko'rsatadi
# talaba_0 = {
#     'ism':'alijon',
#     'familya':'shamshiyev',
#     'yosh':23,
#     'fakultet':'Matematika',
#     'kurs': 4
#     }
# print(talaba_0.items())
# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat}\n")





# telefonlar = {
#     'ali': 'iphone x',
#     'sayfulloh':'iphone 6s',
#     'vali': 'mi 10 pro',
#     'olim': 'galaxy note8',
#     'orif':'nokia 3310'
#     }

# for k,v in telefonlar.items():
#     print(f"{k.title()}ning telefoni {v}")




# # .keys() mthod faqat ichidagi kalitlarni bilish uchun foydalaniladi
# mahsulotlar = {
#     'olma': 10_000,
#     'anor': 20_000,
#     'uzum': 30_000,
#     'anjir': 25_000,
#     'shaftoli': 15_000,
#     }

# # print(mahsulotlar.keys())

# print('Do\'kondagi mahsulotlari:')
# for each in mahsulotlar.keys():
#     print(each.title())


# print('Do\'kondagi mahsulotlar:')
# for each in mahsulotlar:
#     print(each.title())





# bozorlik = ['anor', 'uzum', 'non', 'baliq']

# for good in mahsulotlar:
#     if good in bozorlik:
#         print(f"{good.title()} {mahsulotlar[good]} so'm")

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum.title()} ham olib keling")





# print(mahsulotlar)
# print('Do\'kondagi mahsulotlari:')
# for key in sorted(mahsulotlar):
#     print(key.title())




# # .values() qiymatlar
# print(telefonlar)
# print(telefonlar.values())
# print("Foydalanuvchilar quyidagi telefonlarni ishlatadi:")
# for phone in telefonlar.values():
#     print((phone))




# # .set() takrorlanishni qaytarmaydi.
# # telefon lug'atini kengaytiramiz
# telefonlar['hamida'] = 'huawei p30'
# telefonlar['maryam'] = 'samsung a30'
# telefonlar['tina'] = 'iphone xs max'
# telefonlar['hamida'] = 'microsoft'

# print(telefonlar)
# print("Foydalanuvchilar quyidagi telefonlarni ishlatadi:")
# for phone in telefonlar.values():
#     print((phone))
# print('\n')
# print("Foydalanuvchilar quyidagi telefonlarni ishlatadi:")
# for phone in set(telefonlar.values()):
#     print((phone))



# # set ham ma'lumot turlaridan biri

# setToys = {'ball', 'car', 'lamp','ball'}
# listToys = ['ball', 'car', 'lamp','ball']
# tupleToys = ('ball', 'car', 'lamp','ball')
# dicToys = {'ball':'football', 'car':'bmw', 'lamp':'akfa', 'rang':'green'}

# print(setToys)
# print(type(setToys))
# print(type(listToys))
# print(type(tupleToys))
# print(type(dicToys))




#Amaliyot
#Uyga vazifa

# python_izohli_lugati = {
#     'print':'print() funksiyasi maxsus xabarni ekranda chiqarish uchun foydalaniladi.',
#     'variable':'variable ya\'ni o\'zgaruvchi biror ma\'lumotni shu o\'zgaruvchida\
#  vaqtincha saqlab turadi',
#     'string':'stringlar pythonda qo\'sh tirnoq yoki tirnoqning orasiga yozilgan\
#  ma\'lumotlar string deb ataladi(matn)',
#     'list': 'ro\'yxat, buning ichida turli xil ma\'lumotlarni saqlasa bo\'ladi',
#     'for':'takrorlanish operatori',
#     'while':'while ham takrorlanish operatori for dan biroz farq qiladi',
#     'if else':'agar, aks xolda, deya birnechta shartlarni bajariladi',
#     'elif':'yoki, deya birnechta shartlarni bajariladi',
#     'f""':'bu belgi orqali matnlar bilan funksiya, o\'zgaruvchi va \
#     hokazolarni foydalansa bo\'ladi.',
#     'dictionary':'lug\'at, key value pair(kalit so\'z, qiymat juftligi)',
#     'integer':'butun son',
#     'float': 'o\'nlik sonlar',
#     'logical operator':'mantiqiy operatorlar',
#     'string method':"string metodlar, matn bilan ishlashda qulayliklar beradi",
#     'list method':"ro'yxat bilan ishlashda qulayliklar beradi"
#     }


# print(python_izohli_lugati.values())
# print("Python dagi ba'zi so'zlariga izoh:")
# for k,v in sorted(python_izohli_lugati.items()):
#     print(f"{k.upper()}: \t {v} degan ma'nosi bor")


capital_of_country = {
"india":"delhi",
"nepal":"kathmandu",
"pakistan":"islamabad",
"russia":"moscow",
"china":"peikng",
"afghanistan":"kabul",
'japan': 'tokyo',
'belgium':'brussels',
'france':'paris',
'germany':'berlin',
'italy':'rome',
'poland':'warsaw',
'australia': 'canberra',
'england': 'london',
'south africa':'pretoria',
'uzbekistan':'tashkent',
"united arab emirates":"abu dhabi",
'turkey':'istanbul',
"malaysia":"kuala Lumpur",
"indonesia":"jakarta",
"south Korea":"seoul",
"united States":"washington"
    }





# print(capital_of_country.keys())
# print('\n')
# print(capital_of_country.values())

# print("Ba'zi davlatlarning nomi va poytaxti':")
# for key in sorted(capital_of_country):
#     print(key.upper())

# print("\nBa'zi davlatlarning nomi va poytaxti':")
# for key in sorted(capital_of_country.values()):
#     print(key.title())

# print("Ba'zi davlatlarning nomi va poytaxti':")
# for k,v in sorted(capital_of_country.items()):
#     print(f"{k.upper()} ning poytaxti:  {v.upper()} ")





name = input("Please enter country name or capital of country\n>>> ").lower()



# result = capital_of_country.get(name)

# if result != None:
#     print(f"{name.upper()} ning poytaxti {result.upper()} shahri")
# elif result == None:
#     print(f'Kechirasiz, bizda bunday {name.title()} nomli ma\'lumot yo\'q') 

natija = ''

if len(name):
    for k,v in capital_of_country.items():
        if name == v:
            print(f"{k.upper()} ning poytaxti: {name.upper()}")
        elif name == k:
            print(f"{name.upper()} ning poytaxti: {v.upper()}")
        elif not name in capital_of_country.keys() and not name in capital_of_country.values():
            natija = f"Kechirasiz, bizda bunday {name.title()} nomli ma\'lumot yo\'q"
    print(natija)




# menu = {
#         "osh":15_000,
#         "mastava":10_000,
#         "bishteks":11_000,
#         "achchiq go'sht":14_000,
#         "manti":12_000,
#         "shashlik":8_000,
#         "qozon kabob":13_000,
#         "tushonka":16_000,
#         "shorva":7_000,
#         "chuchvara":12_000,
#         "tiftel":9_000
#         }


# input_menu = []
# print("istagan 3ta taom nomini kiriting:")
# for i in range(3):
#     taom = input(f"{i+1}-taomning nomini kiriting:\n>>> ").lower()
#     input_menu.append(taom)

# for each in menu:
#     if each in input_menu:
#         print(f"{each.title()} ning narhi: {menu[each]} so'm")
    # else:
    #     print(f"\nbizda bunday {each.title()} yo\'q.")
    # bu yerga yozsak, bor ovqatlarning orasiga tushib qolar ekan
        
# for each in input_menu:
#     if each not in menu:
#         print(f"\nbizda bunday {each.title()} yo\'q.")















































































