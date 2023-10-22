class Shaxs:
    """Shaxslar haqida ma'lumot"""
    __odamlar_soni = 0
    def __init__(self,ism,familiya,passport,tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        Shaxs.__odamlar_soni += 1
    
    @classmethod
    def get_odamlar_soni(cls):
        return cls.__odamlar_soni

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport: {self.passport}, {self.tyil}-yilda tug'ilgan"
        return info
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil


class Talaba(Shaxs): # Shaxs - super klass, Talaba - voris klass
    """Talaba klassi"""
    __talabalar_soni = 0
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        """Talabaning xusuiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.manzil = manzil
        self.bosqich = 1
        Talaba.__talabalar_soni += 1
    
    @classmethod
    def get_talabalar_soni(cls):
        return cls.__talabalar_soni

    def get_id(self):
        """ Talabaning ID raqami"""
        return self.idraqam
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.get_id()}"
        return info

talaba1 = Talaba("Vepa","Kurbanklichev","KA123456",2002,"AB123456",'Okkamish')
talaba1 = Talaba("Vepa","Kurbanklichev","KA123456",2002,"AB123456",'Okkamish')
talaba1 = Talaba("Vepa","Kurbanklichev","KA123456",2002,"AB123456",'Okkamish')
shaxs1 = Shaxs('Vepa','Kurbanklichev','KA123456',2002)
print(Talaba.get_talabalar_soni())
print(Shaxs.get_odamlar_soni())