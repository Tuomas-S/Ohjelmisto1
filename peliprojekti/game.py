from classes import *
from missions import *

name = input(f"{split} \n  Nimi: ")
age = input("  Ikä:  ")
while True:
    try:
        int(age)
    except ValueError:
        age = input("  Anna oikea ikä: ")
    else:
        break
age = int(age)
if age < 12:
    input("\n  Olet alaikäinen, suljetaan sovellus...")
    exit()
else:
    print(f"\n  Tervetuloa {name}!")
    player = User(name, age, koti, "Pakkaa tavarasi mukaan")
    player.inventory = []

input("  [enter] = aloita peli ")
# Tähän intro.txt, seuraava rakenne on väliaikainen
input(f"{split} \n{format("Olet muuttanut uuteen kaupunkiin ja huomaat, ettei alueella ole mahdollisuutta minkäänlaiseen koulutukseen. Otat tehtäväksesi rakentaa kaupungin asukkaille laadukkaan koulun. Muista ottaa tavarasi mukaan ennen lähtöä. ")}")

while player.status == "Pakkaa tavarasi mukaan":
    player.status = tutorial(player)

while player.status == "Tutoriaali valmis":
    player.status = building_spot(player)

input(player.status)
while True:
    player.menu("Testaile")