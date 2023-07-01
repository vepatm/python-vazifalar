import numpy as np
n = int(input('Massiv uzunligini kiriting: '))
a = np.array(range(n))
for i in range(0,n):
    a[i] = int(input(f"m[{i+1}]="))
k = int(input('k = '))
l = int(input('l = '))
s = 0
for i in range(k,l+1):
    s += a[i]
print('S = ',s)