import re
from english_words import words

word1 = "cat"
word2 = "dog"
word3 = "book"
word4 = "boosk"

# andoza = "^b..k$"
# print(re.match(andoza, word1))
# print(re.match(andoza, word2))
# print(re.match(andoza, word3))
# print(re.match(andoza, word4))




# andoza = "^b..k$"
# andoza1 = "^m..p$"
# andoza2 = "^c.....l$"
# matches = []
# for word in words:
#     if re.match(andoza, word):
#         matches.append(word)
#     elif re.match(andoza1, word):
#         matches.append(word)
#     elif re.match(andoza2, word):
#         matches.append(word)

# print(matches)




# matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
# Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
# 👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
# 👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """

# andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
# email = re.findall(andoza,matn)
# print(email)






# Kuchli parolni tekshirish
# Quyidagi andoza ham ihateregex.io sahifasidan olindi
andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
msg = "Yangi parol kiriting"
msg += '(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, '
msg += '1 ta son va 1 ta maxsus belgi boʻlishi kerak): '

while True:
    password = input(msg)
    if re.match(andoza,password):
        print("Maxfiy so'z qabul qilindi")
        break
    else:
        print("Maxfiy so'z talabga javob bermadi")