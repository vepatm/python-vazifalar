n = int(input('n='))
fasllar = {
    1 <= n <= 2: 'Qish',
    3 <= n <= 5: 'Bahor',
    6 <= n <= 8: 'Yoz',
    9 <= n <= 11: 'Kuz',
    n == 12: 'Qish'
}
print(fasllar.get(True, 'Oy raqami noto\'g\'ri kiritilgan'))