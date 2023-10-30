a = float(input('a='))
b = float(input('b='))
amal = int(input('amal='))
arif = {
    1: a+b,
    2: a-b,
    3: a*b,
    4: a/b
}
print(arif.get(amal, 'Bunday amal yo\'q'))