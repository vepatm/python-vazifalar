n = int(input('n='))
baholar = {
    1: 'Yomon',
    2: 'Qoniqarsiz',
    3: 'Qoniqarli',
    4: 'Yaxshi',
    5: 'A\'lo'
}
print(baholar.get(n, 'Bunday baho yo\'q'))