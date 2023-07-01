a = int(input('a='))
b = int(input('b='))
c = int(input('c='))

print(bool((a>0 and b<=0 or c<=0) or (b>0 and a<=0 or c<=0) or (c>0 and b<=0 or a<=0)))