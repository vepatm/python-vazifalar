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

satr_yigindisi = np.sum(massiv, axis=1)

eng_katta_yigindi = max(satr_yigindisi)
eng_kichik_yigindi = min(satr_yigindisi)

print(f'Har bir satr elementlari yig\'indisi: {satr_yigindisi}')
print(f'Eng kattasi: {eng_katta_yigindi}')
print(f'Eng kichigi: {eng_kichik_yigindi}')