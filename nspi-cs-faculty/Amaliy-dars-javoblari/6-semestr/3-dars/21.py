x = int(input("x="))
y = int(input("y="))
if x==0 and y==0:
    n = 0
elif x>0 and y==0:
    n = 1
elif y>0 and x==0:
    n = 2
else:
    n = 3
print(n)