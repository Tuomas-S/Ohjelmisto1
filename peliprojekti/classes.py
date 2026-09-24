import time
import random
import textwrap

# Tekstin formatointia
split = "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━▶\n"
def format(text):
    lines = textwrap.wrap(text, width=64)
    return "» " + "\n  ".join(lines)

# Luodaan luokat
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
        self.usedIn = usedIn # missä sijainnissa esine on käytetty (joukko)

class Location:
    def __init__(self, name, searchText, isLocked, lockedText, item, acceptsItem, connections = None):
        self.name = name # sijainnin nimi
        self.searchText = searchText # tämä tulostetaan kun sijaintia tutkitaan
        self.isLocked = isLocked # onko pelaajalla pääsyä sijaintiin vai ei
        self.lockedText = lockedText # tämä tulostuu jos koitetaan siirtyä lukittuun sijaintiin
        self.item = item # sijainnista löytyvät esineet (lista)
        self.acceptsItem = acceptsItem # mitä esinettä sijainnissa voi käyttää
        self.connections = connections # joukko paikoista mihin tästä sijainnista pääsee

class User:
    def __init__(self, name, age, location, status, inventory = None,):
        self.name = name # pelaajan asettama nimi
        self.age = age # pelaajan asettama ikä
        self.location = location # nykyinen sijainti
        self.status = status # pelaajan tämänhetkinen tilanne
        self.inventory = inventory # inventaario

    # Pelaajan liikkuminen listasta valittuun sijaintiin
    def move(self, ownLocation):
        hasMoved = False
        while hasMoved == False:
            print(f"{split} \n╭─────────────────────────────────────────────╮ \n│ Voit siirtyä seuraaviin paikkoihin:         │")
            for i in ownLocation.connections:
                print(f"│ » {i.name:<42}│")
            choice = input("╰─────────────────────────────────────────────╯ \n\n  Liiku paikkaan kirjoittamalla sen nimi. \n  [enter] = takaisin \n\n  Valitse toiminto: ")
            if choice == "":
                hasMoved = True
                break
            else:
                for i in ownLocation.connections:
                    if choice.lower() == i.name.lower():
                        if i.isLocked:
                            input(f"{split} \n{i.lockedText} ")
                            break
                        print("  Siirrytään...")
                        time.sleep(random.randrange(1, 3))
                        self.location = i
                        hasMoved = True
                        break
                else:
                    input(f"{split} \n  Sijaintia ei löytynyt. ")

    # Nykyisen sijainnin tutkiminen
    def search(self, location):
        input(f"{split} \n{location.searchText} ")
        if self.location.item == []:
            input("\n  Et löytänyt alueelta mitään mukaan otettavaa. ")
        else:
            for i in self.location.item:
                input(f"{i.itemFound} ")
                self.inventory.append(i)
            location.item = []

    # Esineen käyttäminen (choice on pelaajan tekemä valinta)
    def item_use(self, choice):
        for i in self.inventory:
            if choice.lower() == i.name.lower():
                if isinstance(i, Functional):
                    if i in self.location.acceptsItem:
                        if i.usedIn == self.location:
                            input(f"{split} \n  Olet jo käyttänyt esineen tässä paikassa. ")
                            return(False)
                        print("  Käytetään esine...")
                        time.sleep(random.randrange(1, 3))
                        input(f"{split} \n{i.useText} ")
                        i.usedIn.append(self.location)
                        if i.isSingleUse:
                            self.inventory.remove(i)
                        return(True)
                    else:
                        input(f"{split} \n{i.useFail} ")
                        return(False)
                else:
                    print("  Käytetään esine...")
                    time.sleep(random.randrange(1, 3))
                    input(f"{split} \n{i.useText} ")
                    return(True)
        else:
            input(f"{split} \n  Esinettä ei löytynyt inventaariostasi. ")
            return(False)
        
    # Inventaarion tulostus ja esineen valinta
    def inv_show(self):
        itemUsed = False
        while itemUsed == False:
            if self.inventory == []:
                input(f"{split} \n╭───────────────────────────────────────╮ \n│ Inventaariosi on tyhjä.               │ \n│ Täältä näet löytämäsi esineet.        │ \n╰───────────────────────────────────────╯ \n\n  [enter] = takaisin ")
                break
            else:
                print(f"{split} \n╭─────────────────────────────────────────╮ \n│ Inventaariossasi on:                    │")
                for i in self.inventory:
                    print(f"│ » {i.name:<38}│")
                choice = input("╰─────────────────────────────────────────╯ \n\n  Käytä esine kirjoittamalla sen nimi. \n  [enter] = takaisin \n\n  Valitse toiminto: ")
                if choice == "":
                    break
                else:
                    itemUsed = self.item_use(choice)

    # Päävalikko josta pelaaja voi valita eri funktioita
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

