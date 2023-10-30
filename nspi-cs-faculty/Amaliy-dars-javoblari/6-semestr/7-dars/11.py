C = input('Robot yo\'nalishini kiriting (N W E S): ')
N1 = int(input('Birinchi komandani kiriting: '))
N2 = int(input('Ikkinchi komandani kiriting: '))
if C=='N':
    if N1+N2 in (-1,3):
        C='E'
    elif N1+N2==1:
        C='W'
    elif N1+N2 in (2,-2):
        C='S'
        
elif C=='E':
    if N1+N2 in (-1,3):
        C='S'
    elif N1+N2==1:
        C='N'
    elif N1+N2 in (2,-2):
        C='W'
        
elif C=='S':
    if N1+N2 in (-1,3):
        C='W'
    elif N1+N2==1:
        C='E'
    elif N1+N2 in (2,-2):
        C='N'
        
elif C=='W':
    if N1+N2 in (-1,3):
        C='N'
    elif N1+N2==1:
        C='S'
    elif N1+N2 in (2,-2):
        C='E'
print(C)