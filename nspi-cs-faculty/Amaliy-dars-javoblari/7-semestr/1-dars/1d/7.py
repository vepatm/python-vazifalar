import numpy as np
import random
royxat = []
for i in range(10):
    e = random.randint(1,20)
    royxat.append(e)
x = np.array(royxat)
print(x)

toq = []
juft = []
for i in x:
    if i%2==0:
        juft.append(i)
    else:
        toq.append(i)
print(set(toq))
print(set(juft))