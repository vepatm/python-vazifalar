a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
if ((a+b>=a+c) and (a+c>=b+c)) or ((a+b>=b+c) and (a+c>=b+c)):
    print(a,b)
elif ((a+c>=a+b) and (a+c>=b+c)) or ((a+c>=b+c) and (b+c>=a+b)):
    print(a,c)
else:
    print(b,c)