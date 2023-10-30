import numpy as np
import random
n = int(input('n='))
massiv = np.empty((n,n), dtype=int)
for i in range(n):
    for j in range(n):
        e = random.randint(-5,10)
        massiv[i][j] = e
print(massiv)

musbat = 0
manfiy = 0
nol = 0
for i in range(n):
    for j in range(n):
        if massiv[i][j]>0:
            musbat += 1
        elif massiv[i][j]<0:
            manfiy += 1
        else:
            nol += 1
print(f'Musbat elementlari soni: {musbat}')
print(f'Manfiy elementlari soni: {manfiy}')
print(f'Nol elementlari soni: {nol}')