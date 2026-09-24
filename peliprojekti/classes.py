split = "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━▶\n"

import time
import random

class Item:
    def __init__(self, name, itemFound, useText):
        self.name = name # esineen nimi
        self.itemFound = itemFound # tämä tulostuu esineen löytyessä
        self.useText = useText # tämä tulostuu kun esinettä käytetään

class Functional(Item):
    def __init__(self, name, itemFound, useText, useFail, isSingleUse, usedIn = None):
        super().__init__(name, itemFound, useText)
        self.useFail = useFail # tämä tulostuu kun esinettä ei voi käyttää
        self.isSingleUse = isSingleUse # onko esine kertakäyttöinen
        self.usedIn = usedIn # missä sijainnissa esine on käytetty (lista)

        
class Location:
    def __init__(self, name, searchText, isLocked, lockedText, item = None, acceptsItem = None, connections = None):
        self.name = name # sijainnin nimi
        self.searchText = searchText # tämä tulostetaan kun sijaintia tutkitaan
        self.isLocked = isLocked # onko pelaajalla pääsyä sijaintiin vai ei
        self.lockedText = lockedText # tämä tulostuu jos koitetaan siirtyä lukittuun sijaintiin
        self.item = item # sijainnista löytyvä esine
        self.acceptsItem = acceptsItem # mitä esinettä sijainnissa voi käyttää
        self.connections = connections # lista paikoista mihin tästä sijainnista pääsee

class User:
    def __init__(self, name, age, location, inventory = None):
        self.name = name # pelaajan asettama nimi
        self.age = age # pelaajan asettama ikä
        self.inventory = inventory # inventaario
        self.location = location # nykyinen sijainti

    def move(self, ownLocation):
        hasMoved = False
        while hasMoved == False:
            print(f"{split} \n╭─────────────────────────────────────────────╮ \n│ Voit siirtyä seuraaviin paikkoihin:         │")
            for location in ownLocation.connections:
                print(f"│ » {location.name:<42}│")
            choice = input("╰─────────────────────────────────────────────╯ \n\n  Liiku paikkaan kirjoittamalla sen nimi. \n  [enter] = takaisin \n\n  Valitse toiminto: ")
            if choice == "":
                hasMoved = True
                break
            else:
                for location in ownLocation.connections:
                    if choice.lower() == location.name.lower():
                        if location.isLocked:
                            input(f"{split} \n{location.lockedText} ")
                            break
                        print("  Siirrytään...")
                        time.sleep(random.randrange(1, 3))
                        self.location = location
                        hasMoved = True
                        break
                else:
                    input(f"{split} \n  Sijaintia ei löytynyt. ")

    def search(self, location):
        if location.item != None:
            input(f"{split} \n{location.searchText} ")
            input(f"\n{location.item.itemFound} ")
            self.inventory.append(location.item)
            location.item = None
        else:
            input(f"{split} \n{location.searchText}")
            input("\n  Et löytänyt alueelta mitään mukaan otettavaa. ")

    def item_use(self, choice):
        for item in self.inventory:
            if choice.lower() == item.name.lower():
                if isinstance(item, Functional):
                    if item in self.location.acceptsItem:
                        if item.usedIn == self.location:
                            input(f"{split} \n  Olet jo käyttänyt esineen tässä paikassa. ")
                            return(False)
                        print("  Käytetään esine...")
                        time.sleep(random.randrange(1, 3))
                        input(f"{split} \n{item.useText} ")
                        item.usedIn.append(self.location)
                        if item.isSingleUse:
                            self.inventory.remove(item)
                        return(True)
                    else:
                        input(f"{split} \n{item.useFail} ")
                        return(False)
                else:
                    print("  Käytetään esine...")
                    time.sleep(random.randrange(1, 3))
                    input(f"{split} \n{item.useText} ")
                    return(True)
        else:
            input(f"{split} \n  Esinettä ei löytynyt inventaariostasi. ")
            return(False)

    def inv_show(self):
        itemUsed = False
        while itemUsed == False:
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
                    itemUsed = self.item_use(choice)

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
kirjat.usedIn = []
romu = Functional
kärryt = Item
työkalut = Functional("Työkalut", "» Ostat työvälineitä, lautaa sekä kottikärryt. \n  Voit kantaa nyt raskaita esineitä.", "» Nikkaroit keskustaan yhen talon. Aika siistii!", "» Et voi rakentaa tähän.", False)
työkalut.usedIn = []

#name, searchText, isLocked, lockedText, item = None, acceptsItem = None, connections = None
koti = Location("Koti", "» Kotisi näyttää ihanan tunnelmalliselta. Tahtoisit mennä \n  takaisin nukkumaan, mutta sinulla riittää vielä tekemistä.", False, "» Et halua palata vielä kotiin, sillä sinulla on \n  vielä asioita hoidettavana.", kartta)
keskusta = Location("Keskusta", "» Kaupunki on täynnä vilinää ja melua. Nauttisit mieluummin \n  ajastasi luonnossa. No... Ei voi mitään.", False, "» Nyt on jo niin myöhäistä ettet halua enää lähteä ulos.", kirjat)
kauppa = Location("Kauppa", "» Kaupan hyllyt ovat täynnä rakennusmateriaaleja \n  ja työkaluja. Juttelet hetken kauppiaan kanssa.", False, "» Et tarvitse kaupasta enää mitään.", työkalut)
metsä = Location
raunio = Location
niitty = Location
varasto = Location

keskusta.connections = [kauppa, koti]
keskusta.acceptsItem = [kartta, työkalut]
koti.connections = [keskusta]
koti.acceptsItem = [kartta, kirjat]
kauppa.connections = [keskusta]
kauppa.acceptsItem = [kartta]