import random
title  = {
    1 : 'Водолей',
    2 : 'Рыбы',
    3 : 'Овен',
    4 : 'Телец',
    5 : 'Близнецы',
    6 : 'Рак',
    7 : 'Лев',
    8 : 'Дева',
    9 : 'Весы',
    10 : 'Скорпион',
    11 : 'Стрелец',
    12 : 'Козерог'
}
M = random.randrange(1,13)
if M in [1,3,5,7,8,10,12]:
    D = random.randrange(1,32)
elif M in [4,6,9,11]:
    D = random.randrange(1,31)
else:
    D = random.randrange(1,30)
#D = 1
#M = 1
print("День:",D)
print("Месяц:",M)
x = M*100 + D
if x in range(101,119):
    i = 12
elif x in range(120,218):
    i = 1
elif x in range(219,320):
    i = 2
elif x in range(321,419):
    i = 3
elif x in range(420,520):
    i = 4
elif x in range(521,621):
    i = 5
elif x in range(622,722):
    i = 6
elif x in range(723,822):
    i = 7
elif x in range(823,922):
    i = 8
elif x in range(923,1022):
    i = 9   
elif x in range(1023,1122):
    i = 10
elif x in range(1123,1221):
    i = 11
elif x in range(1222,1231):
    i = 12
print("Знак Зодиака:",title[i])