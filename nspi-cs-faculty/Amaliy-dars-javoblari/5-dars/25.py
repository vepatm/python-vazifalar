n = int(input('n='))
x = float(input('x='))
s = 0
belgi = 1
for i in range(1,n+1):
    azo = belgi * (x**i)/i
    s += azo
print('S='+str(s))