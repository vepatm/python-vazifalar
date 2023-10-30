import math
a = int(input('a='))
b = int(input('b='))
n = int(input('n='))

ns = (b - a) / (n + 1)

n_lar = []
for i in range(1, n + 1):
    nuqta = a + i * ns
    fx = 1 - math.sin(nuqta)
    print(fx)