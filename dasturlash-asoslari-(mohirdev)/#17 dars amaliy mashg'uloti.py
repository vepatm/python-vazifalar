print("Yaqin do'stlaringiz ro'yxatini tuzamiz")
ismlar = []
n=1
while True:
    savol = f"{n}-do'stingizni ismini kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    takrorlash = input("Yana ism qo'shasizmi (ha/yo'q): ")
    n+=1
    if takrorlash != 'ha':
        break
print("Do'stlaringiz ro'yxati:")
for ism in ismlar:
    print(ism)

dostlar = {}
ishora = True
while ishora:
    ism = input("Do'stingiz ismini kiriting: ")
    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
    dostlar[ism] = int(yosh)

    javob = input("Yana ma'lumot qo'shasizmi (ha/yo'q): ")
    if javob == "yo'q":
        ishora = False
for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")


cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'audi', 'malibu', 'nexia']
car = 'nexia'
while car in cars:
    cars.remove(car)
print(cars)

talabalar = ['hasan', 'husan', 'olim', 'botir']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}nig bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = baho
for talaba, baho in baholangan_talabalar.items():
    print(f"{talaba.title()}: {baho}")