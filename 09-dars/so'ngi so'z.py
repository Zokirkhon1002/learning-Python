"""
Created on Mon Oct 11 01:26:33 2021

@author: Zokirkhon

"""


### Lambda funksiyasi
from math import sqrt


# def nom(argument):
#     return ifoda


# uzunik = lambda pi, r: 2*pi*r
# print(uzunik(math.pi,10))


# kvadrat = lambda x,y:x**y;
# print(kvadrat(3,3))



# def daraja(n):
#     return lambda x:x**n
# print(daraja(3))
# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati: {kvadrat(3)} ga,"
#       f"kubi: {kub(3)} ga teng")





# sonlar = list(range(11))
# ildizlar = list(map(sqrt,sonlar))
# print(ildizlar)



# def daraja2(x):
#     """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x*x


# print(list(map(daraja2,sonlar)))


##Lambda funksiyasi bilan
# print(list(map(lambda x:x*x,sonlar)))




# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9]
# a_plus_b_plus_c = list(map(lambda x,y,z:x+y+z,a,b,c))
# print(a_plus_b_plus_c)





# ismlar = ['hasan','husan','olim','umid','Zokirkhon']
# print(list(map(lambda ism:ism.upper(),ismlar)))







import random as r

# sonlar  = r.sample(range(100),10)
# print(sonlar)





# def juftmi(x):
#     """x juft bo'lsa True, aks holda False qaytaradi"""
#     return x%2==0

# juft_sonlar = list(filter(juftmi,sonlar))
# print(juft_sonlar)



# juft_sonlar = list(filter(lambda x:x%2==0,sonlar))
# print(juft_sonlar)






# mevalar = ['olma', 'anor', 'anjir', 'shaftoli', 'o\'rik','tarvuz', 'banan','behi']
# harf = 'b'
# mevalar_b = list(filter(lambda meva:meva.startswith(harf),mevalar))
# print(mevalar_b)


# mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
# print(mevalar2)


# result1 = list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')),mevalar))
# print(result1)


































































