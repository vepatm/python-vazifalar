n = 10
k = 1
massiv = []
p = 1
for i in range(1, n + 1):
    qator = []
    for j in range(i):
        qator.append(k)
        k += 1
    massiv.append(qator)
    p *= sum(qator)
for qator in massiv:
    print(qator)
print(p)