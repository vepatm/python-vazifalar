import numpy as np
n = int(input('n='))
array = [int(input(f'a[{i+1}]=')) for i in range(n)]
a = np.array(array)
print(a)

max = a[0]
for i in range(n):
    if max<a[i]:
        max = a[i]
        k = i+1

min = a[0]
for i in range(n):
    if min>a[i]:
        min = a[i]
        m = i+1
print(f'Max index = {k}\n'
      f'Min index = {m}')