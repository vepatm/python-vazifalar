n = int(input('n='))
f1 = 1
f2 = 1
f = 0
k = 2
while f<n:
    f = f2 + f1
    f2 = f1
    f1 = f
    k += 1
print(k)