n = int(input("n = "))
a = []
for i in range(n):
    a.append(int(input(f"a[{i+1}] = ")))
max = a[0]
for i in range(n):
    if a[i]>max:
        max = a[i]
        k = i+1
print('Max = ', max,\
    'indeks = ', k)