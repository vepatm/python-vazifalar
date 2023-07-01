n = int(input("n = "))
a = []
for i in range(n):
    a.append(int(input(f"a[{i+1}] = ")))
s = 0
for i in range(n-1):
    if a[i]==a[i+1]:
        s += 1
print(s)