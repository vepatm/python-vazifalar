otam = {
    'ism': 'Seyitnazar',
    't_yil': 1976,
    't_joy': 'Qoraqolpog\'iston Respublikasi',
    's_taom': 'osh'
}
onam = {
    'ism': 'Miesser',
    't_yil': 1984,
    't_joy': 'Qoraqolpog\'iston Respublikasi',
    's_taom': 'beshbarmoq'
}
ukam = {
    'ism': 'Sapa',
    't_yil': 2002,
    't_joy': 'Qoraqolpog\'iston Respublikasi',
    's_taom': 'osh'
}
print(f"Otaming ismi {otam['ism']}, {otam['t_yil']}-yil {otam['t_joy']}da tug'ilgan")
print(f"Onaming ismi {onam['ism']}, {onam['t_yil']}-yil {onam['t_joy']}da tug'ilgan")
print(f"Ukaming ismi {ukam['ism']}, {ukam['t_yil']}-yil {ukam['t_joy']}da tug'ilgan")

print(f"{otam['ism']}ning sevimli taomi {otam['s_taom']}")
print(f"{onam['ism']}ning sevimli taomi {onam['s_taom']}")
print(f"{ukam['ism']}ning sevimli taomi {ukam['s_taom']}")

python_lugat = {
    'integer': 'butun son',
    'float': 'haqiyqiy son',
    'string': 'qator',
    'if': 'agar',
    'else': 'bo\'lmasa',
    'elif': 'else-if ning qisqartmasi',
    'for': 'uchun',
    'range': 'oraliq',
    'input': 'kiritish',
    'get': 'olish'
}

k_soz = input('Kalit so\'z kiriting: ')
if k_soz in python_lugat:
    print(f"{k_soz} so'zi {python_lugat[k_soz]} deb tarjima qilinadi")
else:
    print('Bunday so\'z mavjud emas')