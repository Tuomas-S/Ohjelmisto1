split = "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━▶\n"

import time
import random
from descriptions import *

class Item:
    def __init__(self, name, item_found, use_success, use_fail, is_single_use, is_used = False):
        self.name = name # esineen nimi
        self.item_found = item_found # tämä tulostuu esineen löytyessä
        self.use_success = use_success # tämä tulostuu kun esinettä käytetään
        self.use_fail = use_fail # tämä tulostuu kun esinettä ei voi käyttää
        self.is_single_use = is_single_use # onko esine kertakäyttöinen
        self.is_used = is_used # onko pelaaja käyttänyt esineen
        
class Location:
    def __init__(self, name, search_text, item = None, accepts_item = None, connections = None):
        self.name = name # sijainnin nimi
        self.search_text = search_text # tämä tulostetaan kun sijaintia tutkitaan
        self.item = item # sijainnista löytyvä esine
        self.accepts_item = accepts_item # mitä esinettä sijainnissa voi käyttää
        self.connections = connections # lista paikoista mihin tästä sijainnista pääsee

class User:
    def __init__(self, name, age, location, inventory = None):
        self.name = name # pelaajan asettama nimi
        self.age = age # pelaajan asettama ikä
        self.inventory = inventory # inventaario
        self.location = location # nykyinen sijainti

    def move(self, move_to):
        has_moved = False
        while has_moved == False:
            print(f"{split} \n╭─────────────────────────────────────────────╮ \n│ Voit siirtyä seuraaviin paikkoihin:         │")
            for location in move_to.connections:
                print(f"│ » {location.name:<42}│")
            choice = input("╰─────────────────────────────────────────────╯ \n\n  Liiku paikkaan kirjoittamalla sen nimi. \n  [enter] = takaisin \n\n  Valitse toiminto: ")
            if choice == "":
                has_moved = True
                break
            else:
                for location in move_to.connections:
                    if choice.lower() == location.name.lower():
                        print("  Siirrytään...")
                        time.sleep(random.randrange(1, 3))
                        self.location = location
                        has_moved = True
                        break
                else:
                    input(f"{split} \n  Sijaintia ei löytynyt. ")

    def search(self, location):
        if location.item != None:
            input(f"{split} \n{location.search_text} ")
            input(f"\n{location.item.item_found} ")
            self.inventory.append(location.item)
            location.item = None
        else:
            input(f"{split} \n{location.search_text}")
            input("\n  Et löytänyt alueelta mitään mukaan otettavaa. ")

    def item_use(self, choice):
        for item in self.inventory:
            if choice.lower() == item.name.lower():
                if item in self.location.accepts_item:
                    print("  Käytetään esine...")
                    time.sleep(random.randrange(1, 3))
                    input(f"{split} \n{item.use_success} ")
                    item.is_used = True
                    if item.is_single_use == True:
                        self.inventory.remove(item)
                    return(True)
                else:
                    print("  Käytetään esine...")
                    time.sleep(random.randrange(1, 3))
                    input(f"{split} \n{item.use_fail} ")
                    return(False)
        else:
            input(f"{split} \n  Esinettä ei löytynyt inventaariostasi. ")
            return(False)

    def inv_show(self):
        an_item_was_used = False
        while an_item_was_used == False:
            if self.inventory == []:
                input(f"{split} \n╭───────────────────────────────────────╮ \n│ Inventaariosi on tyhjä.               │ \n│ Täältä näet löytämäsi esineet.        │ \n╰───────────────────────────────────────╯ \n\n  [enter] = takaisin ")
                break
            else:
                print(f"{split} \n╭─────────────────────────────────────────╮ \n│ Inventaariossasi on:                    │")
                for item in self.inventory:
                    print(f"│ » {item.name:<38}│")
                choice = input("╰─────────────────────────────────────────╯ \n\n  Käytä esine kirjoittamalla sen nimi. \n  [enter] = takaisin \n\n  Valitse toiminto: ")
                if choice == "":
                    break
                else:
                    an_item_was_used = self.item_use(choice)

    def menu(self, mission):
        print(f"{split} \n╭─────────────────────────────────────────────────────╮ \n│ [⌂] SIJAINTI: {self.location.name:<38}│ \n│ [≡] TEHTÄVÄ:  {mission:<38}│ \n╰─────────────────────────────────────────────────────╯ \n\n  [1] = Vaihda sijaintia \n  [2] = Tutki aluetta \n  [3] = Avaa inventaario \n  [4] = Sulje peli")
        choice = input("\n  Valitse toiminto: ")
        if choice == "1":
            self.move(self.location)
        elif choice == "2":
            print("  Tutkitaan aluetta...")
            time.sleep(random.randrange(1,3))
            self.search(self.location)
        elif choice == "3":
            print("  Avataan inventaario...")
            time.sleep(1)
            self.inv_show()
        elif choice == "4":
            confirm = input(f'{split} \n╭────────────────────────────────────╮ \n│ Suljetaako peli?                   │ \n╰────────────────────────────────────╯ \n\n  Kirjoita "ok" vahvistaaksesi. \n  [enter] = peruuta \n\n  Valitse toiminto: ')
            if confirm.lower() == "ok":
                exit()
        else:
            input(f"{split} \n  Kyseistä toimintoa ei löydy. Valitse toiminto \n  kirjoittamalla sitä vastaava numero. ")

# Luodaan esineet, huoneet ja pelaaja
kartta = Item("Kartta", kartta_found, kartta_success, kartta_fail, False)
kirjat = Item("Kirjat", kirjat_found, kirjat_success, kirjat_fail, True)
romu = Item
kärryt = Item
työkalut = Item("Työkalut", työkalut_found, työkalut_success, työkalut_fail, False)


koti = Location("Koti", koti_search, kartta)
keskusta = Location("Keskusta", keskusta_search, kirjat)
kauppa = Location("Kauppa", kauppa_search, työkalut)
metsä = Location
raunio = Location
niitty = Location
varasto = Location

keskusta.connections = [kauppa, koti]
keskusta.accepts_item = [kartta, työkalut]
koti.connections = [keskusta]
koti.accepts_item = [kartta, kirjat]
kauppa.connections = [keskusta]
kauppa.accepts_item = [kartta]