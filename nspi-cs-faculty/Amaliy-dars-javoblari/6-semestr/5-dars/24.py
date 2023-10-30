import math
n = int(input('n='))
x = float(input('x='))
s = 1
belgi = -1
for i in range(1,n+1):
    azo = belgi * (x**(2*i)) / math.factorial(2*i)
    s += azo
print('S='+str(s))