# 16-dars mashg'uloti
buxoriy = {
    'ism': 'abu abdulloh muhammad ibn ismoil',
    'tyil': 810,
    'vyil': 870,
    'tjoy': 'buxoro',
    'asarlar': ['Al-jome\' as-sahih', 'Al-adab al-mufrad', 'At-tarix al-kabir', 'At-tarix as-sag\'ir']
}
qodiriy = {
    'ism': 'abdulla qodiriy',
    'tyil': 1894,
    'vyil': 1938,
    'tjoy': 'toshkent',
    'asarlar': ['O\'tkan kunlar', 'Mehrobdan Chayon', 'Obid ketmon']
}
vohidov = {
    'ism': 'erkin vohidov',
    'tyil': 1936,
    'vyil': 2016,
    'tjoy': 'farg\'ona',
    'asarlar': ['Tong nafasi', 'Qo\'shiqlarim sizga', 'O\'zbegim', 'Qiziquvchan Matmusa']
}
navoiy = {
    'ism': 'alisher navoiy',
    'tyil': 1441,
    'vyil': 1501,
    'tjoy': 'buxoro',
    'asarlar': ['Lison ut-Tayr', 'Xamsa', 'Mahbub al-Qulub', 'Munojot']
}
t_shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
for shaxs in t_shaxslar:
    print(f"{shaxs['ism'].title()} {shaxs['tyil']}-yilda "
          f"{shaxs['tjoy'].capitalize()}da tavallud topgan. "
          f"{shaxs['vyil']-shaxs['tyil']} yil umr ko'rgan.")

for shaxs in t_shaxslar:
    print(f"{shaxs['ism'].title()}ning mashhur asarlari:")
    for asar in shaxs['asarlar']:
        print(asar)
    print()

seyitnazar = {
    'ism': 'seyitnazar',
    'kinolar': []
}
miesser = {
    'ism': 'miesser',
    'kinolar': []
}
sapa = {
    'ism': 'sapa',
    'kinolar': []
}
yorqinoy = {
    'ism': 'yorqinoy',
    'kinolar': []
}
oila_azolari = [seyitnazar, miesser, sapa, yorqinoy]
for azo in oila_azolari:
    print(f"{azo['ism'].title()}, sevimli 3 ta kinoingizni kiriting:")
    for i in range(3):
        kino = input(f"{i+1}-kinoingizni kiriting: ")
        azo['kinolar'].append(kino)
    print()
for azo in oila_azolari:
    print(f"{azo['ism'].title()}ning sevimli kinolari:")
    for kino in azo['kinolar']:
        print(kino.capitalize())
    print()

davlatlar = {
    'uzb': {
        'nom': 'O\'zbekiston',
        'poytaxt': 'toshkent',
        'hudud': 448978,
        'aholi': 33*(10**6),
        'pulb': 'so\'m'
    },
    'rus': {
        'nom': 'Rossiya',
        'poytaxt': 'moskva',
        'hudud': 17098246,
        'aholi': 144*(10**6),
        'pulb': 'rubl'
    },
    'usa': {
        'nom': 'AQSH',
        'poytaxt': 'vashington',
        'hudud': 9631418,
        'aholi': 327*(10**6),
        'pulb': 'dollar'
    },
    'mlz': {
        'nom': 'Malayziya',
        'poytaxt': 'kuala-lumpur',
        'hudud': 329750,
        'aholi': 25*(10**6),
        'pulb': 'rinngit'
    }
}
for info in davlatlar.values():
    print(f"{info['nom']}ning poytaxti {info['poytaxt']}\n"
          f"Hududi: {info['hudud']} kv.km\n"
          f"Aholisi: {info['aholi']}\n"
          f"Pul birligi: {info['pulb']}\n\n")

davlat = input('Davlat nomini kiriting: ')
k = 0
for info in davlatlar.values():
    if davlat == info['nom']:
        k =+ 1
        nom = info['nom']
        poytaxt = info['poytaxt']
        hudud = info['hudud']
        aholi = info['aholi']
        pulb = info['pulb']
if k==1:
    print(f"\n{nom}ning poytaxti {poytaxt}n"
          f"Hududi: {hudud} kv.km\n"
          f"Aholisi: {aholi}\n"
          f"Pul birligi: {pulb}\n\n")
else:
    print('\nBizda bu davlat haqida ma\'lumot mavjud emas')