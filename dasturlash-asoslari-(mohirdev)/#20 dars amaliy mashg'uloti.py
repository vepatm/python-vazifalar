def data_collection(name, surname, age, date_of_birth, hometown, e_mail=None, phone_number=None):
    data = {
        'name': name,
        'surname': surname,
        'age': age,
        'date_of_birth': date_of_birth,
        'hometown': hometown,
        'e_mail': e_mail,
        'phone_number': phone_number
    }
    return data
users = []
while True:
    name = input("Ismi: ")
    surname = input("Familiyasi: ")
    age = input("Yosh: ")
    date_of_birth = input("Tug'ilgan yili: ")
    hometown = input("Tug'ilgan joyi: ")
    e_mail = input("Elektron pochta manzili: ")
    phone_number = input("Telefon raqami: ")
    users.append(data_collection(name, surname, age, date_of_birth,hometown, e_mail, phone_number))
    answer = input("Yana foydalanuvchi qo'shasizmi? (yes/no): ")
    if answer == 'no':
        break
print("\nTizimdagi foydalanuvchilar: \n")
for data in users:
    if data['e_mail']:
        e_mail = data['e_mail']
    else:
        e_mail = "Noma'lum"
    if data['phone_number']:
        phone_number = data['phone_number']
    else:
        phone_number = "No'ma'lum"
    print(f"Ismi va familiyasi: {data['name'].title()} {data['surname'].title()}\n"
          f"Hozir {data['age']} yoshda\n"
          f"{data['date_of_birth']}-yilda "
          f"{data['hometown'].capitalize()} da tug'ilgan\n"
          f"Elektron pochta manzili: {e_mail.title()}\n"
          f"Telefon raqami: {phone_number}\n")

sonlar = []
for i in range(3):
    son = int(input(f"{i+1}-sonni kiriting: "))
    sonlar.append(son)
def eng_katta_son(toplam):
    a = max(toplam)
    return a
max = eng_katta_son(sonlar)
print(max)

import math
radius = int(input("r = "))
def circle_r_d_p_s(r):
    circle_options = {
        'radius': r,
        'diametr': 2*r,
        'perimetr': math.pi*2*r,
        'yuza': math.pi*(r**2)
    }
    return circle_options
circle = circle_r_d_p_s(radius)
print(f"Aylana radiusi: {circle['radius']}\n"
      f"Aylana diametri: {circle['diametr']}\n"
      f"Aylana perimetri: {circle['perimetr']}\n"
      f"Aylana yuzi: {circle['yuza']}")

def tub_sonlar(son1,son2):
    while son1<son2+1:
        tub_sonlar = []
        for i in range(son1,son2):
            s = 0
            for j in range(1,i+1):
                if i % j == 0:
                    s += 1
            if s == 2:
                  tub_sonlar.append(i)
        son1 += 1
        return tub_sonlar
bir = int(input("Oraliqning birnchi raqamini kiriting: "))
ikki = int(input("Oraliqning ikkinchi raqamini kiritingL: "))
t_sonlar = tub_sonlar(bir,ikki)
print(t_sonlar)

def fibionacci(son):
    toplam = []
    toplam.append(1)
    toplam.append(1)
    for i in range(2,son):
        toplam.append(toplam[i-1]+toplam[i-2])
    return toplam
n = int(input("n = "))
fibionacci_sonlari = fibionacci(n)
print(fibionacci_sonlari)