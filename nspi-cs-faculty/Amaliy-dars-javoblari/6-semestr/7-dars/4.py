n = int(input('n='))
oylar = {
    n in range(1,8,2) or n in range (8,13,2): '31 kun',
    n == 2: '28 yoki 29 kun',
    n==4 or n==6 or n==9 or n==11: '30 kun'
}
print(oylar.get(True, '1-12 oraliqda son kiriting'))