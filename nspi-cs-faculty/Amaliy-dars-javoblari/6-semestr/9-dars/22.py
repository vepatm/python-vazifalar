n = int(input('n='))
ch = True
d = 2
while d*d<=n:
    if n%2==0:
        ch = False
        break
    d += 1
print(ch)