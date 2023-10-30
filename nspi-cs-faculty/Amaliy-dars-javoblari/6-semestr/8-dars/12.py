n = int(input("n = "))
a = []
for i in range(n):
    a.append(int(input(f"a[{i+1}] = ")))
s = 0
for i in range(n-1):
    if a[i]==0 and a[i+1]==0:
        s += 1
if s>0:
    print('Yes')
else:
    print('No')