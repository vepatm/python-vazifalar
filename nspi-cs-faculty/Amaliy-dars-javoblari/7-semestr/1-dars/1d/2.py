import numpy as np
n = int(input('n='))
array = [int(input(f'a[{i+1}]=')) for i in range(n)]
a = np.array(array)
print(a)
print(sorted(a))