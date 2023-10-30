n = int(input('n='))
h_kunlari = {
    1: 'Dushanba',
    2: 'Seshanba',
    3: 'Chorshanba',
    4: 'Payshanba',
    5: 'Juma',
    6: 'Shanba',
    7: 'Yakshanba'
}
print(h_kunlari.get(n, 'Bunday hafta kuni yoq'))