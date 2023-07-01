n = int(input("n = "))
a = []
for i in range(n):
    a.append(int(input(f"a[{i+1}] = ")))
ta = a[-2:] + a[:-2]
print(ta)