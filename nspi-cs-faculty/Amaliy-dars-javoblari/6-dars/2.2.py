import numpy as np
n = int(input('n='))
m = np.array(range(n))
for i in range(0,n):
    m[i] = int(input(f"m[{i+1}]="))
print(m)
juft = []
toq = []
for i in range(0,n):
    if m[i] % 2 == 0:
        juft.append(m[i])
    else:
        toq.append(m[i])
print(toq)
print(juft)
print(sum(juft)/len(juft))
p = 1
for i in toq:
    p *= i
print(p**(1/len(toq)))