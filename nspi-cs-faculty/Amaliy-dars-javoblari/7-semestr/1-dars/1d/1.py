import numpy as np
n = int(input('n='))
array = [int(input(f'a[{i+1}]=')) for i in range(n)]
a = np.array(array)
print(a)
print(f'Max = {max(a)}')
print(f'Min = {min(a)}')