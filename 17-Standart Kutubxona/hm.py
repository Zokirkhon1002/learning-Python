import datetime as d
import re


# yil = int(input("Yil: "))
# oy = int(input("Oy: "))
# kun = int(input("Kun: "))


# bugun = d.date.today()
# birthday = d.date(yil,oy,kun)
# result = bugun - birthday;
# print(f"Sizning tug'ilganingizga {result.days} kun bo'libdi")






# hozir = d.datetime.now();
# birthday = d.datetime(yil,oy,kun,12,00,00)
# farq = hozir - birthday;
# sekundlar = farq.seconds;
# minutlar = int(sekundlar/60)
# soatlar = int(minutlar/60)
# print(f"Sizning tug'ilganingizga {farq.days} kun {soatlar} soat bo'ldi")













# # telefon raqam
# andoza = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'


# while True:
#     telefon = input("Telefon raqam: ")
#     if re.match(andoza,telefon):
#         print("Telefon raqam qabul qilindi")
#         break
#     else:
#         print("Telefon raqamingiz qabul qilinmadi qaytadan harakat qiling!")






# # Web sahifa
matn = """
Assalom alaykum hurmatli do'stlar.
Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI
Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar 
va metodlarini tekshiruvchi dastur yozishni o'rganamiz. 
Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test
"""

web = re.findall('https://[^\s]+',matn)
print(web)