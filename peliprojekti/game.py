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
    player = User(name, age, koti)
    player.inventory = []
input("  [enter] = aloita peli ")

# Tähän intro.txt, seuraava rakenne on väliaikainen
input(f"{split} \n» On vapaapäivä. Olet juonut aamukahvisi ja koitat löytää \n  itsellesi tekemistä. Jo pitkään olet halunnut lukea jonkun kirjan. \n  Nykyään kun kaikki aika vietetään vain näytön äärellä koet, \n  että lukeminen tekisi aivoille hyvää. Lähdet etsimään itsellesi luettavaa. \n\n  [enter] = jatka ")

mission_current = "Löydä itsellesi luettavaa"
while kirjat not in player.inventory:
    player.menu(mission_current)
    if työkalut in player.inventory and työkalut.is_used == False:
        input("\n» No nyt kun kerran ostit työkaluja saat luvan \n  rakentaa jotain hienoa. ")
        mission_current = "Rakenna jotain siistiä"
        while työkalut.is_used == False:
            player.menu(mission_current)
        keskusta.accepts_item.remove(työkalut)
        mission_current = "Löydä itsellesi luettavaa"
        input("\n» Olipa urakka.. Tällä kertaa kannattaa oikeasti \n  löytää sitä luettavaa. ")
input("\n» Noniin, nyt on aika mennä takaisiin kotiin lukemaan. ")

mission_current = "Palaa kotiin lukemaan"
while kirjat.is_used == False:
    player.menu(mission_current)
input("\n» Se siitä kirjojen lukemisesta... \n  Viet kirjat varastoon ja painut takaisin pehkuihin. ")
input("\n  Voitit pelin!!") 

