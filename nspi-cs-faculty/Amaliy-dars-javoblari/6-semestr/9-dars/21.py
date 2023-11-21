n = int(input('n='))
ch = False
while n>0:
    if n%2!=0:
        ch = True
    n //= 10
print(ch)