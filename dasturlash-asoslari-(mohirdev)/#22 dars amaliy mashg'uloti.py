def kopaytma(*sonlar):
    p = 1
    for son in sonlar:
        p *= son
    return p
print(kopaytma(1,2,3,4,5,6,7,8,9,10))

def talaba_info(ism,familiya,**malumotlar):
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar
talaba1 = talaba_info('Vepa', 'Kurbanklichev', yosh=21, malumot='tugallanmagan oliy')
print(talaba1)