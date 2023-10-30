a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
if a>=b and b>=c:
    a = 2*a
    b = 2*b
    c = 2*c
else:
    a = 0-a
    b = 0-b
    c = 0-c
print(a,b,c)