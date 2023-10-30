a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
d = int(input("d="))
# a=b=c a=b=d a=c=d b=c=d
if a==b and b==c:
    tr = 4
if a==b and b==d:
    tr = 3
if a==c and c==d:
    tr = 2
if b==c and c==d:
    tr = 1
print(tr)