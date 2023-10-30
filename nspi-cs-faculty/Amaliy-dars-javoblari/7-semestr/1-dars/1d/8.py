def almashtirish(massiv):
    if len(massiv) < 2:
        return massiv

    birinchi_element = massiv[0]
    oxirgi_element = massiv[-1]

    massiv[0] = oxirgi_element
    massiv[-1] = birinchi_element

    return massiv

import numpy as np
import random
royxat = []
for i in range(10):
    e = random.randint(1,20)
    royxat.append(e)
x = np.array(royxat)
print(x)
natija = almashtirish(x)
print(natija)