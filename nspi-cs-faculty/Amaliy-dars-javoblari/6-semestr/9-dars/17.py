n = int(input('n='))
m = int(input('m='))
k=0
while n>=m:
    n = n - m
    k += 1
print(n)
print(k)