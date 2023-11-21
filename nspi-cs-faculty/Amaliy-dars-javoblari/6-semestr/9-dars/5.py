n=int(input('n='))
k=0
while n>=2:
    n=n//2
    k+=1
print(k)
if(n%2!=0):
    print('2 darajasi emas')