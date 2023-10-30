a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
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