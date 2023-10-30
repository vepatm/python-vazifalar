uzunlik_birligi = int(input('uznlik birligini kiriting (1-5) ='))
uzunlik = float(input('Uzunlikni kiriting = '))
metr = {
    1: uzunlik/10,
    2: uzunlik*1000,
    3: uzunlik,
    4: uzunlik/1000,
    5: uzunlik/100
}
print(metr.get(uzunlik_birligi, 'Bunday uzunlik birligi yo\'q'))