import math
n=int(input('n='))
k=0
while (math.pow(3,k)>n)==False:
    k+=1
print('k=',k)