A = int(input("A ni kiriting: "))
B = int(input("B ni kiriting: "))
C = int(input("C ni kiriting: "))

f1 = A // C
f2 = B // C
ks = f1 * f2
ls = A*B - ks*(C**2)

print('Kvadratlar soni: ', ks)
print('Ortib qolgan yuza: ', ls)