# Luodaan esineet (name, itemFound, useText, (useFail, isSingleUse, usedIn = None))
kartta = Item("Kartta", format("Löysit kartan. Tästä voi olla paljon hyötyä."), "» ╭───────────────═══════════════════───────═════╗ \n  │           皿  ⌂ ⌂                        ^   ║ \n  ║    ╭╌╌ [ Keskusta ] ──┬─ [ Koti ]        N   ║ \n  ║    ┆        ║ ⌂⌂      │      ┆              ─╢ \n  │ [ Kuja ]  ⌂ ║         ╰─ [ Metsä ] ╌╌╌╮      │ \n  │    ┆        ║             ♣Ψ │ ♣      ┆      │ \n  ║    ┆    [ Kauppa ]         ♣ │    [ Raunio ] ║ \n  ╠═   ┆                         │ Ψ      ┆      ║ \n  ║    ╰╌ [ ??? ] † †        [ Niitty ] ╌╌╯      ║ \n  ║                †      ▲▲             ~~~     │ \n  ╚═════════─────════════────────────────────────╯ \n\n» Kartta kaikista kaupungin sijainneista. \n  Jotkut sijainnit eivät ole aina saatavilla.")
kärryt = Item
rakennuslupa = Functional("Rakennuslupa", format("Otat mukaan myös rakennusluvan. Voit nyt lähteä seikkailemaan ympäri kaupunkia. Valitse rakennuspaikka käyttämällä tämä esine."), format("Pääset vihdoin aloittamaan rakennusurakkasi. Sinulta puuttuu kuitenkin vielä työkalut sekä materiaalit."), format("Et voi rakentaa tähän. Kaupungista ja niityltä pitäisi löytyä rakennusalueita."), True)
lompakko = Functional
kirjat = Functional("Kirjat", format("Löysit kadun nurkassa olevasta laatikosta muutaman kirjan. Historiaa, pokkareita, kauhua ja muuta jännää."), format("Luet kirjoja. Pettymykseksesi ne ovat kirjoitettu hepreaksi. Suljet kirjat ja päätät tehdä tehdä jotain muuta."), format("Kotona sitten luetaan. Nyt ei ole aikaa sille..."), True)
romu = Functional
työkalut = Functional("Työkalut", format("Ostat työvälineitä sekä lautaa. Nämä saattavat riittää koulun rakentamiseen."), format("Nikkaroit keskustaan yhen talon. Aika siistii!"), format("Et voi rakentaa tähän."), False)

# Luodaan funktionaalisille esineille joukot joihin lisätään sijainnit missä niitä on käytetty
rakennuslupa.usedIn = []
kirjat.usedIn = []
työkalut.usedIn = []
romu.usedIn = []
lompakko.usedIn = []

# Luodaan sijainnit (name, searchText, isLocked, lockedText, item, acceptsItem, connections)
keskusta = Location("Keskusta", format("Kaupunki on täynnä vilinää ja melua. Nauttisit mieluummin ajastasi luonnossa. No... Ei voi mitään."), True, format("Pakkaa tavarasi mukaan ennen keskustaan suuntaamista. Tutki aluetta kunnes inventaariostasi löytyy kartta sekä rakennuslupa."), [kirjat], [rakennuslupa])
koti = Location("Koti", format("Kotisi näyttää ihanan tunnelmalliselta. Tahtoisit mennä takaisin nukkumaan, mutta sinulla riittää vielä tekemistä."), False, format("Et halua palata vielä kotiin, sillä sinulla on vielä asioita hoidettavana."), [kartta, rakennuslupa], [kirjat])
kellari = Location("Kellari", "» Tutkitaan... (Väliaikainen)", True, "  Lukittu... (Väliaikainen)", [], [])
kuja = Location("Kuja", "  Tutkitaan... (Väliaikainen)", True, "  Lukittu... (Väliaikainen)", [], [])
metsä = Location("Metsä", "  Tutkitaan... (Väliaikainen)", True, "  Lukittu... (Väliaikainen)", [], [])
kauppa = Location("Kauppa", format("Kaupan hyllyt ovat täynnä rakennusmateriaaleja ja työkaluja. Juttelet hetken kauppiaan kanssa."), False, format("Et tarvitse kaupasta enää mitään."), [työkalut], [])
raunio = Location("Raunio", "  Tutkitaan... (Väliaikainen)", False, "  Lukittu... (Väliaikainen)", [], [])
varasto = Location("???", "  Tutkitaan... (Väliaikainen)", False, "  Lukittu... (Väliaikainen)", [], [])
niitty = Location("Niitty", "  Tutkitaan... (Väliaikainen)", False, "  Lukittu... (Väliaikainen)", [], [rakennuslupa])

# Lisätään alueiden väliset yhteydet
keskusta.connections = [koti, metsä, kauppa, kuja]
koti.connections = [keskusta, metsä]
kellari.connections = [koti]
kuja.connections = [keskusta, varasto]
metsä.connections = [koti, keskusta, niitty, raunio]
kauppa.connections = [keskusta]
raunio.connections = [metsä, niitty]
varasto.connections = [kuja]
niitty.connections = [metsä, raunio]