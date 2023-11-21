a = int(input('a='))
b = 0
while a != 0 and b != 2:
    b = a % 10
    a = a // 10
print(b==2)