import numpy as np
import random
n = int(input('n='))
m = int(input('m='))
massiv = np.empty((n,m), dtype=int)
for i in range(n):
    for j in range(m):
        e = random.randint(-5,10)
        massiv[i][j] = e
print(massiv)

ustunlar_y = np.sum(massiv, axis=0)
satrlar_k = np.prod(massiv, axis=1)
print(f'Massivning har bir ustunlari yig\'indisi: {ustunlar_y}')
print(f'Massivning har bir satrlari ko\'paytmasi: {satrlar_k}')