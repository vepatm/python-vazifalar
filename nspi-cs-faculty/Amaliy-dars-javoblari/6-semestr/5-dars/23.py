import math
n = int(input('n='))
x = float(input('x='))
s = x
belgi = -1
for i in range(1,n+1):
    azo = belgi * (x ** (2*i+1)) / math.factorial(2*i+1)
    s += azo
    belgi *= -1
print('S='+str(s))