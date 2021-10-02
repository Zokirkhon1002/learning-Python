# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 20:46:58 2021

@author: Zokirkhon
"""

# #1
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# ismlar = []
# n=1 ## ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingizni ismini kiriting:\n>>> "
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)\n>>> ")
#     n+=1
#     if takrorlash != 'ha':
#         break
# print("dastur tugadi,\nsizning do'stlaringizning ismlar ro'yxati:")
# for ism in ismlar:
#     print(ism.title())






# #2
# print("Yaqin do'stlaringiz yoshini saqlaymiz:\n>>> ")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting:\n>>> ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting:\n>>> ")
#     dostlar[ism] = int(yosh)
    
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)\n>>> ")
#     if javob == "yo'q":
#         ishora = False

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()}ning yoshi: {yosh} da")






# #3
# cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'audi', 'malibu', 'nexia']
# car = 'nexia'
# while car in cars:
#     cars.remove('nexia')
# print(cars)






# #4
# students = ['Zokirkhon', 'Sayfullokhon', 'Khurshidbek', 'Abdulkhamid', 'A\'zmjon', 'Ismoil']
# evaulated_student = {}
# while students:
#     student = students.pop()
#     grade = input(f"{student.title()}ning bahosini kiriting:\n>>> ")
#     if grade.isdigit():
#         grade = float(grade)
#     else:
#         grade = str(grade)
#     print(f"{student.title()} baholandi\n")
#     evaulated_student[student] = grade

# for key,value in evaulated_student.items():
#     print(f"{key.title()} talabaning bahosi: {value} ")






# # Uyga vazifa
# # Amaliyot


# #1
savatcha = ['sabzi', 'kartoshka','shaftoli']
# chiqish = ['exit', 'chiqish', 'quit']
# while True:
#     print("Eslatma!. (quit/exit/chiqish) so'zlaridan birini kiritsangiz dastur to'xtaydi.")
#     mahsulot = input("Savatchaga mahsulot qo'shing\n>>> ").lower()
#     if mahsulot in chiqish:
#         break
#     savatcha.append(mahsulot)

# print("dastur to'xtatildi!\nSiz buyurtma qilgan mahsulotlar ro'yxati:")
# for mahsulotlar in savatcha:
#     print(mahsulotlar.title())





# #2
# print("e-bozor uchun do'konga mahsulot va uning narhlarini kiritish bo'limi.")
mahsulotlar = {'sabzi':3400,"go'sht":55000,'kartoshka':4000}
# ishora = True
# while ishora:
#     m_nomi = input("Mahsulot nomini kiriting:\n>>> ").lower()
#     m_narhi = input(f"{m_nomi.title()} ning narhini kiriting:(so'mda)\n>>> ")
#     if m_narhi.isdigit():
#         m_narhi = int(m_narhi)
#     else:
#         m_narhi = str(m_narhi)
#     mahsulotlar[m_nomi] = m_narhi
    
#     javob = input("Dastur to'xtasinmi? (ha/yo'q) so'zini kiriting:\n>>> ").lower()
#     if javob == 'ha':
#         ishora = False

# for nomi, narhi in mahsulotlar.items():
#     print(f"{nomi.title()} ning narhi: {narhi} so'm")





# #3
# # yuqoridagi 2tasiga bog'liq
print('\n3-mashq!!!\n')
is_not_mahsulot = []
while savatcha:
    buyurtma = savatcha.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} ning narhi: {narh} so'm")
    else:
        is_not_mahsulot.append(buyurtma)
print("\nbizda bu mahsulotlar yo'q: ")
for each in is_not_mahsulot:
    print(each.title())


        


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
