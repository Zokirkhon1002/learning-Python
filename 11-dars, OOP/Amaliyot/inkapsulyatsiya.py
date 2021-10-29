class Shaxs():
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familya,passport,tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familya = familya
        self.passport = passport
        self.tyil = tyil
    def get_info(self):
        """Shaxs haqida ma'lumot qaytaradi."""
        info = f"{self.ism} {self.familya}. "
        info += f"Passport: {self.passport}, {self.tyil}-yilda tug'ilgan"
        return info;
    def get_age(self,hozirgi_yil):
        """Shaxsning yoshini qaytaruvchi method."""
        return hozirgi_yil - self.tyil

###super class1
class Talaba(Shaxs):
    """Talaba klasi"""
    __num_shaxs = 0
    def __init__(self,ism,familya,passport,tyil,idraqam,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism,familya,passport,tyil)
        self.idraqam = idraqam
        self.__bosqich = 1
        self.manzil = manzil
        self.__fanlar = []
        self.__fanlar_soni = 0
        Talaba.__num_shaxs += 1
        
    @classmethod
    def get_num_shaxs(cls):
        return cls.__num_shaxs
    
    def add_bosqich(self):
        self.__bosqich += 1
    
    def get_id(self):
        return self.idraqam
    
    def get_bosqich(self):
        return self.__bosqich
    
    
    def fanga_yozil(self,yozilgan_fanlar):
        self.__fanlar.append(yozilgan_fanlar)
        self.__fanlar_soni += 1
    
    def get_fanlar(self):
        return self.__fanlar
    
    def get_fanlar_soni(self):
        return self.__fanlar_soni
    
    def remove_fan(self,removingFan):
        if removingFan in self.fanlar:
            self.fanlar.remove(removingFan)
            self.fanlar_soni -= 1
        else:
            return f"Uzr siz {removingFan} ga yozilmagansiz"
    
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familya}. "
        info += f"\n{self.get_bosqich()}-bosqich. \nID raqam: {self.get_id()}"
        info += f"\nManzil: {self.manzil}."
        info += f"\nFanlar: {self.get_fanlar()}"
        info += f"\nFanlar soni: {self.get_fanlar_soni()}"
        return info;

talaba1 = Talaba("Zokirkhon","Kotibkhonov","123456789",1995,"123456789","Namangan")
print(talaba1.get_info())
talaba1.fanga_yozil("WEB")
talaba1.fanga_yozil("AI")
talaba1.add_bosqich()
print(talaba1.get_info())
print(talaba1.get_num_shaxs())
