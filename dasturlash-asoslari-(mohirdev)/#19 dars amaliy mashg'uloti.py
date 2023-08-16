f_ism = input("Ismingizni kiriting: ")
f_yosh = int(input("Yoshingizni kiriting: "))
def tugulgan_yilni_hisobla(ism, yosh):
    """Ism va yoshni aniqlovchi funksiya"""
    t_yil = 2023 - yosh
    print(f"{ism.title()}, siz {t_yil}-yilda tug'ilgansiz")
tugulgan_yilni_hisobla(f_ism, f_yosh)


def kv_va_kub_hisobla():
    """2 ta son so'rab shu sonlarning kubi va
    kvadratini chiqaruvchi dastur"""
    f_son = float(input("Istalgan bitta son kiriting: "))
    print(f"{f_son} ning kvadrati: {f_son**2}\n"
          f"{f_son} ning kubi: {f_son**3}")
kv_va_kub_hisobla()

def juft_yoki_toq():
    """1 ta son so'rab shu sonning juft yoki toqligini
    aniqlovchi dastur"""
    son = int(input("Istalgan butun son kiriting: "))
    if son%2==0:
        print("Kiritilgan son juft")
    else:
        print("Kiritilgan son toq")
juft_yoki_toq()

f_son1 = float(input("1-sonni kiriting: "))
f_son2 = float(input("2- sonni kriting: "))
def taqqosla(son1,son2):
    """2 ta sonni taqqoslovchi funksiya"""
    if son1 > son2:
        print(f"{son1} > {son2}")
    elif son1 < son2:
        print(f"{son1} < {son2}")
    else:
        print(f"{son1} = {son2}")
taqqosla(f_son1,f_son2)

x = int(input("Asosni kiriting: "))
y = int(input("Darajani kiriting: "))
def daraja_hisobla(asos, daraja=2):
    """Darajani hisoblovchi funksiya"""
    print(f"{asos}^{daraja} = {asos**daraja}")
daraja_hisobla(x,y)

f_son = int(input("Istalgan butun son kirting: "))
def bolinish_alomatlari(son):
    """10 gacha bo'linish alomatlarini tekshiruvchi funksiya"""
    for i in range(2, 11):
        if son % i == 0:
            print(f"{son} {i} ga qoldiqsiz bo'linadi")
bolinish_alomatlari()