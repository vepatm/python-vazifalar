n = int(input('n='))
t = [1,2,3]
for i in range(2,n+1):
    k = (t[i-2] + 2*t[i-1]) / 3
    t.append(k)
print(t)