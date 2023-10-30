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

satlar_eng_katta = np.max(massiv, axis=1)
indekslar = np.argmax(massiv, axis=1)

indekslar_pyus_bir = []
for i in indekslar:
    e = i+1
    indekslar_pyus_bir.append(e)

indekslar_togri = np.array(indekslar_pyus_bir)

print(f'Massivning har bir satrining eng katta elementi: {satlar_eng_katta}')
print(f'Ularning indekslari: {indekslar_togri}')