split = "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━▶\n"

import time
import random

class item:
    def __init__(self, name, found_text, is_heavy = False, is_used = False):
        self.name = name # esineen nimi
        self.found_text = found_text # tämä tulostuu esineen löytyessä
        self.is_heavy = is_heavy # voiko esineen ottaa vain apuvälineen kanssa
        self.is_used = is_used # onko pelaaja käyttänyt esineen
        
class location:
    def __init__(self, name, search_text, item = None, accepts_item = None, connections = None):
        self.name = name # sijainnin nimi
        self.search_text = search_text # tämä tulostetaan kun sijaintia tutkitaan
        self.item = item # sijainnista löytyvä esine
        self.accepts_item = accepts_item # mitä esinettä sijainnissa voi käyttää
        self.connections = connections # lista paikoista mihin tästä sijainnista pääsee

class user:
    def __init__(self, name, age, location, inventory = None, can_carry = False):
        self.name = name # pelaajan asettama nimi
        self.age = age # pelaajan asettama ikä
        self.inventory = inventory # inventaario
        self.location = location # nykyinen sijainti
        self.can_carry = can_carry # voiko lisätä painavia esineitä inventaarioon

    def move(self, move_to):
        has_moved = False
        while has_moved == False:
            print(f"{split} \n╭─────────────────────────────────────────────╮ \n│ Voit siirtyä seuraaviin paikkoihin:         │")
            for location in move_to.connections:
                print(f"│ » {location.name:<42}│")
            choice = input("╰─────────────────────────────────────────────╯ \n\nLiiku paikkaan kirjoittamalla sen nimi. \n[enter] = takaisin \n\nValitse toiminto: ")
            if choice == "":
                has_moved = True
                break
            else:
                for location in move_to.connections:
                    if choice.lower() == location.name.lower():
                        print("Siirrytään...")
                        time.sleep(random.randrange(1, 3))
                        self.location = location
                        has_moved = True
                        break
                else:
                    input(f"{split} \nSijaintia ei löytynyt. ")

    def search(self, location):
        if location.item != None:
            if location.item.is_heavy == True and self.can_carry == False:
                print(f"{split} \n{location.search_text}")
                input("\n  Esimerkkiteksti kun löydät raskaan esineen...")
            else:
                input(f"{split} \n» {location.search_text} ")
                input(f"\n» {location.item.found_text} ")
                self.inventory.append(location.item)
                location.item = None
        else:
            input(f"{split} \n» {location.search_text}")
            input("\n  Et löytänyt alueelta mitään merkittävää. ")

    def item_use(self, choice):
        if choice.lower() == "kartta":
            print(f"{split} \n  Avataan kartta...")
            time.sleep(random.randrange(1, 3))
            input(f"\n\n╭───────────────════════════════════───────═════╗ \n│           皿  ⌂ ⌂                         ^   ║ \n║    ╭╌╌ [ Keskusta ] ──┬── [ Koti ]        N   ║ \n║    ┆        ║ ⌂⌂      │       ┆              ─╢ \n│ [ Kuja ]  ⌂ ║         ╰── [ Metsä ] ╌╌╌╮      │ \n│    ┆        ║              ♣Ψ │ ♣      ┆      │ \n║    ┆    [ Kauppa ]          ♣ │    [ Raunio ] ║ \n╠═   ┆                          │ Ψ      ┆      ║ \n║    ╰╌ [ ??? ] † †        [ Niitty ] ╌╌╌╯      ║ \n║                †      ▲▲              ~~~     │ \n╚═════════─────════════─────────────────────────╯ \n\n  [⌂] SIJAINTI: {self.location.name} \n  [enter] = takaisin ")
            return(False)
        else:
            for item in self.inventory:
                if choice.lower() == item.name.lower():
                    if item == self.location.accepts_item:
                        print("  Käytetään esine...")
                        time.sleep(random.randrange(1, 3))
                        item.is_used = True
                        self.inventory.remove(item)
                        return(True)
                    else:
                        input(f"{split} \n  Et voi käyttää esinettä juuri nyt. ")
                        return(False)
            else:
                input(f"{split} \n  Esinettä ei löytynyt inventaariostasi. ")
                return(False)

    def inv_show(self):
        is_used = False
        while is_used == False:
            if self.inventory == []:
                input(f"{split} \nInventaariosi on tyhjä. Täältä näet löytämäsi esineet. \n\n[enter] = takaisin \n\nValitse toiminto: ")
                break
            else:
                print(f"{split} \n╭─────────────────────────────────────────╮ \n│ Inventaariossasi on:                    │")
                for item in self.inventory:
                    print(f"│ » {item.name:<38}│")
                choice = input("╰─────────────────────────────────────────╯ \n\n  Käytä esine kirjoittamalla sen nimi. \n  [enter] = takaisin \n\n  Valitse toiminto: ")
                if choice == "":
                    break
                else:
                    is_used = self.item_use(choice)

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
            input(f"{split} \nKyseistä toimintoa ei löydy. Valitse toiminto \nkirjoittamalla sitä vastaava numero. ")

# Luodaan esineet, huoneet ja pelaaja
kartta = item("Kartta", "Löysit kartan. Tästä voi olla paljon hyötyä.", None)
kirjat = item("Kirjat", "Löysit kadun nurkassa olevasta laatikosta muutaman kirjan. \n  Historiaa, pokkareita, kauhua ja muuta jännää.")
romu = item
lappu = item
kärryt = item
rakennusvälineet = item("Rakennusvälineet", "Ostat työvälineitä, lautaa sekä kottikärryt. \n  Voit kantaa nyt raskaita esineitä")


koti = location("Koti", "Kotisi näyttää ihanan tunnelmalliselta. Tahtoisit mennä \n  takaisin nukkumaan, mutta sinulla riittää vielä tekemistä.", kartta, kirjat)
keskusta = location("Keskusta", "Kaupunki on täynnä vilinää ja melua. Nauttisit mieluummin \n  ajastasi luonnossa. No... Ei voi mitään.", kirjat)
kauppa = location("Kauppa", "Kaupan hyllyt ovat täynnä rakennusmateriaaleja \n  ja työkaluja. Juttelet hetken kauppiaan kanssa.", rakennusvälineet)
metsä = location
raunio = location
niitty = location
varasto = location

keskusta.connections = [kauppa, koti]
koti.connections = [keskusta]
kauppa.connections = [keskusta]