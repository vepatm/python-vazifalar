import numpy as np
import random
n = int(input('n='))
a = []
for i in range(n):
    e = random.randint(-10,5)
    a.append(e)
massiv_a = np.array(a)
print(massiv_a)
b = []
for i in range(n):
    if massiv_a[i] < 0:
        b.append(massiv_a[i])
print(max(b))