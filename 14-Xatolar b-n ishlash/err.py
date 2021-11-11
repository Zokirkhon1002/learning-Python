### 1
# while True:
#     try:
#         yosh = int(input("Yoshingizni kiriting: "))
#     except:
#         print("Siz butun son kiritmadingiz")
#         continue;
#     else:
#         break;

# print(f"Siz {2021-yosh} yilda tug'ilgansiz")



### 2
### ZeroDivisionError
# x,y=5,10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print(f"{y} ni 0 ga bo'lib bo'lmaydi")







### 3
### IndexError
# mevalar = ['olma','anor','anjir','uzum']

# try:
#     print(mevalar[9])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta mevalar bor xolos.")




### 4
### KeyError
# user = {
#     "username":"Zokirkhon1002",
#     "status":"Student",
#     "email":"zokirxonkotibxanov@gmail.com",
#     "phone": "01080891816"
# }
# while True:
#     key = input("Enter a key: ").lower();
#     try:
#         print(f"Foydalanuvchi: {user[key]}")
#     except KeyError:
#         print(f"{key} nomli kalit yo'q.")
#         continue
#     else:
#         break





### 5
### FileNotFoundError

# filename = "data.txt"
# try:
#     with open(filename) as f:
#         text = f.read()
# except FileNotFoundError:
#     print(f"{filename} mavjud emas.")




### 6
### FileNotFoundError
# import json
# files = ['talaba1.json','talaba5.json','talaba2.json','talaba3.json','talaba4.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)
#     except FileNotFoundError:
#         # print(f"{filename} nomli fayl mavjud emas")
#         pass
#     else:
#         print(talaba['ism'])
#         # print(talaba['yosh'])
#         # print(talaba['fakultet'])







### 7
### ValueError
while True:
    n = input("Butun son kiriting: ")
    try:
        n = int(n)
        x = 20/n
    except ValueError: # if user doesn't enter int; 
        print("Butun son kiritmadingiz.")
        continue
    except ZeroDivisionError: # if user divides 0;
        print("0 ga bo'lib bo'lmaydi.")
        continue
    else:
        break;
print(f"n: {n}")
print(f"x: {x}")

