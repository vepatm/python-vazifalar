n = int(input("n = "))
a = []
b = []
c = []
for i in range(n):
    a.append(int(input(f"a[{i+1}] = ")))
    if a[i]%2==0:
        c.append(a[i])
    else:
        b.append(a[i])
print(b, \
    c)