# Zadanie 1
punkty = float(input("Podaj liczbę punktów: "))
if punkty > 80:
    print("Zaliczyłeś egzamin w terminie 0")
elif 50 <= punkty <= 80:
    print("Możesz poprawić wynik")
else:
    print("Musisz poprawić egzamin")

# Zadanie 2
x = float(input("Podaj x: "))
y = float(input("Podaj y: "))
z = float(input("Podaj z: "))
if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y
print(x, y, z)

# Zadanie 3
Nazwa_pliku = 'Raport_maj.xlsx'
if Nazwa_pliku.endswith('.xlsx'):
    print('Tak')
else:
    print('Nie')

# Zadanie 5a
with open('notowania_gieldowe.txt', 'r', encoding='utf-8') as plik:
    for linia in plik:
        print(linia.strip())

# Zadanie 5b
with open('notowania_gieldowe.txt', 'a', encoding='utf-8') as plik:
    plik.write('\nALR, 113')
with open('notowania_gieldowe.txt', 'r', encoding='utf-8') as plik:
    for linia in plik:
        print(linia.strip())

# Zadanie 6
litera = input("Podaj literę: ")
if litera.isupper():
    print("Duża litera")
elif litera.islower():
    print("Mała litera")
else:
    print("To nie jest litera")

# Zadanie 7
Hasło = 'pk47!jy0893'
if len(Hasło) == 11 and '!' in Hasło:
    print("Hasło jest poprawne")
else:
    print("Hasło jest nie poprawne")

# Zadanie 8
text = 'Studiuje-Informatykę'
print(text[:3])
print(text[-2:])