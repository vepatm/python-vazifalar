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
if m in [1,3,5,7,8,10] and d==31:
    d = 0
    m = m + 1
if m in [4,6,9,11] and d==30:
    d = 0
    m = m + 1
if m==12:
    d = 0
    m = 1
print(f"{d+1}-{oylar.get(m)}")