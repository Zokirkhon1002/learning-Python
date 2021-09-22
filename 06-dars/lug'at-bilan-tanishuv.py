# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 22:16:36 2021

@author: Zokirkhon
"""
# car_0 = {'model': 'Hyundai', 'rang': 'yashil'}
# print(car_0['model'])
# print(car_0['rang'])


# en_uz = {'apple':'olma', 'apricot':'o\'rik', 'banana':'banan'}
# print(en_uz)
# print(en_uz['apple'])
# print(en_uz['apricot'])
# print(en_uz['banana'])


# mevalar = {'olma':10_000, 'tarvuz':15_000, 'qovun':12_000}
# print(f"Olma narhi {mevalar['olma']} so\'m.")
# print(f"Tarvuz narhi {mevalar['tarvuz']} so\'m.")
# print(f"Qovun narhi {mevalar['qovun']} so\'m.")



# talaba_0 = {'ism':'zokirkhon kotibkhonov', 'yosh':22, 't_yil':2000}
# print(f"{talaba_0['ism'].title()}, \
#  {talaba_0['t_yil']}-yilda tug\'ilgan, \
#  {talaba_0['yosh']} yoshda ")
 
 
 #yangi kalit so'z qo'shish
 
# talaba_0['kurs'] = '4 - kurs';
# talaba_0['fakultet'] = 'Computer Science';
# talaba_0['ism'] = 'Abdulloh';
# print(talaba_0)




# talaba_1 = {}
# talaba_1['ism'] = 'Kotibkhonov Zokirkhon'
# talaba_1['kurs'] = 4
# talaba_1['yosh'] = 22
# print(talaba_1)
# print(F"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
# talaba_1['kurs'] = 3
# print(F"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")



# del yordamida o'chiramiz
# talaba_0 = {'ism':'zokirkhon kotibkhonov', 'yosh':22, 't_yil':2000}
# print(talaba_0)
# del talaba_0['yosh']
# print(talaba_0)


# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'redmi 10',
#     'orif':'Microsoft',
#     'zokirkhon':'Galaxy note8'
#     }


# print(telefonlar['hasan'])
# phone = telefonlar.get('hasan', 'Bunday kalit so\'z yo\'q')
# print(phone)
# phone = telefonlar.get('hasan')
# print(phone)




# Amaliyot
# Uyga Vazifa

# #1
# dadam = {'fullName':'obidov zokhidkhon', 't_yil':1970, 'manzil':'Namangan'}
# onam = {'fullName':'irgasheva salbar', 't_yil':1970, 'manzil':'Namangan'}
# opam = {'fullName':'obidova nasiba', 't_yil':1995, 'manzil':'Namangan'}

# output1 = f"Otamning ismi {dadam['fullName'].title()}, {dadam['t_yil']}-yilda,\
#     {dadam['manzil'].title()} shahrida tug\'ilgan."
# output2 = f"Onamning ismi {onam['fullName'].title()}, {onam['t_yil']}-yilda,\
#     {onam['manzil'].title()} shahrida tug\'ilgan."
# output3 = f"Opamning ismi {opam['fullName'].title()}, {opam['t_yil']}-yilda,\
#     {opam['manzil'].title()} shahrida tug\'ilgan."
    
# print(output1)
# print(output2)
# print(output3)





# #2
# sevimli_taomlar = {'dadam':'palov', 'onam':'ko\'katli shorva', 
#                    'nasiba':'turli xil salatlar', 'zokirkhon':'qozon kabob',
#                    'naima':'shashlik', 'nazira':'manti', 'obidxon':'somsa'}
# output = f"{output1} va sevimli taomlari {sevimli_taomlar['dadam'].title()},\n\
# {output2} va sevimli taomlari {sevimli_taomlar['onam'].title()},\n\
# Nasiba {output3} va sevimli taomlari {sevimli_taomlar['nasiba'].title()}\n\
# Naima Opamning sevimli taomlari {sevimli_taomlar['naima'].title()}\n\
# Nazira Opaming sevimli taomlari {sevimli_taomlar['nazira'].title()}\n\
# Jiyanim Obidxon va kamina Zokirkhonning sevimli taomlari:\
# {sevimli_taomlar['zokirkhon'].title()} va {sevimli_taomlar['obidxon'].title()}"
# print(output)




# #3

python_izohli_lugati = {
    'print':'print() funksiyasi maxsus xabarni ekranda chiqarish uchun foydalaniladi.',
    'variable':'variable ya\'ni o\'zgaruvchi biror ma\'lumotni shu o\'zgaruvchida\
 vaqtincha saqlab turadi',
    'string':'stringlar pythonda qo\'sh tirnoq yoki tirnoqning orasiga yozilgan\
 ma\'lumotlar string deb ataladi(matn)',
    'list': 'ro\'yxat, buning ichida turli xil ma\'lumotlarni saqlasa bo\'ladi',
    'for':'takrorlanish operatori',
    'while':'while ham takrorlanish operatori for dan biroz farq qiladi',
    'if else':'agar, aks xolda, deya birnechta shartlarni bajariladi',
    'elif':'yoki, deya birnechta shartlarni bajariladi',
    'f""':'bu belgi orqali matnlar bilan funksiya, o\'zgaruvchi va \
    hokazolarni foydalansa bo\'ladi.',
    'dictionary':'lug\'at, key value pair(kalit so\'z, qiymat juftligi)',
    'integer':'butun son',
    'float': 'o\'nlik sonlar',
    'logical operator':'mantiqiy operatorlar',
    'string method':"string metodlar, matn bilan ishlashda qulayliklar beradi",
    'list method':"ro'yxat bilan ishlashda qulayliklar beradi"
    }

kalit_soz = input("pythondagi ba'zi so'zlarning ma'nolarini bilib oling\n>>> ").lower()
# result = python_izohli_lugati.get(kalit_soz, "Bunday so'z lug'atimizda topilmadi")
# print(result)

result2 = python_izohli_lugati.get(kalit_soz)

if result2 == None:
   print("Bunday so'z lug'atimizda topilmadi")
else:
   print(f"{kalit_soz.title()} so'zi {result2} degan ma'nolariga ega")
        








































