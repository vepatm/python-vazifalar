a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
if (a>=b and b>=c) or (b>=a and a>=c):
    k = c
elif (a>=c and c>=b) or (c>=a and a>=b):
    k = b
else:
    k = a
print(k)