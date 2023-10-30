a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
if a>=b and b>=c:
    print(c,a)
elif b>=a and a>=c:
    print(c,b)
elif b>=c and c>=a:
    print(a,b)
elif c>=b and b>=a:
    print(a,c)
elif c>=a and a>=b:
    print(b,c)
else:
    print(b,a)