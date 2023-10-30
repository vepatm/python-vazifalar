a = int(input('a='))

y = a // 100
o = (a // 10) % 10
b = a % 100

print(bool((y<=o and o<=b) or (y>=o and o>=b)))