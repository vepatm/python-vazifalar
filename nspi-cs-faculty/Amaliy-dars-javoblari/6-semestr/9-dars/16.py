s = 10
p = float(input('(0<p<50) p='))

k=0
while s<200:
    foiz = s/100*p
    s += foiz
    k += 1
print('S=',s)
print('k=',k)