
### Home work
### Amaliyot

class User:
    def __init__(self,username,name,surname,email,number,birthdate,address,nationality,status):
        self.username = username
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.email = email
        self.number = number
        self.address = address    
        self.nationality = nationality
        self.status = status
    
    def get_userName(self):
        return self.username
    
    def get_name(self):
        return self.name
    
    def get_surname(self):
        return self.surname
    
    def get_fullName(self):
        return f"{self.name} {self.surname}"
    
    def get_age(self,year_now):
        return year_now - self.birthdate
    
    def get_email(self):
        return self.email
    
    def get_number(self):
        return self.number
    
    def get_address(self,country,city,street,home):
        return (f"Address: {self.address}"
                f"\nCountry: {country}"
                f"\nCity: {city}"
                f"\nStreet: {street}"
                f"\nHome: {home}")
    
    def get_nationality(self):
        return self.nationality
    
    def get_status(self):
        return self.status
    
    def get_info(self):
        return (f"name: {self.get_name()}"
                f"\nsurname: {self.surname}"
                f"\nusername: {self.username}"
                f"\nage: {self.get_age(2021)}"
                f"\nemail: {self.email}"
                f"\nnumber: {self.number}"
                f"\naddress: {self.address}"
                f"\nnationality: {self.nationality}"
                f"\nstatus: {self.status}")


user1 = User("Zokirkhon1002","Zokirkhon","Kotibkhonov","zokirxonkotibxanov@gmail","+821080891816",1999,"G'isht ko'prik","Uzbek","single")



print(user1.get_info())
print(user1.get_fullName())
print(user1.get_userName())
print(user1.get_status())