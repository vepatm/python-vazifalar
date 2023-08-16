#1
buyurtma = []
savol = "Mahsulot buyurtma qilmoqchimisiz (ha/yo'q)?\n>>>"
ishora = True
n=1
while ishora:
    qiymat = input(savol)
    if qiymat == "yo'q":
        ishora = False
    else:
        mahsulot = input(f"{n}-mahsulot nomini kiriting: ")
        buyurtma.append(mahsulot)
        n+=1
print('Buyurtma qilingan mahsulotlar: ', end='')
for mahsulot in buyurtma:
    print(mahsulot, end=' ')

#2
e_bozor = {}
ishora = True
m=1
while ishora:
    qiymat = input("e-bozor uchun mahsulot kiritmoqchimisiz (ha/yo'q): ")
    if qiymat == "yo'q":
        break
    else:
        mahsulot = input(f"{m}-mahsulotni kiriting: ")
        narh = float(input(f"{mahsulot.capitalize()}ning narhini kiriting (necha so'm): "))
        e_bozor[mahsulot] = narh
        m+=1
print("Bozordagi mahsulotlar narxi:")
for m, n in e_bozor.items():
    print(f"{m.capitalize()} - {n} so'm")

print(buyurtma)
print(e_bozor)

#3
e_bozor = {}
ishora = True
m=1
while ishora:
    qiymat = input("e-bozor uchun mahsulot kiritmoqchimisiz (ha/yo'q): ")
    if qiymat == "yo'q":
        break
    else:
        mahsulot = input(f"{m}-mahsulotni kiriting: ")
        narh = float(input(f"{mahsulot.capitalize()}ning narhini kiriting (necha so'm): "))
        e_bozor[mahsulot] = narh
        m+=1
print("Bozordagi mahsulotlar narxi:")
for m, n in e_bozor.items():
    print(f"{m.capitalize()} - {n} so'm")

buyurtma = []
savol = "Mahsulot buyurtma qilmoqchimisiz (ha/yo'q)?\n>>>"
ishora = True
n=1
while ishora:
    qiymat = input(savol)
    if qiymat == "yo'q":
        ishora = False
    else:
        mahsulot = input(f"{n}-mahsulot nomini kiriting: ")
        if mahsulot in e_bozor.keys():
            print(f"{mahsulot.title()}ning narhi {e_bozor[mahsulot]} so'm")
        else:
            print("Bizda bu mahsulot mavjud emas")
        n+=1