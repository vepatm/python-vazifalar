N=int(input('To\'g\'ri burchakli uchburchak element raqamini kiriting: '))
X=float(input('Element uzunligini kiriting: '))
if N==1:
    a=X
    c=a*(2**0.5)
    h=c/2
    S=c*h/2
elif N==2:
    c=X
    a=c/(2**0.5)
    h=c/2
    S=c*h/2
elif N==3:
    h=X
    c=2*h
    a=c/(2**0.5)
    S=c*h/2
elif N==4:
    S=X
    h=S**(0.5)
    c=2*h
    a=c/(2**0.5)
    
print('Katet uzunligi:', a, '; Gipotenuza uzunligi:',c, '; Gipotenuzdan tushirilgan balandlik:',h, '; Yuza:', S)