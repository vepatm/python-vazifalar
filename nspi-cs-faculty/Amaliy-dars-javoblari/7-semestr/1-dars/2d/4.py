import numpy as np
import random
n = int(input('n='))
massiv = np.empty((n,n), dtype=int)
for i in range(n):
    for j in range(n):
        e = random.randint(-5,10)
        massiv[i][j] = e
print(massiv)

max = massiv[0,0]
for i in range(n):
    for j in range(n):
        if i==j and max<massiv[i,j]:
            max = massiv[i,j]
            k = i+1
print(f'Bosh diogonalining eng katta elementi: {max}')
print(f'U turgan ustun: {k}')