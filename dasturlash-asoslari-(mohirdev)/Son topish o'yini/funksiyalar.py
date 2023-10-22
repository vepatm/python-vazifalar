import random as r
def son_top(n):
    pc_tahmini = r.randint(1,n)
    print(f"1 dan {n} gacha son o'yladim topa olasizmi?:")
    urinishlarim = 0
    while True:
        tahminim = int(input('>>'))
        urinishlarim += 1
        if tahminim > pc_tahmini:
            print("Xato men o'ylagan son bundan kichikroq. Yana harakat qiling:")
        elif tahminim < pc_tahmini:
            print("Xato men o'ylagan son bundan kattaroq. Yana harakat qiling:")
        else:
            break
    print(f"{pc_tahmini} sonini o'ylagan edim. {urinishlarim} ta tahmin bilan topdingiz. Tabriklayman!!")   
    return urinishlarim
# son_top(100)

def son_top_pc(n):
    print(f"1 dan {n} gacha son o'ylang. Men topaman")
    input("Istalgan tugmani bosing")
    pc_urinishlari = 0
    min = 1
    max = n
    while True:
        if max != min:
            pc_tahmini = r.randint(1,n)
        else:
            pc_tahmini = max
        tekshirish_natijasi = input(f"Siz {pc_tahmini} sonini o'yladingiz, to'g'ri (T), "
                                    f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)??")
        pc_urinishlari += 1
        if tekshirish_natijasi.upper() == 'T':
            print(f"Soningizni {pc_urinishlari} ta tahmin bilan topdim")
            break
        elif tekshirish_natijasi == '+':
            max = pc_tahmini + 1
        elif tekshirish_natijasi == '-':
            max = pc_tahmini - 1
    return pc_urinishlari
# son_top_pc(10)
def play(n):
    while True:
        me = son_top(n)
        print()
        pc = son_top_pc(n)
        print()
        if me<pc:
            print("Siz g'alaba qozondingiz! Tabriklayman!")
        elif me>pc:
            print("SIz mag'lub bo'ldingiz :(")
        else:
            print("Durrang! Do'stlik ga'alaba qozondi!")
        print()
        print(f"Siz {me} - {pc} Men")
        savol = input("Yana o'ynashni xohlaysizmi? Ha (1) / Yo'q (0)")
        if savol == '0':
            break
# play(10)