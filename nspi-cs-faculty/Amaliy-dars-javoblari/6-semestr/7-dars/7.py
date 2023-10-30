ogirlik_birligi = int(input('Og\'irlik birligini kiriting (1-5) ='))
ogirlik = float(input('Og\'irlikni kiriting = '))
kg = {
    1: ogirlik,
    2: ogirlik / (10**5),
    3: ogirlik / 1000,
    4: ogirlik * 1000,
    5: ogirlik * 100
}
print(kg.get(ogirlik_birligi, 'Bunday og\'irlik birligi yo\'q'))