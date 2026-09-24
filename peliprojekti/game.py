from classes import *

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
    player = User(name, age, koti)
    player.inventory = []
input("  [enter] = aloita peli ")

# Tähän intro.txt, seuraava rakenne on väliaikainen
input(f"{split} \n» On vapaapäivä. Olet juonut aamukahvisi ja koitat löytää \n  itsellesi tekemistä. Jo pitkään olet halunnut lukea jonkun kirjan. \n  Nykyään kun kaikki aika vietetään vain näytön äärellä koet, \n  että lukeminen tekisi aivoille hyvää. Lähdet etsimään itsellesi luettavaa. \n\n  [enter] = jatka ")

missionCurrent = "Löydä itsellesi luettavaa"
while kirjat not in player.inventory:
    player.menu(missionCurrent)
    if työkalut in player.inventory and keskusta not in työkalut.usedIn:
        input("\n» No nyt kun kerran ostit työkaluja saat luvan \n  rakentaa jotain hienoa. ")
        missionCurrent = "Rakenna jotain siistiä"
        koti.isLocked = kauppa.isLocked = True
        while keskusta not in työkalut.usedIn:
            player.menu(missionCurrent)
        missionCurrent = "Löydä itsellesi luettavaa"
        input("\n» Olipa urakka.. Tällä kertaa kannattaa oikeasti \n  löytää sitä luettavaa. ")
        koti.isLocked = False
input("\n» Noniin, nyt on aika mennä takaisiin kotiin lukemaan. ")

missionCurrent = "Lue kirjoja"
keskusta.isLocked = kauppa.isLocked = True
while koti not in kirjat.usedIn:
    player.menu(missionCurrent)
input("\n» Viet kirjat varastoon ja painut takaisin nukkumaan. ")
input("\n  Voitit pelin!!") 

