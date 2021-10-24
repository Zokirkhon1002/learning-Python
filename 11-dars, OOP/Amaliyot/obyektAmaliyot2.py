from obyektlarAmaliyot import mashina1,mashina2,mashina3,mashina4;

class AvtoSalon():
    def __init__(self,name,address,term_payment,sail,car1,car2):
        """Avtosalonga oid ma'lumotlarni to'ldiring"""
        self.nomi = name
        self.manzili = address
        self.muddatli_tolov = term_payment
        self.chegirma = sail
        self.mashinalar_soni = 0
        self.sotuvdagi_mashinalar = []
        self.sotilgan_mashinalar = []
        self.sotilgan_mashinalar_soni = 0
        self.car1 = car1
        self.car2 = car2
    
    def get_name(self):
        """Avto salonning nomini qaytaradi"""
        return self.nomi
    def get_address(self):
        """Avto salonning manzilini qaytaradi"""
        return self.manzili
    def get_term_payment(self):
        """Avto salonda muddatli to'lov borligi yoki yo'q ligini qaytaradi"""
        return self.muddatli_tolov
    def get_sail(self):
        """Avto salonda chegirma bor yoki yo'qligin qaytaradi"""
        return self.chegirma
    def get_cars_number(self):
        """Avto salondagi mashinalar sonini qaytaradi."""
        return self.mashinalar_soni
    def get_selling_cars(self):
        """Avto salondagi mashinalarni va ularning hususiyatlarini qaytaradi."""
        return [car.get_info() for car in self.sotuvdagi_mashinalar]
    def get_sold_cars(self):
        """Avto salondagi sotilgan mashinalarni va ularning hususiyatlarini qaytaradi."""
        return [car.get_info() for car in self.sotilgan_mashinalar]
    def get_sold_cars_numbers(self):
        """Avto salondan sotilgan mashinalar soni qaytaradi"""
        return self.sotilgan_mashinalar_soni;
    
    def get_info1(self):
        """Avtosalon haqida va mashinalar haqida ma'lumot beradi."""
        return (f"Avtosalon nomi: {self.nomi}. "
                f"\n Manzili: {self.manzili}. "
                f"\n Muddatli to'lov: {self.muddatli_tolov}. "
                f"\n Chegirma: {self.chegirma}. "
                f"\n Sotuvdagi mashinalar soni: {self.mashinalar_soni}. "
                f"\n Sotuvdagi mashinalar: {self.get_selling_cars()}. "
                f"\n Sotilgan mashinalar: {self.get_sold_cars()}. "
                f"\n Sotilgan mashinalar soni: {self.sotilgan_mashinalar_soni}. "
                f"\n car 1: {self.car1}. "
                f"\n car 2: {self.car2}. "
                )
    
    def add_car(self,car):
        """Avtosalonga mashina qo'shish"""
        self.sotuvdagi_mashinalar.append(car)
        self.mashinalar_soni += 1
        
    def remove_car(self,removeCar):
        """Avtosalondan o'chirish va sotilgan mashinalar ro'yxatiga qo'shish"""
        self.sotilgan_mashinalar.append(removeCar)
        self.mashinalar_soni -= 1
        self.sotilgan_mashinalar_soni +=1
        self.sotuvdagi_mashinalar.remove(removeCar)

salon1 = AvtoSalon("Universal","Namangan 31a-uy","bor","10%",mashina1.get_info(),mashina2.get_info())




# salon1.add_car(mashina1)
# salon1.add_car(mashina2)
# salon1.add_car(mashina3)
# salon1.add_car(mashina4)
# salon1.remove_car(mashina1)
print(salon1.get_info1())



# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False ]

# print(dir(AvtoSalon))
# print(see_methods(AvtoSalon))
# print(see_methods(salon1))
# print(salon1.__dict__)
# print(salon1.__dict__.keys())