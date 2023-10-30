import numpy as np
import random
n=3
m=3
massiv = np.empty((n,m), dtype=int)
for i in range(n):
    for j in range(m):
        e = random.randint(-5,10)
        massiv[i][j] = e
print('\n' + str(massiv) + '\n')

massiv[:, 0] *= 3
massiv[:, 2] *= 3

print(f'So\'ralgan massiv:\n{massiv}')