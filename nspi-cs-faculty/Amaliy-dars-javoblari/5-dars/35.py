n = int(input('n='))
t = [1,2,3]
for i in range(3,n+1):
    k = t[i-1] + t[i-2] - 2*t[i-3]
    t.append(k)
print(t)