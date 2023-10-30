import numpy as np
n = int(input('Massiv uzunligini kiriting: '))
a = np.array(range(n))
for i in range(0,n):
    a[i] = int(input(f"m[{i+1}]="))
b = np.array(range(n))
for i in range(0,n):
    b[i] = int(input(f"m[{i+1}]="))
print('A = ',b)
print('B = ',a)