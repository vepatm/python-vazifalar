import random
title  = {
    1 : 'крысы',
    2 : 'коровы',
    3 : 'тигра',
    4 : 'зайца',
    5 : 'дракона',
    6 : 'змеи',
    7 : 'лошади',
    8 : 'овцы',
    9 : 'обезьяны',
    10 : 'курицы',
    11 : 'собаки',
    12 : 'свиньи'
}
color = {
    0 : {
        1 : 'зеленой',
        2 : 'красной',
        3 : 'желтой',
        4 : 'белой',
        5 : 'черной'
    },
    1 : {
        1 : 'зеленого',
        2 : 'красного',
        3 : 'желтого',
        4 : 'белого',
        5 : 'черного'
    }
}
N = random.randrange(1900,2222)
N = 1932
N = 1976
print("Год:",N)
year_name = 'Год '
title_code = (N - 4) % 12 + 1
print("Title code: ", title_code)
print("Title: ", title[title_code])
i = 0
if title_code in [3,4,5]:
    i = 1
color_code = (N - 4) % 10 + 1
color_code = int((color_code - 1) / 2) + 1
print("Color code: ", color_code)
print("Color: ", color[i][color_code])
year_name += color[i][color_code] + ' ' + title[title_code]
print(year_name)