x = int(input("x="))
y = int(input("y="))
if x>0 and y>0:
    n = 1
elif x<0 and y>0:
    n = 2
elif x<0 and y<0:
    n = 3
elif x>0 and y<0:
    n = 4
else:
    n = 'Kordinata boshida yotadi'
print(n)