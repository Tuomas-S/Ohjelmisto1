split = "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━▶\n"

import time
import random

class Item:
    def __init__(self, name, item_found, use_text):
        self.name = name # esineen nimi
        self.item_found = item_found # tämä tulostuu esineen löytyessä
        self.use_text = use_text # tämä tulostuu kun esinettä käytetään

class Functional(Item):
    def __init__(self, name, item_found, use_text, use_fail, is_single_use, used_in = None):
        super().__init__(name, item_found, use_text)
        self.use_fail = use_fail # tämä tulostuu kun esinettä ei voi käyttää
        self.is_single_use = is_single_use # onko esine kertakäyttöinen
        self.used_in = used_in # missä sijainnissa esine on käytetty (lista)

        
class Location:
    def __init__(self, name, search_text, is_locked, locked_text, item = None, accepts_item = None, connections = None):
        self.name = name # sijainnin nimi
        self.search_text = search_text # tämä tulostetaan kun sijaintia tutkitaan
        self.is_locked = is_locked # onko pelaajalla pääsyä sijaintiin vai ei
        self.locked_text = locked_text # tämä tulostuu jos koitetaan siirtyä lukittuun sijaintiin
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
                        if location.is_locked:
                            input(f"{split} \n{location.locked_text} ")
                            break
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
                if isinstance(item, Functional):
                    if item in self.location.accepts_item:
                        if item.used_in == self.location:
                            input(f"{split} \n  Olet jo käyttänyt esineen tässä paikassa. ")
                            return(False)
                        print("  Käytetään esine...")
                        time.sleep(random.randrange(1, 3))
                        input(f"{split} \n{item.use_text} ")
                        item.used_in.append(self.location)
                        if item.is_single_use:
                            self.inventory.remove(item)
                        return(True)
                    else:
                        input(f"{split} \n{item.use_fail} ")
                        return(False)
                else:
                    print("  Käytetään esine...")
                    time.sleep(random.randrange(1, 3))
                    input(f"{split} \n{item.use_text} ")
                    return(True)
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
kartta = Item("Kartta", "» Löysit kartan. Tästä voi olla paljon hyötyä.", "╭───────────────════════════════════───────═════╗ \n│           皿  ⌂ ⌂                         ^   ║ \n║    ╭╌╌ [ Keskusta ] ──┬── [ Koti ]        N   ║ \n║    ┆        ║ ⌂⌂      │       ┆              ─╢ \n│ [ Kuja ]  ⌂ ║         ╰── [ Metsä ] ╌╌╌╮      │ \n│    ┆        ║              ♣Ψ │ ♣      ┆      │ \n║    ┆    [ Kauppa ]          ♣ │    [ Raunio ] ║ \n╠═   ┆                          │ Ψ      ┆      ║ \n║    ╰╌ [ ??? ] † †        [ Niitty ] ╌╌╌╯      ║ \n║                †      ▲▲              ~~~     │ \n╚═════════─────════════─────────────────────────╯ \n\n» Kartta kaikista kaupungin sijainneista. \n  Jotkut sijainnit eivät ole aina saatavilla.")
kirjat = Functional("Kirjat", "» Löysit kadun nurkassa olevasta laatikosta muutaman kirjan. \n  Historiaa, pokkareita, kauhua ja muuta jännää.", "» Luet kirjoja. Pettymykseksesi ne ovat kirjoitettu hepreaksi. \n  Suljet kirjat ja päätät tehdä tehdä jotain muuta.", "» Kotona sitten luetaan. Nyt ei ole aikaa sille...", True)
kirjat.used_in = []
romu = Functional
kärryt = Item
työkalut = Functional("Työkalut", "» Ostat työvälineitä, lautaa sekä kottikärryt. \n  Voit kantaa nyt raskaita esineitä.", "» Nikkaroit keskustaan yhen talon. Aika siistii!", "» Et voi rakentaa tähän.", False)
työkalut.used_in = []

#name, search_text, is_locked, locked_text, item = None, accepts_item = None, connections = None
koti = Location("Koti", "» Kotisi näyttää ihanan tunnelmalliselta. Tahtoisit mennä \n  takaisin nukkumaan, mutta sinulla riittää vielä tekemistä.", False, "» Et halua palata vielä kotiin, sillä sinulla on \n  vielä asioita hoidettavana.", kartta)
keskusta = Location("Keskusta", "» Kaupunki on täynnä vilinää ja melua. Nauttisit mieluummin \n  ajastasi luonnossa. No... Ei voi mitään.", False, "» Nyt on jo niin myöhäistä ettet halua enää lähteä ulos.", kirjat)
kauppa = Location("Kauppa", "» Kaupan hyllyt ovat täynnä rakennusmateriaaleja \n  ja työkaluja. Juttelet hetken kauppiaan kanssa.", False, "» Et tarvitse kaupasta enää mitään.", työkalut)
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