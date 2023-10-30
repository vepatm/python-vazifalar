import numpy as np
n = int(input('n='))
array = [int(input(f'a[{i+1}]=')) for i in range(n)]
a = np.array(array)
print(a)

max = max(a)
min = min(a)
for i in range(n):
    if a[i]==max:
        a[i]=1
    if a[i]==min:
        a[i]=-1
print(a)