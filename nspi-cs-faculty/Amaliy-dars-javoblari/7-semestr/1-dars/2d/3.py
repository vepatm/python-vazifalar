import numpy as np
import random
n = int(input('n='))
massiv = np.empty((n,n), dtype=int)
for i in range(n):
    for j in range(n):
        e = random.randint(-5,10)
        massiv[i][j] = e
print(massiv)

manfiy_k = 1
diogonal_y = 0
for i in range(n):
    for j in range(n):
        if i==j:
            diogonal_y += massiv[i][j]
        if massiv[i][j]<0:
            manfiy_k *= massiv[i][j]

print(f'Diogonal elementlari yig\'indisi: {diogonal_y}')
print(f'Manfiy elementlari ko\'paytmasi: {manfiy_k}')