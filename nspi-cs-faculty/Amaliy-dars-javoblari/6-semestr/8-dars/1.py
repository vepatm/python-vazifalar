import numpy as np
n = int(input('Massiv uzunligini kiriting: '))
m = np.array(range(n))
for i in range(0,n):
    m[i] = int(input(f"m[{i+1}]="))
k = int(input('Qaysi sonni izlamoqchisiz: '))
s = 0
for i in m:
    if k == i:
        s += 1
print(s)