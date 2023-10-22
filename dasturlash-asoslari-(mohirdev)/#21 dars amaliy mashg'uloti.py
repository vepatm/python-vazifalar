def katta_harf(ismlar):
    for i in range(len(ismlar)):
        ismlar[i] = ismlar[i].title()
names = ['ali','vali','hasan','husan']
katta_harf(names)
print(names)

def katta_harf(ismlar):
    for i in range(len(ismlar)):
        ismlar[i] = ismlar[i].title()
names = ['ali','vali','hasan','husan']
new_names = katta_harf(names[:])
print(names)
print(new_names)

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = int(baho)
    return baholar
talabalar = ['ali','vali','hasan','husan']
baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)