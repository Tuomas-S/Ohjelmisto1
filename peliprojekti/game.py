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

mission_current = "Löydä itsellesi luettavaa"
while kirjat not in player.inventory:
    player.menu(mission_current)
    if työkalut in player.inventory and keskusta not in työkalut.used_in:
        input("\n» No nyt kun kerran ostit työkaluja saat luvan \n  rakentaa jotain hienoa. ")
        mission_current = "Rakenna jotain siistiä"
        koti.is_locked = kauppa.is_locked = True
        while keskusta not in työkalut.used_in:
            player.menu(mission_current)
        mission_current = "Löydä itsellesi luettavaa"
        input("\n» Olipa urakka.. Tällä kertaa kannattaa oikeasti \n  löytää sitä luettavaa. ")
        koti.is_locked = False
input("\n» Noniin, nyt on aika mennä takaisiin kotiin lukemaan. ")

mission_current = "Lue kirjoja"
keskusta.is_locked = kauppa.is_locked = True
while koti not in kirjat.used_in:
    player.menu(mission_current)
input("\n» Viet kirjat varastoon ja painut takaisin nukkumaan. ")
input("\n  Voitit pelin!!") 

