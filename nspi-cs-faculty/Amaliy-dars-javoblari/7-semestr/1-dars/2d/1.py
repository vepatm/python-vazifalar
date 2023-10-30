import numpy as np
import random
n = int(input('n='))
massiv = np.empty((n,n), dtype=int)
for i in range(n):
    for j in range(n):
        e = random.randint(-5,10)
        massiv[i][j] = e
print(massiv)

musbat_y = 0
manfiy_k = 1
for i in range(n):
    for j in range(n):
        if massiv[i][j]>=0:
            musbat_y += massiv[i][j]
        else:
            manfiy_k *= massiv[i][j]
print(f'Musbat elementlari yig\'indisi: {musbat_y}')
print(f'Manfiy elementlari ko\'paytmasi: {manfiy_k}')