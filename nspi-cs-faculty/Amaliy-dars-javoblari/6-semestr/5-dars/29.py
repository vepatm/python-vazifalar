a = int(input('a='))
b = int(input('b='))
n = int(input('n='))

# nuqtalar soni
ns = (b - a) / (n + 1)

# nuqtalar
n_lar = []
for i in range(1, n + 1):
    nuqta = a + i * ns
    n_lar.append(nuqta)

print("Ajratilgan nuqtalar:")
for i in n_lar:
    print(i)