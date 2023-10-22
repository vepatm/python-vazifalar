class Avto:
    def __init__(self,rusum,rang,korobka):
        """Avtomilning rusumini rangini korobkasini kiritish uchun klass"""
        self.rusum = rusum
        self.rang = rang
        self.korobka = korobka
        self.narh = 0
        self.kilometr = 0
    
    def set_narh(self,narh):
        """Avtomobilning narhini kirituvchi method"""
        self.narh = narh
    
    def update_narh(self,qoshilgan_narh):
        """Avtomobilning joriy narhni o'zgartiruvchi method"""
        self.narh += qoshilgan_narh
    
    def set_kilometr(self,kilometr):
        """Avtomobilning yurgan masofasini kirituvchi method"""
        self.kilometr = kilometr
    
    def update_kilometr(self,qoshilgan_kilometr):
        """Avtomobilning yurgan masofasini o'zgartiruvchi dastur"""
        self.kilometr += qoshilgan_kilometr

    def get_info(self):
        """Avtomobil haqidagi ma'lumotlarni qaytaruvchi method"""
        if not self.narh:
            self.narh = 'NOMA\'LUM'
        if not self.kilometr:
            self.kilometr = 'YURMAGAN'
        return f"Rusum: {self.rusum.upper()}\nRang: {self.rang.upper()}\nKorobka: {self.korobka.upper()}\nNarhi: {self.narh}$\nYurgan masofasi: {self.kilometr}"

class Avtosalon:
    def __init__(self,nom,manzil):
        """Avtosalon haqida ma'lumot kiritish uchun klass"""
        self.nom = nom
        self.manzil = manzil
        self.sotuvdagi_avtolar = []
        self.avtolar_soni = 0
    
    def add_avto(self,avto):
        """Avtosalonga avtomobil qo'shish"""
        self.sotuvdagi_avtolar.append(avto)
        self.avtolar_soni += 1
    def get_avtos(self):
        """Sotuvdagi avtomobillar haqida ma'lumot"""
        return [avto.get_info() for avto in self.sotuvdagi_avtolar]

    def get_name(self):
        return self.nom.upper()
    
    def get_address(self):
        return self.manzil.upper()

avto1 = Avto('malibu','qora','avtomat')
avto1.set_narh(38000)
avto1.set_kilometr(5000)

avto2 = Avto('gentra','oq','mexanika')
avto2.set_narh(18000)

salon = Avtosalon('AvtoSavda (AS)','Nukus ko\'chasi 27-uy')
salon.add_avto(avto1)
salon.add_avto(avto2)
print(f"{salon.get_address()} da joylashgan {salon.get_name()} \
mashinalar haqida ma'lumot:\
\n{salon.get_avtos()}")

print(dir(Avto))
print(dir(Avtosalon))
print(avto1.__dict__)