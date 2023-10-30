import numpy as np
n = int(input('n='))
array = [int(input(f'a[{i+1}]=')) for i in range(n)]
a = np.array(array)
print(a)

musbat = 0
manfiy = 0
nol = 0
for i in range(n):
    if a[i]>0:
        musbat += 1
    elif a[i]<0:
        manfiy += 1
    else:
        nol += 1

print(f'Musbat elementlari soni: {musbat}\n'
      f'Manfiy elementlari soni: {manfiy}\n'
      f'Nol elementlari soni: {nol}')