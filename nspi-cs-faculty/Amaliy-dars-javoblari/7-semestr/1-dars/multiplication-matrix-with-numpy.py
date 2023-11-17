import random
import numpy as np

print("Birinchi matritsa o'lchami:")
b_m = int(input('m='))
b_n = int(input('n='))

print()

print('Ikkinchi o\'lchami:')
i_m = int(input('m='))
i_n = int(input('n='))

print()

first_m = np.empty((b_m,b_n), dtype=int)
second_m = np.empty((i_m,i_n), dtype=int)

for i in range(b_m):
    for j in range(b_n):
        e = random.randint(-5,10)
        first_m[i][j] = e
print(first_m)

print()

for i in range(i_m):
    for j in range(i_n):
        e = random.randint(-5,10)
        second_m[i][j] = e
print(second_m)

print()

if b_m == i_n:
    c_m = np.dot(first_m, second_m)
    print(c_m)
else:
    print("Bu ikki matritsani ko'paytirib bo'lmaydi")