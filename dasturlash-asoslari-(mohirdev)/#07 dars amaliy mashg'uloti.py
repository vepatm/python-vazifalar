ismlar = ['Xudoyor', 'Nodirbek', 'Dilshod']
print('Salom ' + ismlar[0] + ', bugun choyxona bormi?')
print(ismlar[1] + ' choyxonaga boramizmi?')
print(ismlar[2] + ' soat nechiga edi choyxona')

sonlar = [6, -3, 3.6]
print(sonlar[0] + sonlar[1])
print(sonlar[1] - sonlar[2])

sonlar[0] = 4
sonlar[1] = 6
print(sonlar)

t_shaxslar = ['Muhammad sollallohu alyhi vasallam', 'Imom Buxoriy', 'Abu Nasr Forobiy']
z_shaxslar = ['Muhammadali Eshonqulov', 'Ilon Musk', 'Temurbek Adhamov', 'Bil Gates']
t_shaxs = t_shaxslar.pop(0)
z_shaxs = z_shaxslar.pop(2)
print(f"Men tarixiy shaxslardan {t_shaxs} bilan, zamonaviy shaxlardan {z_shaxs} bilan suhbat qilishni istar edim")

friends = []
friends.append('Xudoyor')
friends.append('Azamat')
friends.append('Nodirbek')
friends.append('Ravshan')
friends.append('Dilshod')
print(friends)

friends.remove('Azamat')
friends.insert(0, 'Ahmad')
friends.insert(5, 'Sanjar')
print(friends)
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(4))
mehmonlar.append(friends.pop(5))
print(mehmonlar)