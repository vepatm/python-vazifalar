a = float(input('a='))
n = int(input('n='))
s = 0
for i in range(0,n+1):
    s += ((-1)**i)*(a**i)
    print(f"a^{i}={a**i}")
print('S='+str(s))