n = int(input('n='))
t = [2]
for i in range(1,n+1):
    k = 2 + 1/t[i-1]
    t.append(k)
print(t)