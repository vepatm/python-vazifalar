e = float(input('e='))
ak = 2
ak1 = 1
k =2
while abs(ak-ak1)>=e:
    ak2 = ak1
    ak1 = ak
    k += 1
    ak = (ak2 + 2*ak1)/3
print(k, ak, ak1)