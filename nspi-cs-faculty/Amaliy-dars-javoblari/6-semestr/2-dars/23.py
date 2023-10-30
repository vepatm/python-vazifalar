N = int(input("N sekundni kiriting: "))
soat = N // 3600
minut = (N - soat * 3600) // 60
sekund = N - soat * 3600 - minut * 60

print(f"{N} sekund {soat} soat, {minut} minut, {sekund} sekundga teng")