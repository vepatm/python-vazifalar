import math
n = int(input("n="))
x = float(input("x="))
s = 1
belgi = 1
for i in range(1, n + 1):
    toq = math.prod(range(1, 2*i, 2))
    juft = math.prod(range(2, 2*i+1, 2))
    azo = (belgi * toq * (x ** i)) / juft
    s += azo
    belgi *= -1
print("Natija:", s)