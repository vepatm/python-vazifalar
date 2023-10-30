x1 = float(input('x1='))
y1 = float(input('y1='))
x2 = float(input('x2='))
y2 = float(input('y2='))
x3 = float(input('x3='))
y3 = float(input('y3='))
a = ((x2-x1)**2+(y2-y1)**2)**(1/2)
b = ((x3-x2)**2+(y3-y2)**2)**(1/2)
c = ((x3-x1)**2+(y3-y1)**2)**(1/2)
P = a+b+c
p = P/2
s = (p*(p-a)*(p-b)*(p-c))**(1/2)
print('P='+str(P), 'S='+str(s))