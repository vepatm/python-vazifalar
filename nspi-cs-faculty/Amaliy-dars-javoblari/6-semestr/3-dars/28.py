n = int(input('n='))
if n%4 == 0 and n%100 != 0:
    k = 366
elif n%400 == 0:
    k = 366
else:
    k = 365
print(k)