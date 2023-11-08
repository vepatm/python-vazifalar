import numpy as np
import random

n=2

massiv = np.empty((n,n), dtype=int)
for i in range(n):
    for j in range(n):
        e = random.randint(-5,10)
        massiv[i][j] = e
print(massiv)

a = random.randint(1,10)
b = random.randint(11,21)
vector = [a,b]
print(vector)

d = massiv[0][0]*massiv[1][1]-massiv[0][1]*massiv[1][0]
dx = massiv[0][0]*vector[1]-massiv[1][0]*vector[1]
dy = massiv[0][1]*vector[1]-massiv[1][1]*vector[1]

if d==0:
    print('Yechimga ega emas')
else:
    x = d/dx
    y = d/dy
    print(f'Yechimi: ({x},{y})')