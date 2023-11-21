s = float(input('s='))
p = int(input('(0<p<25) p='))
s2 = s
k = 0
while s2!=2*s:
    foiz = s2/100*p
    s2 += foiz
    k += 1
print('k=',k)
print('S=',s2)