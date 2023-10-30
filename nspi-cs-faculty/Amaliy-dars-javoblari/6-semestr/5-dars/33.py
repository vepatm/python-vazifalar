n = int(input('n='))
t = [1,1]
for i in range(2,n+1):
    k = t[i-2]+t[i-1]
    t.append(k)
print(t)