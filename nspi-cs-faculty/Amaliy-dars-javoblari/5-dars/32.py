n = int(input('n='))
t = [1]
for i in range(1,n+1):
    k = (t[i-1]+1)/i
    t.append(k)
print(t)