import math
n = int(input('n='))
s = 0
for i in range(1,n+1):
    s += math.prod(range(1,i+1))
print(s)