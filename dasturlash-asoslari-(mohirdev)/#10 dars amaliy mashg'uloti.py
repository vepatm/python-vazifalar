cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())

user = input('Login ismingiz nima?\n>>>')
if user.lower() == 'admin':
    print(f"Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print('Xush kelibsiz', user.title())

a = float(input('1-sonni kiriting: '))
b = float(input('2-sonni kiriting: '))
if a==b:
    print('Sonlar teng')

son = float(input('Istalgan son kiriting: '))
if son >= 0:
    print('Musbat son')
else:
    print('Manfiy son')

son = float(input('Istalgan son kiriting: '))
if son >= 0:
    print(son**(1/2))
else:
    print('Musbat son kiriting')