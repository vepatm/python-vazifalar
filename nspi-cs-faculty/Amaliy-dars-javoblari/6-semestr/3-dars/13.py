a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
if (a>=b and b>=c) or (c>=b and b>=a):
    o = b
elif (b>=a and a>=c) or (c>=a and a>=b):
    o = a
else:
    o = c
print(o)