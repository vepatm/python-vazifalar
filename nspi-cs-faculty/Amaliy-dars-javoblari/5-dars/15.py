a = float(input('a='))
n = int(input('n='))
s = 1
for i in range(1,n+1):
    s *= a
print('a^n = ',s)