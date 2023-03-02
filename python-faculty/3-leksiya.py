# 1-topshiriq
a = float(input('a='))
b = float(input('b='))
if a < 0:
    y=a**2+b
elif a > 1:
    y=a+b**2
else:
    y=a+b
print('y=' + str(y))

# 2-topshiriq
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
if a != 0:
    d = b**2-4*a*c
    if d > 0:
        x1=(-b+(d)**(1/2))/(2*a)
        x2=(-b-(d)**(1/2))/(2*a)
        print('Tenglama yechimlari:', x1, 'va', x2)
    elif d == 0:
        x=-b/(2*a)
        print('Tenglama yechimi:', x)
    else:
        print('Tenglama yechimga ega emas')
else:
    print('Berilgan tenglama kvadrat tenglama emas')

# 3-topshiriq
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
if (a+b>c) and (b+c>a) and (a+c>b):
    p = (a+b+c)/2
    s=(p*(p-a)*(p-b)*(p-c))**(1/2)
    print('S = ', s)
else:
    print('Bunday uchburchak mavjud emas')

# 4-topshiriq
b = int(input('Ball: '))
baholar = {
    0<=b<60: 'Baho: 2',
    60<=b<70: 'Baho: 3',
    70<=b<90: 'Baho: 4',
    90<=b<=100: 'Baho: 5',
    b<0 and b>100: 'Xato'
}
print(baholar.get(True))