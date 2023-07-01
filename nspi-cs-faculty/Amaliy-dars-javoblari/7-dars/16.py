Y=int(input('Yoshni kiriting: '))
if Y // 10 == 2:
    print('yigirma', end=' ')
elif Y // 10 == 3:
    print('o\'ttiz', end=' ')
elif Y // 10 == 4:
    print('qirq', end=' ')
elif Y // 10 == 5:
    print('ellik', end=' ')
elif Y // 10 == 6:
    print('oltmish', end=' ')
if Y % 10 == 1:
    print('bir', end=' ')
elif Y % 10 == 2:
    print('ikki', end=' ')
elif Y % 10 == 3:
    print('uch', end=' ')
elif Y % 10 == 4:
    print('to\'rt', end=' ')
elif Y % 10 == 5:
    print('besh', end=' ')
elif Y % 10 == 6:
    print('olti', end=' ')
elif Y % 10 == 7:
    print('yetti', end=' ')
elif Y % 10 == 8:
    print('sakkiz', end=' ')
elif Y % 10 == 9:
    print('to\'qqiz', end=' ')
if Y % 10 in [0,5,6,7,8,9]:
    print('yosh.')
elif Y % 10 == 1:
    print('yosh.')
elif Y % 10 in [2,3,4]:
    print('yosh.')