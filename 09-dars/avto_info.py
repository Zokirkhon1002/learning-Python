def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None):
    """Mashina ma'lumotlarini qaytarib beruvchi funksiya"""
    avto = {"kompaniya": kompaniya,
            "model": model,
            "rang": rangi,
            "karobka": karobka,
            "yili": yili,
            "narhi":narhi}
    return avto;


def avto_kirit():
    print("Saytimizdagi avtolar ro'yxatini shakllantiramiz")
    avtolar = [];
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting", end=" ")
        kompaniya=input("Ishlab chiqaruvchi: ")
        model=input("Modeli: ")
        rangi=input("Rangi: ")
        karobka=input("Karobka: ")
        yili=input("Ishlab chiqarilgan yili: ")
        narhi=input("Narhi: ")
        # Foydalanuvchi kiritgan ma'lumotlardan avto_info yordamida
        # lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
        avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili, narhi))
        # Yana avto qo'shish-qo'shmaslikni so'raymiz
        javob = input("yana avto qo'shasizmi? (yes/no): ")
        if javob == 'no':
            break



def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rang'].title()}, {avto_info['model'].title()}, {avto_info['karobka']} karobka. Narhi: {avto_info['narhi']}$")