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
    input("\n  Olet alaikäinen, suljetaan sovellus... ")
    exit()
else:
    player = User(name, age, koti, "Pakkaa tavarasi mukaan", [])
    input(f"\n  Tervetuloa {name}! \n  [enter] = aloita peli ")

# Tähän intro.txt, seuraava rakenne on väliaikainen
input(f"{split} \n{format("Olet muuttanut uuteen kaupunkiin ja huomaat, ettei alueella ole mahdollisuutta minkäänlaiseen koulutukseen. Otat tehtäväksesi rakentaa kaupungin asukkaille laadukkaan koulun. Muista ottaa tavarasi mukaan ennen lähtöä.")} ")

while player.status == "Pakkaa tavarasi mukaan":
    player.status = tutorial(player)

while player.status == "Valitse rakennuspaikka":
    player.status = building_spot(player)

while player.status == "Hanki työkalut ja materiaalit":
    player.status = get_tools(player)

while player.status == "Hae rahaa":
    player.status = get_money(player)

while player.status == "Pelto valittu":
    player.status = clear_pelto(player)

while player.status == "Palaa maan päälle":
    player.status = escape_cellar(player)

while player.status == "Käy ostamassa materiaalit":
    player.status = buy_materials(player)

while player.status == "Rakenna koulu":
    player.status = finale(player)

while player.status == "Palaa kotiisi nukkumaan":
    player.status = ending(player)

if kirjat in player.inventory:
    if keskusta not in romua.usedIn and pelto not in romua.usedIn:
        input(f"{split} \n{format("Rakensit koulun ja koulutuksen laatu on erinomaista. Kaupungin asukkaat kuitenkin valittavat ruokalan puuttumisesta. Pisteet: 2/3.")} ")
    else:
        input(f"{split} \n{format("Rakensit koulun ja koulutuksen laatu on erinomaista. Kaupungin asukkaat ovat tyytyväisiä uuteen ruokalaan. Pisteet: 3/3.")} ")
else:
    if keskusta not in romua.usedIn and pelto not in romua.usedIn:
        input(f"{split} \n{format("Rakensit koulun, mutta koulutuksessa on puutteita. Kaupungin asukkaat valittavat myös ruokalan puuttumisesta. Pisteet: 1/3.")} ")
    else:
        input(f"{split} \n{format("Rakensit koulun, mutta koulutuksessa on puutteita. Olet saanut kuitenkin kehuja maistuvasta ruuasta. Pisteet: 2/3.")} ")