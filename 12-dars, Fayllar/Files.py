# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 21:48:44 2021

@author: Zokirkhon
"""


###1
# file = open("app.js") # tavsiya qilinmaydi, 
# log = file.read()
# print(log)
# # ochiq holatda qolib ketadi
# file.close() # ni yozmagunimizcha




###2
# Tavsiya qilinadigan usul
# with open("app.js") as file:
#     log = file.read()
# print(log)

# with open("pi.txt") as file:
#     pi = file.read()
# print(pi)

# pi = pi.rstrip() 
# pi = pi.replace('\n','')
# pi = float(pi)
# print(pi)







###3
# filename = "data/talabalar.txt"
# # with open(filename) as file:
# #     for line in file:
# #         print(line)

# with open(filename) as file:
#     talabalar = file.readlines()

# print(talabalar)

# talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)






###4
# faylnomi = 'app2.js'
# ism = "Zokirkhon Kotibkhonov"
# tyil = 1999
# with open(faylnomi,'w') as file:
#     file.write(ism+'\n')
#     file.write(str(tyil)+'\n')

# with open(faylnomi,'w') as file:
#     file.write(ism+'\n')
#     file.write(str(tyil)+'\n')








###5
# faylnomi = 'app2.js'
# with open(faylnomi,'a') as file:
#     file.write("Khurshidbek Alisherov\n")
#     file.write("2001\n")






###6
import pickle
# talaba1 = {'ism':'zokirkhon','familya':'kotibkhonov','tyil':1999,'kurs':4}
# talaba2 = {'ism':'khurshidbek','familya':'alisherov','tyil':2001,'kurs':2}


# with open('talaba_Info.pickle','wb') as file:
#     pickle.dump(talaba1, file)
#     pickle.dump(talaba2, file)









###7
## o'qish uchun
fileName = "talaba_Info.pickle"
with open(fileName,'rb') as file:
    student1 = pickle.load(file)
    student2 = pickle.load(file)

print(student1)
print(student2)







































