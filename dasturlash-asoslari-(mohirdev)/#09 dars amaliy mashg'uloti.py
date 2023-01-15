dostlar = ['Hudaýar', 'Dilşat', 'Röwşen', 'Azamat', 'Nadirbek']
for dost in dostlar:
    print('Gowymyň?', dost, 'dost')
    
print('Kod', len(dostlar), 'merte gaýtalandy')

sanlar = list(range(10, 100))
for san in sanlar:
    print(san**3)

print('5 däne iň gowy görýän kinolaryňyz haýsy?')
kinolar = []
for n in range(5):
    kinolar.append(input(f"{n+1}-nji kino adyny giridiň: "))
print(kinolar)

a = int(input('Bügin niçe adam bilen gepleşdiňiz?>>>'))
adamlar = []
for m in range(a):
    adamlar.append(input(f"{m+1}-nji gepleşen adamyňyz kimdi: "))
print(adamlar)