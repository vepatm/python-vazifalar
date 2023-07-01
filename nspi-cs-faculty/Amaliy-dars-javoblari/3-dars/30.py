n = int(input('n='))
if n<10 and n%2 == 0:
    r = "bir xonali juft son"
if n<10 and n%2 != 0:
    r = "bir xonali toq son"
if n>=10 and n<100 and n%2 == 0:
    r = "ikki xonali juft son"
if n>=10 and n<100 and n%2 != 0:
    r = "ikk xonali toq son"
if n>=100 and n<1000 and n%2 == 0:
    r = "uch xonali juft son"
if n>=100 and n<1000 and n%2 != 0:
    r = "uch xonali toq son"