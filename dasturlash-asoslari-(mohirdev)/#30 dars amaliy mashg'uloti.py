class Talaba:
    def __init__(self,ism,familiya,id):
        self.ism = ism
        self.familiya = familiya
        self.id = id
        self.bosqich = 1
        self.fanlar = []
    
    def fanga_yozil(self,fan):
        self.fanlar.append(fan)

    def remove_fan(self,fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            return "Siz bu fanga yozilmagansiz"
    
    def get_fanlar(self):
        return self.fanlar

class Fan:
    def __init__(self,fan):
        self.fan = fan
    
    def get_name(self):
        return self.fan


fan1 = Fan('Python')
fan2 = Fan('Web dizayn')
fan3 = Fan('Elementar matematika')    
talaba1 = Talaba('Vepa','Kurbanklichev','KA123456')
talaba1.fanga_yozil(fan1.get_name())
talaba1.fanga_yozil(fan2.get_name())
talaba1.fanga_yozil(fan3.get_name())
print(talaba1.get_fanlar())