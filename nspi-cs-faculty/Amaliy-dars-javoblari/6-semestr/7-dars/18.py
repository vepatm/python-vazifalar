n = int(input('n='))
yuzliklar = {
    1: 'bir yuz',
    2: 'ikki yuz',
    3: 'uch yuz',
    4: 'to\'rt yuz',
    5: 'besh yuz',
    6: 'olti yuz',
    7: 'yetti yuz',
    8: 'sakkiz yuz',
    9: 'to\'qqiz yuz'
}

onliklar = {
    1: 'o\'n',
    2: 'yigitma',
    3: 'o\'ttiz',
    4: 'qirq',
    5: 'ellik',
    6: 'oltmish',
    7: 'yetmish',
    8: 'sakson',
    9: 'to\'qson'
}

birliklar = {
    1: 'bir',
    2: 'ikki',
    3: 'uch',
    4: 'to\'rt',
    5: 'besh',
    6: 'olti',
    7: 'yetti',
    8: 'sakkiz',
    9: 'to\'qqiz'
}

f1 = n // 100
f2 = (n // 10) % 10
f3 = n % 10
print(yuzliklar.get(f1), onliklar.get(f2), birliklar.get(f3))