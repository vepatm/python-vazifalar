n = int(input("n = "))
a = []
s = 0
for i in range(n):
    a.append(int(input(f"a[{i+1}] = ")))
    s += a[i]
print(s)