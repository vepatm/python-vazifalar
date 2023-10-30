a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
print(bool(a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2))