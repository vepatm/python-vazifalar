import math
n = int(input("n="))
x = float(input("x="))
s = x
maxraj = 1
for i in range(1,n+1):
    maxraj *= (2*i)*(2*i+1)
    surat = 1
    for j in range(1,2*i):
        surat *= j
    azo = surat*(x**(2*i+1)) / maxraj
    s += azo
print('S='+str(s))