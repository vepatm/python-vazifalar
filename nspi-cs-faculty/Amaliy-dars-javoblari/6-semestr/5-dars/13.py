n = int(input('n='))
s = 0
for i in range(11,11+n):
    s += ((-1)**(i-1))*i/10
print(s)