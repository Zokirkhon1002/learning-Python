# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 21:27:14 2021

@author: Zokirkhon
"""








# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':2018,
#         'narh':13_000,
#         'km':50_000,
#         'karobka':'avtomat'
#         }
# car1 = {
#         'model':'nexia 3',
#         'rang':'qora',
#         'yil':2017,
#         'narh':9000,
#         'km':65_000,
#         'karobka':'mexanika'
#         }
# car2 = {
#         'model':'gentra',
#         'rang':'gray',
#         'yil':2019,
#         'narh':15_000,
#         'km':20_000,
#         'karobka':'avtomat'
#         }
# cars = [car0, car1, car2]
# for each_car in cars:
#     print(f"{each_car['model'].title()},"
#           f"{each_car['rang']} rang,"
#           f"{each_car['yil']}-yil, {each_car['narh']},")

# print(cars[0]['model'])
# print(cars)


# malibus=[]
# for n in range(10):
#     new_car = {
#         'model':'malibu',
#         'rang':None, # rang noaniq
#         'yil':2020,
#         'narh':None, 
#         'km':0,
#         'karobka':'avto'
#         }
#     malibus.append(new_car)
    
# print(malibus)

# # for malibu in malibus:
# #     print(malibu)


# for malibu in malibus[:3]:
#     malibu['rang']="qizil"

# # for malibu in malibus:
# #     print(malibu)

# for malibu in malibus[3:6]:
#     malibu['rang']="qora"

# # for malibu in malibus:
# #     print(malibu)

# for malibu in malibus[6:]:
#     malibu['rang']="kulrang"
#     malibu['karobka']="mexanik"

# # for malibu in malibus:
# #     print(malibu)

# for malibu in malibus:
#     if malibu['karobka'] =='avto':
#         malibu['narh'] = 40_000
#     else:
#         malibu['narh'] = 35_000

# for malibu in malibus:
#     print(malibu)








# # # Lug'at ichida ro'yxat
# dasturchilar = {
#     'ali':['python', 'c++'],
#     'zokirkhon':['html','css','js',
#                  'sass','bootstrap','materializecss','reactjs',
#                  'nodejs', 'python',
#                  'mangodb', 'data science'],
#     'hasan':['php', 'sql'],
#     'husan':['python', 'php'],
#     'maryam':['c', 'c#', 'c++']
#     }

# for ism,tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())

# for ism,tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(f"{til.upper()}, ", end='')







# hamkasblar = {
#     'ali':{'familya':'valiyev',
#            't_yil':1995,
#            'malumot':'maxsus',
#            'tillar':['python', 'c++'],
#            },
#     'zokirkhon':{'familya':'kotibkhonov',
#            't_yil':1999,
#            'malumot':'oliy',
#            'tillar':['html','css','js',
#                  'sass','bootstrap','materializecss','reactjs',
#                  'nodejs', 'python',
#                  'mangodb', 'data science'],
#            },
#     'hasan':{'familya':'husanov',
#            't_yil':2001,
#            'malumot':'o\'rta maxsus',
#            'tillar':['php', 'sql'],
#            },
#     'husan':{'familya':'hasanov',
#            't_yil':2000,
#            'malumot':'maxsus',
#            'tillar':['python', 'php'],
#            },
#     'maryam':{'familya':'ominova',
#            't_yil':2002,
#            'malumot':'maxsus',
#            'tillar':['c', 'c#', 'c++'],
#            },
#     }
# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familya'].title()}, "
#           f"{info['t_yil']}-yilda tu'g'ilgan. "
#           f"Ma'lumoti: {info['malumot']}. \n"
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())









# Amaliyot
# Uyga vazifa

# # #1
# shaxs01 = {
#     'ism':'Jaloliddin Rumiy r.alayhi',
#     't_yil':1207,
#     'v_yil':1273,
#     't_joy':'Balx',
#     'v_joy':'Konya'
#     }
# shaxs02 = {
#     'ism':'Alisher Navoiy r.alayhi',
#     't_yil':1441,
#     'v_yil':1501,
#     't_joy':'Hirot',
#     'v_joy':'Hirot'
#     }
# shaxs03 = {
#     'ism':'Abu Abdulloh ibn Ismoil r.alayhi',
#     't_yil':810,
#     'v_yil':870,
#     't_joy':'Buxoro',
#     'v_joy':'Buxoro'
#     }
# shaxs04 = {
#     'ism':'Erkin Vohidov',
#     't_yil':1936,
#     'v_yil':2016,
#     't_joy':'Farg\'ona',
#     'v_joy':'Toshkent'
#     }

# shaxslar = [shaxs01, shaxs02, shaxs03, shaxs04]
# for shaxs in shaxslar:
#     ism, tyil, vyil, tjoy, vjoy = shaxs['ism'], shaxs['t_yil'], shaxs['v_yil'], shaxs['t_joy'], shaxs['v_joy']
#     print(f"{ism} {tyil}-yilda {tjoy}da tavallud topganlar."
#           f"va {vyil}-yilda {vjoy}da vafot etganlar.\n")






# # #2
# shaxs01 = {
#     'ism':'Jaloliddin Rumiy r.alayhi',
#     't_yil':1207,
#     'v_yil':1273,
#     't_joy':'Balx',
#     'v_joy':'Konya',
#     'asarlar':['Masnaviy-Ma\'naviy', 'Ichindagi-Ichindadir', 'Maktubot']
#     }
# shaxs02 = {
#     'ism':'Alisher Navoiy r.alayhi',
#     't_yil':1441,
#     'v_yil':1501,
#     't_joy':'Hirot',
#     'v_joy':'Hirot',
#     'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
#     }
# shaxs03 = {
#     'ism':'Abu Abdulloh ibn Ismoil r.alayhi',
#     't_yil':810,
#     'v_yil':870,
#     't_joy':'Buxoro',
#     'v_joy':'Buxoro',
#     'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
#     }
# shaxs04 = {
#     'ism':'Erkin Vohidov',
#     't_yil':1936,
#     'v_yil':2016,
#     't_joy':'Farg\'ona',
#     'v_joy':'Toshkent',
#     'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
#     }

# shaxslar = [shaxs01, shaxs02, shaxs03, shaxs04]

# for each_person in shaxslar:
#     ism = each_person['ism']
#     asarlar = each_person['asarlar']
    
#     print(f"\n{ism}ning mashxur asarlari: ")
#     for asar in asarlar:
#         print(asar)





# # #3
# print("Ismingizni va 3ta yaxshi ko'rgan kinoyingizni nomini kiriting.")
# name1 = input("Iltimos ismingizni kiritng:\n>>> ")
# array1 = []
# for i in range(3):
#     liked_movie = input(f"Iltimos {i+1}-yaxshi ko'rgan kinoyngizni nomini kiriting:\n>>> ")
#     array1.append(liked_movie)
# ## print(f"{name1}\n{array1}")



# print("Ismingizni va 3ta yaxshi ko'rgan kinoyingizni nomini kiriting.")
# name2 = input("Iltimos ismingizni kiritng:\n>>> ")
# array2 = []
# for i in range(3):
#     liked_movie = input(f"Iltimos {i+1}-yaxshi ko'rgan kinoyngizni nomini kiriting:\n>>> ")
#     array2.append(liked_movie)
# ## print(f"{name2}\n{array2}")




# print("Ismingizni va 3ta yaxshi ko'rgan kinoyingizni nomini kiriting.")
# name3 = input("Iltimos ismingizni kiritng:\n>>> ")
# array3 = []
# for i in range(3):
#     liked_movie = input(f"Iltimos {i+1}-yaxshi ko'rgan kinoyngizni nomini kiriting:\n>>> ")
#     array3.append(liked_movie)
# ## print(f"{name3}\n{array3}")

# lugat = {
#     name1: array1,
#     name2: array2,
#     name3: array3
#     }

# for ism, values in lugat.items():
#     print(f"\n{ism}ning yaxshi ko'rgan kinolari: {values}")
#     for value in values:
#         print(value)





# # #4
davlatlar = {
    "o\'zbekiston":{"poytaxti": "toshkent",
                   'maydon':448978,
                   'aholisi':35_111_000,
                   'pul_birligi': 'so\'m'
                   },
    "malayziya":{"poytaxti": "kuala lampur",
                   'maydon':329750,
                   'aholisi':32_730_000,
                   'pul_birligi': 'ringgit'
                   },
    "indoneziya":{"poytaxti": "jakarta",
                   'maydon':1_904_569,
                   'aholisi':271_350_000,
                   'pul_birligi': 'rupiya'
                   },
    "turkiya":{"poytaxti": "istanbul",
                   'maydon':783_356,
                   'aholisi':84_000_000,
                   'pul_birligi': 'lira'
                   }
    }

# for davlat, malumot in davlatlar.items():
#     print(f"\n{davlat.upper()} ning poytaxti: {malumot['poytaxti'].title()},"
          # f"\n maydoni: {malumot['maydon']},"
          # f"\n aholisi: {malumot['aholisi']},"
          # f"\n va pul birligi: {malumot['pul_birligi']}")





# # #5
d_name = input("Davlat nomini yoki poytaxt nomini yoki pul birligini kiriting\n>>> ").lower()
natija = ''
if len(d_name):
    for davlat,info in davlatlar.items():
        if d_name == davlat:
            print(f"{davlat.upper()} ning poytaxti: {info['poytaxti']},"
                  f"\n maydoni: {info['maydon']},"
                  f"\n aholisi: {info['aholisi']},"
                  f"\n va pul birligi: {info['pul_birligi']}")
        elif d_name == info['poytaxti']:
            print(f"{davlat.upper()} ning poytaxti: {info['poytaxti']},"
                  f"\n maydoni: {info['maydon']},"
                  f"\n aholisi: {info['aholisi']},"
                  f"\n va pul birligi: {info['pul_birligi']}")
        elif d_name == info['pul_birligi']:
            print(f"{davlat.upper()} ning poytaxti: {info['poytaxti']},"
                  f"\n maydoni: {info['maydon']},"
                  f"\n aholisi: {info['aholisi']},"
                  f"\n va pul birfoligi: {info['pul_birligi']}")
        # for name, value in info.items():
        #     temporery = ''
        #     if type(info[name]) == str():
        #         temporery = info[name]
        #         if not d_name in davlatlar.keys() and not d_name in temporery:
        #             natija = f"Uzr bizdan {d_name.title()} nomi davlat haqida ma'lumot yo'q."
            
    print(natija)








































