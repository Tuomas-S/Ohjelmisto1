from classes import *

name = input(f"{split} \n  Nimi: ")
age = input("  Ikä: ")
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
    player = user(name, age, koti)
    player.inventory = []
input("  [enter] = aloita peli ")

# Tähän intro.txt, seuraava rakenne on väliaikainen
input(f"{split} \n» On vapaapäivä. Olet juonut aamukahvisi ja koitat löytää \n  itsellesi tekemistä. Jo pitkään olet halunnut lukea jonkun kirjan. \n  Nykyään kun kaikki aika vietetään vain näytön äärellä koet, \n  että lukeminen tekisi aivoille hyvää. Lähdet etsimään itsellesi luettavaa. \n\n  [enter] = jatka ")
mission_current = "Löydä itsellesi luettavaa"

while kirjat not in player.inventory:
    player.menu(mission_current)
mission_current = "Palaa kotiin lukemaan"
input("\n» Noniin, nyt on aika mennä takaisiin kotiin lukemaan. ")


while kirjat.is_used == False:
    player.menu(mission_current)
input(f"{split} \n» Ai että nyt on vihdoin hyvä aika ottaa rennosti. \n  Nappaat kirjan käteen ja vietät loppupäivän lukemisen parissa. ")
input("\n  Voitit pelin!!") 