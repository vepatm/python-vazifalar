import numpy as np
import random

n = 3

massiv = np.empty((n,n), dtype=int)
for i in range(n):
    for j in range(n):
        e = random.randint(-5,10)
        massiv[i][j] = e
print(massiv)

a = random.randint(1,10)
b = random.randint(11,20)
c = random.randint(21,30)
vector = [a,b,c]
print(vector)

def d(m):
    m1 = m[0][0]*m[1][1]*m[2][2]
    m2 = m[0][1]*m[1][2]*m[2][0]
    m3 = m[1][0]*m[2][1]*m[0][2]
    s1 = m1 + m2 + m3
    m4 = m[0][2]*m[1][1]*m[2][0]
    m5 = m[0][1]*m[1][0]*m[2][2]
    m6 = m[2][1]*m[1][2]*m[0][0]
    s2 = m4 + m5 + m6
    s = s1 - s2
    return s

def dx(m,v):
    mv1 = v[0]*m[1][1]*m[2][2]
    mv2 = m[0][1]*m[1][2]*v[2]
    mv3 = v[1]*m[2][1]*m[0][2]
    s1 = mv1 + mv2 + mv3
    mv4 = m[0][2]*m[1][1]*v[2]
    mv5 = m[0][1]*v[1]*m[2][2]
    mv6 = v[0]*m[1][2]*m[2][1]
    s2 = mv4 + mv5 + mv6
    s = s1 - s2
    return s

def dy(m,v):
    mv1 = m[0][0]*v[1]*m[2][2]
    mv2 = v[0]*m[1][2]*m[2][0]
    mv3 = m[1][0]*v[2]*m[0][2]
    s1 = mv1 + mv2 + mv3
    mv4 = m[0][2]*v[1]*m[2][0]
    mv5 = v[0]*m[1][0]*m[2][2]
    mv6 = m[1][2]*v[2]*m[1][0]
    s2 = mv4 + mv5 + mv6
    s = s1 - s2
    return s

def dz(m,v):
    mv1 = m[0][0]*m[1][1]*v[2]
    mv2 = m[1][0]*m[2][1]*v[0]
    mv3 = m[0][1]*v[1]*m[2][0]
    s1 = mv1 + mv2 + mv3
    mv4 = v[0]*m[1][1]*m[2][0]
    mv5 = m[0][1]*m[1][0]*v[2]
    mv6 = v[1]*m[2][1]*m[0][0]
    s2 = mv4 + mv5 + mv6
    s = s1 - s2
    return s

d = d(massiv)
if d!=0:
    x = dx(massiv,vector)/d
    y = dy(massiv,vector)/d
    z = dz(massiv,vector)/d
    toplam = (round(x,2),round(y,2),round(z,2))
    print(f'Korenleri: {toplam}')
else:
    print('Tengleme sheshimge iye emes')