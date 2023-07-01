N=int(input('Teng tomonli uchburchak raqamini kiriting: '))
X=float(input('Element uzunligini kiriting: '))
if N==1:
    a=X
    R1=a*(3**0.5)/6
    R2=2*R1
    S=a**2*(3**0.5)/4
elif N==2:
    R1=X
    a=R1*6/(3**0.5)
    R2=2*R1
    S=a**2*(3**0.5)/4
elif N==3:
    R2=X
    R1=R2/2
    a=R1*6/(3**0.5)
    S=a**2*(3**0.5)/4
elif N==4:
    S=X
    a=(S*4/(3**0.5))**0.5
    R1=a*(3**0.5)/6
    R2=2*R1
    
print('Yon tomoni:', a, '; R1:', R1, '; R2:', R2, '; Yuza:', S)