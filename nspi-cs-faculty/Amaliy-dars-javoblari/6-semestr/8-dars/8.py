import numpy as np
n = int(input('Massiv uzunligini kiriting: '))
a = np.array(range(n))
for i in range(0,n):
    a[i] = int(input(f"m[{i+1}]="))
max = a[0]
for i in range(0,n):
    if max<a[i]:
        max = a[i]
print(max)