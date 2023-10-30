import numpy as np
n = int(input('n='))
k = int(input('k='))
m = np.array(range(n))
for i in range(0,n):
    m[i] = int(input(f"m[{i+1}]="))
print(m)
t = 0
for i in range(0,n):
    if m[i]>k:
        t += 1
print(f"{k} elementdan katta elementlar soni: {t}")