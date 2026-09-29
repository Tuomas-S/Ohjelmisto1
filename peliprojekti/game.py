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
    player = User(name, age, koti, "Tutoriaali", [])

input("  [enter] = aloita peli ")
# Tähän intro.txt, seuraava rakenne on väliaikainen
input(f"{split} \n{format("Olet muuttanut uuteen kaupunkiin ja huomaat, ettei alueella ole mahdollisuutta minkäänlaiseen koulutukseen. Otat tehtäväksesi rakentaa kaupungin asukkaille laadukkaan koulun. Muista ottaa tavarasi mukaan ennen lähtöä. ")}")

while player.status == "Tutoriaali":
    player.status = tutorial(player)

while player.status == "Tutoriaali valmis":
    player.status = building_spot(player)

while player.status == "Kaupunki valittu":
    player.status = get_tools(player)

while player.status == "Pelto valittu":
    player.status = clear_area(player)

while player.status == "Lukossa kellarissa":
    player.status = cellar_escape(player)

while player.status == "Kauppaan ostoksille":
    player.status = buy_materials(player)

while player.status == "Finaali":
    player.status = finale(player)