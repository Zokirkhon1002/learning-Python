""" *args va **kwargs - key words arguments"""


# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     # yigindi = 0
#     # for son in sonlar:
#     #     yigindi += son
#     # return yigindi
#     return sum(sonlar)
# print(summa(1,2,3,4,5,6))
# print(summa(4,5,6))
# print(summa(1,2,3,4))


# def summa(x,y,*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     # yigindi = 0
#     # for son in sonlar:
#     #     yigindi += son
#     # return yigindi
#     return x+y+sum(sonlar)
# print(summa(1,2,3,4,5,6))
# print(summa(4,5,6))
# print(summa(1,2,3,4))


# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar

# avto1 = avto_info("GM","Malibu 2",rang = "Oq",karobka ="Avtomat",yili = 2021, narhi = 29500)
# print(avto1)


# Uyga vazifa
# Amaliyot
# 1

# def kopaytma(*sonlar):
#     result = 1
#     for son in sonlar:
#         result *= son
#     return result;
# print(kopaytma(1,2,3,4,5,6,7,8))


# 2
# def talaba_info(ism, familya, **infos):
#     """Talabalar haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     infos['ism']=ism
#     infos['familya']=familya
#     return infos;

# talaba1 = talaba_info("Khurshidbek","Alisherov", yosh = 21, tugilgan_yil = 2000, fakultet = "IT", yonalish = "AI")
# talaba2 = talaba_info("Zokirkhon","Kotibkhonov", yosh = 21, tugilgan_yil = 1999, fakultet = "IT", yonalish = "AI")

# print(talaba1)
# print(talaba2)





names = ["Khurshidbek", "Zokirkhon", "Abdulkhamid", "Azamjon", "Ismoilxon"]
