import math
n = int(input('n='))
x = float(input('x='))
s = 1
for i in range(1,n+1):
    azo = (x**i) / math.factorial(i)
    s += azo
print('S='+s)