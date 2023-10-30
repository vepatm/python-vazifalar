n = int(input("n = "))
a = []
for i in range(n):
    a.append(int(input(f"a[{i+1}] = ")))
oe = 0
te = 0
for i in range(n):
    if a[i]>0:
        oe += 1
    else:
        te += 1
print('Musbat',oe, \
    '\nManfiy elementlar', te)