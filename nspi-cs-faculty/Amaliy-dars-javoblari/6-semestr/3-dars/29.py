n = int(input('n='))
r = []
if n>0:
    r.append("musbat")
elif n<0:
    r.append("manfiy")

if n%2 == 0 and n != 0:
    r.append("juft son")
elif n%2 != 0 and n != 0:
    r.append("toq son")
else:
    print("son nolga teng")

print(r[0], r[1])