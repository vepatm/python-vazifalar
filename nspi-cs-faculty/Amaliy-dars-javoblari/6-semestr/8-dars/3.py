import numpy as np
n = int(input('Massiv uzunligini kiriting: '))
a = np.array(range(n))
for i in range(0,n):
    a[i] = int(input(f"m[{i+1}]="))
s = 0
for i in range(0,n-1):
    if (a[i]>=0 and a[i+1]>=0) or a[i]>=0 and a[i+1]>=0:
        s += 1
if s > 0:
    print('Yes')
else:
    print('No')