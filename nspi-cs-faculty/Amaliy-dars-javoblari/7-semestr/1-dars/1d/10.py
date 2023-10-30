import numpy as np
import random
n = int(input('n='))
a = []
for i in range(n):
    e = random.randint(1,20)
    a.append(e)
massiv_a = np.array(a)
b = []
for i in range(n):
    e = random.randint(1,20)
    b.append(e)
massiv_b = np.array(b)
print(massiv_a)
print(massiv_b)
c = []
for i in range(n):
    if (a[i] % 2 != 0) and (a[i] not in b):
        c.append(a[i])
massiv_c = np.array(c)
print(massiv_c)