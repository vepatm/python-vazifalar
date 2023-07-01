import numpy as np
n = int(input('n='))
m = np.array(range(n))
for i in range(0,n):
    m[i] = int(input(f"m[{i+1}]="))
print(m)
max = m[0]
for i in range(0,n):
    if m[i]>max:
        max = m[i]
        k = i+1
print('Max element = ', max, '\nTurgan o\'rni = ', k)