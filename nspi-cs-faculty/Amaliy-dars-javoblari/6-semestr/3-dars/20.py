a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
if a>=b and b>=c:
    m = abs(a-b)
else:
    m = abs(a-c)
print(m)