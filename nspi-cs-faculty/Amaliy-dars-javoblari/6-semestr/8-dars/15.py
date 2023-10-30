n = int(input("n = "))
a = []
for i in range(n):
    a.append(int(input(f"a[{i+1}] = ")))
print(sorted(a, reverse=True))