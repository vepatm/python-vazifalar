a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
k=0
while a-c>=0:
    a = a-c
    bt = b
    while b-c>=0:
        bt = bt - c
        k += 1
print(k)