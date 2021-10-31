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
    def __init__(self,ism,familya,passport,tyil,idraqam,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism,familya,passport,tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
    
    def get_id(self):
        return self.idraqam
    def get_bosqich(self):
        return self.bosqich
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familya}. "
        info += f"\n{self.get_bosqich()}-bosqich. ID raqam: {self.get_id()}"
        info += f"\nManzil: {self.manzil}."
        return info;
    
    def __repr__(self):
        """Shunisi ko'proq tavsiya qilinadi"""
        return f"Shaxs: {self.ism} {self.familya} {self.passport} {self.tyil} {self.idraqam}"
    def __lt__(self,another):
        return self.tyil > another.tyil
    def __eq__(self,another):
        return self.tyil == another.tyil
    def __le__(self,another):
        return self.tyil <= another.tyil

class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
        
    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyat, {self.tuman}, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil

class Fan:
    """Fan lar haqidagi ma'lumotlarni to'ldiring"""
    def __init__(self,nomi):
        """Fan haqidagi ma'lumotni to'ldiring"""
        self.nomi = nomi
        self.students = []
        self.students_number = 0
    def get_fan(self):
        """Fanni ko'rish"""
        fan = f"Fan nomi: {self.nomi},"
        return fan;
    def add_student(self,talaba):
        if isinstance(talaba,Talaba):
            self.students.append(talaba)
            self.students_number += 1;
    def remove_student(self,c):
        """ '-' belgisin orqali talabani o'chirishingiz mumkin"""
        if c == "-":
            self.students.pop()
        else:
            print("Noto'g'ri belgi kiritdingiz")
    def __repr__(self):
        """ Shunisi ko'proq tavsiya qilinadi"""
        return (f"Fan nomi: {self.nomi}"
                f"Studentlar soni: {self.students_number}"
                f"\nStudentlar ro'yxati: {[c for c in self.students]}")
    def __eq__(self, y):
        return self.students_number == y.students_number

    def __lt__(self, y):
        return self.students_number < y.students_number

    def __le__(self, y):
        return self.students_number <= y.students_number
    def __getitem__(self,index):
        return self.students[index]
    def __setitem__(self,index,newValue):
        self.students[index] = newValue;
    def __call__(self,*newValues):
        """we call like Functions"""
        if newValues:
            for i in newValues:
                self.students.append(i)
        else:
            return [i for i in self.students]
            


talaba1_manzil =Manzil(17,"Soli Adashev","Namangan Shahar","Namangan").get_manzil()
talaba2_manzil =Manzil(11,"Oromgoh","Namangan Shahar","Namangan").get_manzil()
talaba3_manzil =Manzil(15,"Taxta ko'prik","Namangan Shahar","Namangan").get_manzil()
talaba1 = Talaba("Zokirkhon","Kotibkhonov","ff112233",1999,180421,talaba1_manzil)
talaba2 = Talaba("Khurshidbek","Alisherov","ff332211",2000,185421,talaba1_manzil)
talaba3 = Talaba("Sayfullokhon","Ulukhodjaev","ff5566777",2000,1854895,talaba3_manzil)

Frontend = Fan("JavaScript")
Frontend.add_student(talaba1)
Frontend.add_student(talaba2)
Frontend.add_student(talaba3)


print(talaba1.get_info())