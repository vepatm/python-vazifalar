import numpy as np
import random
n = int(input('n='))
massiv = np.empty((n,n), dtype=int)
for i in range(n):
    for j in range(n):
        e = random.randint(-5,10)
        massiv[i][j] = e
print(massiv)

min_element = np.min(massiv)

# Eng kichik elementni joylashgan satrni va ustunni aniqlash
min_index = np.unravel_index(np.argmin(massiv), massiv.shape)
ustun_index, satr_index = min_index

# Joylashgan satr va ustunni o'chiramiz
massiv = np.delete(massiv, ustun_index, axis=0)
massiv = np.delete(massiv, satr_index, axis=1)

# Natijani chiqaramiz
print("Eng kichik element:", min_element)
print("Eng kichik elementni joylashgan satr va ustunni o'chirilgan massiv:")
print(massiv)