n = int(input("n = "))
a = []
for i in range(n):
    a.append(int(input(f"a[{i+1}] = ")))
min = a[0]
for i in range(n):
    if a[i]<min:
        min = a[i]
        k = i+1
print('Min = ', min,\
    'indeks = ', k)