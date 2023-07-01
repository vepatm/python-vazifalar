n = int(input('n='))
s = 0
t = list(range(n,0,-1))
for i in range(1,n+1):
    s = s + i**(t[i-1])
print(s)