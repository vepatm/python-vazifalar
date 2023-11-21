e=float(input('e='))
a1=2
a=0
k=2
while abs(a-a1)>=e:
    k+=1
    a+=2+1/a1
    a1,a=a,a1
print(k)