# 25-betdagi 3 ta topshiriq
# 1
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
shart = bool(b>=a and b<=c)
print('b soni a va c sonlar orasida yotadimi:',shart)
# 2
a = int(input('a='))
b = int(input('b='))
shart = bool(a%2!=0 and b%2!=0)
print('Ikkala son ham toqmi:',shart)
# 3
son = int(input('Musbat son kiriting: '))
shart = bool(son>=100 and son%2!=0)
print('Berilgan son 3 xonali toq sonmi:', shart)

# 10 likdan 8 likka o'tish
x = int(input('x='))
y = oct(x)
print(y)

# 10 likdan 16 likka o'tish
a = int(input('a='))
b = hex(a)
print(b)

a = float(input('1-kompleks sonning haqiyqiy qismini kiriting: '))
b = float(input('1-kompleks sonning mavhum qismini kiriting: '))
x = float(input('2-kompleks sonning haqiyqiy qismini kiriting: '))
y = float(input('2-kompleks sonning mavhum qismini kiriting: '))
com1 = complex(a,b)
com2 = complex(x,y)
s1 = com1+com2
s2 = com1-com2
s3 = com1*com2
s4 = com1/com2
print('sonlar yi\'gindisi:', s1, '\n'
'sonlar ayirmasi:', s2, '\n'
'sonlar ko\'paytmasi:', s3, '\n'
'birinchi sonni ikkinchisiga bo\'lgandagi natija:', s4)