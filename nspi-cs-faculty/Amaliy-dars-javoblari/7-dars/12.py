N=int(input('Aylana element raqamini kiriting: '))
X=float(input('Aylana elementi uzunligini kiriting: '))
if N==1:
    R=X
    D=2*R
    L=2*3.14*R
    S=3.14*R**2
    print(D,L,S)
elif N==2:
    R=X/2
    D=X
    L=2*3.14*R
    S=3.14*R**2
    print(R,L,S)
elif N==3:
    R=X/(2*3.14)
    D=2*R
    L=X
    S=3.14*R**2
    print(R,D,S)
elif N==4:
    R=(X/3.14)**(1/2)
    D=2*R
    L=2*3.14*R
    S=X
    print(R,D,L)