import numpy as np
n = int(input('Massiv uzunligini kiriting: '))
a = np.array(range(n))
for i in range(0,n):
    a[i] = int(input(f"m[{i+1}]="))
t = a[0]
for i in range(0,n-1):
    a[i]=a[i+1]
a[n-1] = t
print(a)