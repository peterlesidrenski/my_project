pileshki_menqta = int(input())
riba= int(input())
vegeterian = int(input())

pile6ki_ceni = pileshki_menqta * 10.35
ribe6ko = riba * 12.40
veg = vegeterian * 8.15

cena = pile6ki_ceni + ribe6ko + veg
desert = (20 / 100) * cena


cena_real = cena + desert + 2.5
print(cena_real)