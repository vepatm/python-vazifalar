n = int(input("n = "))
a = []
for i in range(n):
    a.append(int(input(f"a[{i+1}] = ")))
b = [0]*n
for i in range(1, n+1):
    b[i-1] = sum(a[0:i])/i
print(b)