N=int(input('Miqdor: '))
if N // 10 == 1:
    if N == 10:
        print('o\'nta ilmiy ish.')
    elif N == 11:
        print('o\'n bitta ilmiy ish.')
    elif N == 12:
        print('o\'n ikkita ilmiy ish.')
    elif N == 13:
        print('o\'n uchta ilmiy ish.')
    elif N == 14:
        print('o\'n to\'rtta ilmiy ish.')
    elif N == 15:
        print('o\'n beshta ilmiy ish.')
    elif N == 16:
        print('o\'n oltita ilmiy ish.')
    elif N == 17:
        print('o\'n yettita ilmiy ish.')
    elif N == 18:
        print('o\'n sakkizta ilmiy ish.')
    elif N == 19:
        print('o\'n to\'qqizta ilmiy ish.')
else:
    if N // 10 == 2:
        print('yigirma', end=' ')
    elif N // 10 == 3:
        print('o\'ttiz', end=' ')
    elif N // 10 == 4:
        print('qirq', end=' ')
    if N % 10 == 1:
        print('bir', end=' ')
    elif N % 10 == 2:
        print('ikki', end=' ')
    elif N % 10 == 3:
        print('uch', end=' ')
    elif N % 10 == 4:
        print('to\'rt', end=' ')
    elif N % 10 == 5:
        print('besh', end=' ')
    elif N % 10 == 6:
        print('olti', end=' ')
    elif N % 10 == 7:
        print('yetti', end=' ')
    elif N % 10 == 8:
        print('sakkiz', end=' ')
    elif N % 10 == 9:
        print('to\'qqiz', end=' ')
    if N % 10 in [0,5,6,7,8,9]:
        print('ilmiy ish.')
    elif N % 10 == 1:
        print('ilmiy ish.')
    elif N % 10 in [2,3,4]:
        print('ilmiy ish.')