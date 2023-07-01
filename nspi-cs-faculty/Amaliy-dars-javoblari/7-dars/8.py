d = int(input('Kun raqamini kiriting = '))
m = int(input('Oy raqamini kiriting = '))
oylar = {
    1: 'yanvar',
    2: 'fevral',
    3: 'mart',
    4: 'Aprel',
    5: 'May',
    6: 'Iyun',
    7: 'Iyul',
    8: 'Avgust',
    9: 'Sentyabr',
    10: 'Oktyabr',
    11: 'Noyabr',
    12: 'Dekabr'
}
print(f"{d}-{oylar.get(m)}")