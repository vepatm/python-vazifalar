py_dictionary = {
    'boolean': 'mantiqiy qiymat',
    'integer': 'butun son',
    'float': 'o\'nlik son',
    'string': 'matn',
    'if': 'shartni tekshirish operatori',
    'for': 'biror amalni qayta-qayta bajarish sikli',
    'list': 'ro\'yxat',
    'dictionary': 'lug\'at',
    'else': 'if dagi shart bajarilmasa boshqa amalni bajarish uchun operator',
    'elif': 'if va else ning mantiqiy yig\'indisi'
}
for word,defintion in py_dictionary.items():
    print(f"{word.title()} - {defintion.capitalize()}")

countries_and_capitals  = {
    'aqsh': 'washington d.c.',
    'italiya': 'rim',
    'malaysziya': 'kuala-lumpur',
    'o\'zbekiston': 'toshkent',
    'rossiya': 'moskva',
    'turkmaniston': 'ashgabot'
}
print('Dunyo davlatlari:')
for country in countries_and_capitals.keys():
    print(country.upper())
print('Davlat poytaxtlari:')
for capital in countries_and_capitals.values():
    print(capital.title())

country = input('Qaysi davlatning poytaxtini bilishni istaysiz?: ').lower()
capital = countries_and_capitals[country]
if country in countries_and_capitals.keys():
    print(f"{country.upper()}ning poytaxti {capital.title()}")
else:
    print('Kechirasiz, bizda bu davlat haqida ma\'lumot yo\'q')

menu = {
    'osh': 20000,
    'shashlik': 9000,
    'somsa': 7000,
    'lag\'mon': 15000,
    'ayron': 2000,
    'lavash': 20000,
    'burger': 22000,
    'pitsa': 55000,
    'limonli choy': 5000,
    'non': 3000
}
buyurtma = []
print('3 ta taom buyurtma beringL:')
for i in range(3):
    taom = input(f"{i+1}-taom: ")
    buyurtma.append(taom)
for i in range(3):
    if buyurtma[i] in menu:
        print(f"{buyurtma[i].title()} {menu[buyurtma[i]]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma[i]} yo'q")