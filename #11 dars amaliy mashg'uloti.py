son = int(input('Juft son kiriting\n>>>'))
if son % 2 == 0:
    print('Rahmat!')
else:
    print('Bu son juft emas.')

yosh = int(input('Yoshingiz nechida?\n>>>'))
if yosh <= 4 or yosh >= 60:
    narh = 0
elif yosh <= 18:
    narh = 10000
else:
    narh = 20000
print(f"Sizga kirish {narh} so'm")

a = float(input('Birinchi sonni kiriting: '))
b = float(input('Ikkinchi sonni kiriting: '))
if a>b:
    print(f"{a}>{b}")
elif a<b:
    print(f"{a}<{b}")
else:
    print(f"{a}={b}")

mahsulotlar = ['kartoshka', 'piyoz', 'sabzi', 'makaron', 'olma', 'uzum']
savat = []
for n in range(5):
    savat.append(input(f"Savatchaga {n+1}-mahsulotni qo'shing: "))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
    else:
        print(f"Do'konimizda {mahsulot} yo'q")

mahsulotlar = ['kartoshka', 'piyoz', 'sabzi', 'makaron', 'olma', 'uzum']
savat = []
bor_mahsulotlar = []
yoq_mahsulotlar = []
for n in range(5):
    savat.append(input(f"Savatchaga {n+1}-mahsulotni qo'shing: "))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        yoq_mahsulotlar.append(mahsulot)

if len(bor_mahsulotlar) == 5:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
else:
    print("Do'konimizda quyidagi mahsulotlar yo'q")
    for ym in yoq_mahsulotlar:
        print(ym)


# Javobdagidan farqi
# if yoq_mahsulotlar:
#   print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in yoq_mahsulotlar:
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

foydalanuvchilar = ['vepa', 'sapa', 'rashid', 'xushnud', 'dili', 'sarri']
login = input('Yangi login kiriting: ')
if login.lower() in foydalanuvchilar:
    print('Login band, yangi login tanlang!')
else:
    print('Xush kelibsiz!')

son = int(input('Butun son kiriting: '))
for n in range(2,11):
    if son % n == 0:
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

# Javobdagidan farqi
# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")