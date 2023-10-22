class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def __repr__(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport: {self.passport}, {self.tyil}-yilda tug'ilgan"
        return info
    

        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil


class Talaba(Shaxs): # Shaxs - super klass, Talaba - voris klass
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        """Talabaning xusuiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.manzil = manzil
        self.bosqich = 1
    
    def get_id(self):
        """ Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
       
    def __repr__(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich talabasi. ID raqami: {self.get_id()}"
        return info
    
    def __call__(self,y):
        """Talabaning bosqichini kiriting"""
        self.bosqich = y
    
    def __gt__(self,y):
        if isinstance(y,Talaba):
            return self.bosqich > y.bosqich
    
    def __eq__(self,y):
        if isinstance(y,Talaba):
            return self.bosqich == y.bosqich

class Fan:
    def __init__(self,name):
        self.name = name
        self.talabalar = []
    
    def add_talaba(self,talaba):
        self.talabalar.append(talaba)
    
    def remove_talaba(self,talaba):
        self.talabalar.remove(talaba)
    
    def __getitem__(self,i):
        return self.talabalar[i]
    
    def __setitem__(self,i,qiymat):
        if isinstance(qiymat,Talaba):
            self.talabalar[i] = qiymat
    
    def __add__(self,y):
        if isinstance(y,Talaba):
            self.add_talaba(y)
    
    def __sub__(self,y):
        if isinstance(y,Talaba):
            self.remove_talaba(y)
            
    
    def __len__(self):
        return len(self.talabalar)
    
    def __repr__(self):
        return self.name
    
    def __call__(self,*qiymat):
        if qiymat:
            for talaba in qiymat:
                if isinstance(talaba,Talaba):
                    self.add_talaba(talaba)
        return self.talabalar

shaxs1 = Shaxs('Vepa','Kurbanklichev','KA123456',2002)
print(shaxs1)

talaba1 = Talaba('Vepa','Kurbanklichev','KA123456',2002,12345678,'Nukus')
talaba2 = Talaba('Barchinoy','Kurbanklicheva','AD123456',2005,123456,'Urganch')
talaba1(4)
print(talaba1>talaba2)

fan1 = Fan('Elementar matematika')
fan1 + talaba1
fan1 + talaba2
fan1 - talaba1
print(fan1)
print(fan1(talaba1))