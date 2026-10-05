import time
import random
import textwrap
import os
import subprocess

# Tekstin formatointia
splitter = "\n───◇ ◆ ◇─────────────────────────────────────────────────────────────────────\n\n"

def divide(text):
    lines = textwrap.wrap(text, width=64)
    return "» " + "\n  ".join(lines)

def clear_shell():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

# Luokat
class Item:
    def __init__(self, name, itemFound, itemUsed):
        self.name = name # esineen nimi
        self.itemFound = itemFound # tämä tulostuu esineen löytyessä
        self.itemUsed = itemUsed # tämä tulostuu kun esinettä käytetään

class Functional(Item):
    def __init__(self, name, itemFound, itemUsed, itemNotUsed, isSingleUse, usedIn):
        super().__init__(name, itemFound, itemUsed)
        self.itemNotUsed = itemNotUsed # tämä tulostuu kun esinettä ei voi käyttää
        self.isSingleUse = isSingleUse # onko esine kertakäyttöinen
        self.usedIn = usedIn # missä sijainnissa esine on käytetty (joukko)

class Location:
    def __init__(self, name, searchText, isLocked, lockedText, hasItem, acceptsItem, connections = None):
        self.name = name # sijainnin nimi
        self.searchText = searchText # tämä tulostetaan kun sijaintia tutkitaan
        self.isLocked = isLocked # onko pelaajalla pääsyä sijaintiin vai ei
        self.lockedText = lockedText # tämä tulostuu jos koitetaan siirtyä lukittuun sijaintiin
        self.hasItem = hasItem # sijainnista löytyvät esineet (lista)
        self.acceptsItem = acceptsItem # mitä esinettä sijainnissa voi käyttää
        self.connections = connections # joukko paikoista mihin tästä sijainnista pääsee

class User:
    def __init__(self, name, age, location, status, inventory = None,):
        self.name = name # pelaajan asettama nimi
        self.age = age # pelaajan asettama ikä
        self.location = location # nykyinen sijainti
        self.status = status # pelaajan tämänhetkinen tilanne
        self.inventory = inventory # inventaario

    # Pelaajan liikkuminen
    def move(self):
        hasMoved = False
        while hasMoved == False:
            clear_shell()
            print("╭─────────────────────────────────────────────╮ \n│ Voit siirtyä seuraaviin paikkoihin:         │")
            for i in self.location.connections:
                print(f"│ » {i.name:<42}│")
            choice = input("╰─────────────────────────────────────────────╯ \n\n  Liiku paikkaan kirjoittamalla sen nimi. \n  [enter] = takaisin \n\n  Valitse toiminto: ")
            if choice == "":
                hasMoved = True
            else:
                for i in self.location.connections:
                    if choice.lower() == i.name.lower():
                        if i.isLocked:
                            code = input(splitter + divide(i.lockedText))
                            if self.location == kuja and code == "52971" and varasto.isLocked == True:
                                varasto.isLocked = False
                                kuja.searchText = "Kujalla on erittäin ahdasta ja likaista. Onneksi et kärsi ahtaan paikan kammosta."
                                input("\n» Lukko aukeaa.")
                            break
                        print("  Siirrytään...")
                        time.sleep(random.randrange(1, 3))
                        self.location = i
                        hasMoved = True
                        break
                else:
                    input(f"{splitter}  Sijaintia ei löytynyt.")

    # Nykyisen sijainnin tutkiminen
    def search(self):
        input(splitter + divide(self.location.searchText))
        if self.location.hasItem == []:
            input("\n  Et löytänyt alueelta mitään mukaan otettavaa.")
            clear_shell()
        else:
            for i in self.location.hasItem:
                input(f"\n{divide(i.itemFound)}")
                self.inventory.append(i)
            self.location.hasItem = []

    # Esineen käyttäminen
    def item_use(self, choice):
        for i in self.inventory:
            if choice.lower() == i.name.lower():
                if isinstance(i, Functional):
                    if i in self.location.acceptsItem:
                        if self.location in i.usedIn:
                            input(f"{splitter}  Olet jo käyttänyt esineen tässä paikassa.")
                            return(False)
                        print("  Käytetään esine...")
                        time.sleep(random.randrange(1, 3))
                        input(splitter + divide(i.itemUsed))
                        i.usedIn.append(self.location)
                        if i.isSingleUse:
                            self.inventory.remove(i)
                        return(True)
                    else:
                        input(splitter + divide(i.itemNotUsed))
                        return(False)
                else:
                    print("  Käytetään esine...")
                    time.sleep(random.randrange(1, 3))
                    if choice.lower() == "kartta":
                        clear_shell()
                        print(f"\n{kartta.itemUsed}")
                        print(f"{splitter}{divide("Kartta kaikista kaupungin sijainneista. Jotkut sijainnit eivät ole aina saatavilla.")}\n")
                        input(f"» Nykyinen sijaintisi: {self.location.name}")
                        return(False)
                    else:
                        input(splitter + divide(i.itemUsed))
                    return(True)
        else:
            input(f"{splitter}  Esinettä ei löytynyt inventaariostasi.")
            return(False)
        
    # Inventaario ja esineen valinta
    def inv_show(self):
        itemWasUsed = False
        while itemWasUsed == False:
            clear_shell()
            if self.inventory == []:
                input("╭───────────────────────────────────────╮ \n│ Inventaariosi on tyhjä.               │ \n│ Täältä näet löytämäsi esineet.        │ \n╰───────────────────────────────────────╯ \n\n  [enter] = takaisin")
                break
            else:
                print("╭─────────────────────────────────────────╮ \n│ Inventaariossasi on:                    │")
                for i in self.inventory:
                    print(f"│ » {i.name:<38}│")
                choice = input("╰─────────────────────────────────────────╯ \n\n  Käytä esine kirjoittamalla sen nimi. \n  [enter] = takaisin \n\n  Valitse toiminto: ")
                if choice == "":
                    clear_shell()
                    break
                else:
                    itemWasUsed = self.item_use(choice)
                    clear_shell

    # Pelin sisäinen valikko
    def game_menu(self, mission):
        clear_shell()
        print(f"╭─────────────────────────────────────────────────────╮ \n│ [⌂] SIJAINTI: {self.location.name:<38}│ \n│ [≡] TEHTÄVÄ:  {mission:<38}│ \n╰─────────────────────────────────────────────────────╯ \n\n  [1] = Vaihda sijaintia \n  [2] = Tutki aluetta \n  [3] = Avaa inventaario \n  [4] = Sulje peli")
        choice = input("\n  Valitse toiminto: ")
        if choice == "1":
            self.move()
        elif choice == "2":
            print("  Tutkitaan aluetta...")
            time.sleep(random.randrange(1,3))
            self.search()
        elif choice == "3":
            print("  Avataan inventaario...")
            time.sleep(1)
            self.inv_show()
        elif choice == "4":
            clear_shell()
            confirm = input('╭────────────────────────────────────╮ \n│ Suljetaako peli?                   │ \n╰────────────────────────────────────╯ \n\n  Kirjoita "ok" vahvistaaksesi. \n  [enter] = peruuta \n\n  Valitse toiminto: ')
            if confirm.lower() == "ok":
                exit()
        else:
            input(f"{splitter}  Kyseistä toimintoa ei löydy. Valitse toiminto \n  kirjoittamalla sitä vastaava numero.")



# Esineet
kartta = Item(
    name = "Kartta",
    itemFound = "Löysit kartan. Tästä voi olla paljon hyötyä.",
    itemUsed = "  ╭───────────────═══════════════════───────═════╗ \n"
               "  │                                              ║ \n"
               "  │           皿  ⌂ ⌂             ₅        ^     ║ \n"
               "  ║    ╭╌╌ [ Keskusta ] ══╤═ [ Koti ]      N     ║ \n"
               "  ║    ┆      ⁹ ║ ⌂⌂      │      ┆              ─╢ \n"
               "  │ [ Kuja ]  ⌂ ╚═╗       ╰─ [ Metsä ] ╌╌╌╮      │ \n"
               "  │    ┆ ¹        ║          ♣Ψ  │ ⌂      ┆ ₄    │ \n"
               "  ║    ┆      [ Kauppa ]       ♣ │    [ Raunio ] ║ \n"
               "  ╠═   ┆           ²             │ Ψ      ┆      ║ \n"
               "  ║    ╰╌ [ ??? ] † †        [ Pelto ] ╌╌╌╯      ║ \n"
               "  ║                †      ▲▲      ⁷      ~~~     │ \n"
               "  ║                                              │ \n"
               "  ╚═════════─────════════────────────────────────╯ \n"
    )

kärryt = Item(
    name = "Kärryt",
    itemFound = "Löysit kottikärryt. Niillä saat kannettua raskaat tavarat paikasta toiseen.",
    itemUsed = "Näihin kottikärryihin mahtuu yllättävän paljon tavaraa. Nyt saat kuljetettua myös raskaita esineitä."
    )

kirjat = Item(
    name = "Kirjat",
    itemFound = "Tila on täynnä erilaisia oppikirjoja. Mitä koulu olisikaan ilman oppimateriaaleja? Päätät ottaa ison kasan kirjoja mukaan.",
    itemUsed = "Kirjakokoelmastasi löytyy mm. historiaa, matikkaa, äidinkieltä ja luonnontieteitä. Loppupäivästä jos sinulla on aikaa, voit silmäillä kirjat läpi ja päättää haluatko käyttää niitä opetusmateriaaleina."
    )

työkalut = Item(
    name = "Työkalut",
    itemFound = "Löysit sattumalta myös ikivanhan työkalulaatikkosi. Nappaat mukaasi sahan, vasaran, poran, sekä ruuvimeisselin. Nyt on aika palata takaisin kauppaan.",
    itemUsed = "Työkalulaatikossasi on saha, vasara, pora sekä ruuvimeisseli. Tarvitset näitä koulun rakentamiseen."
    )

# Funktionaaliset esineet
rakennuslupa = Functional(
    name = "Rakennuslupa",
    itemFound = "Otat mukaan myös rakennusluvan. Voit nyt lähteä seikkailemaan ympäri kaupunkia. Valitse rakennuspaikka käyttämällä rakennuslupa inventaariostasi.",
    itemUsed = "Pääset vihdoin aloittamaan rakennusurakkasi. Sinulta puuttuu kuitenkin vielä työkalut sekä materiaalit.",
    itemNotUsed = "Et voi rakentaa tähän. Keskustasta ja pellolta pitäisi löytyä rakennusalueita.",
    isSingleUse = True,
    usedIn = []
    )

sorkkarauta = Functional(
    name = "Sorkkarauta",
    itemFound = "Paniikki meinaa iskeä, kunnes havaitset huoneen nurkassa olevan sorkkaraudan. Ehkä saat oven tiirikoitua auki.",
    itemUsed = "Sorkkarauta uppoaa hyvin kujaa peittävien lautojen alle. Saat kangettua naulat irti ja avaat reitin kujalle.",
    itemNotUsed = "Et ole nyt väkivaltaisella tuulella.",
    isSingleUse = False,
    usedIn = []
    )

avain = Functional(
    name = "Avain",
    itemFound = "Ojennat sorkkaraudan lipaston alle ja nykäiset vajan avaimen kätesi ulottuville.",
    itemUsed = "Vajan lukko aukeaa ja näet sisällä kaikenlaista siistiä.",
    itemNotUsed = "Avain ei käy tähän.",
    isSingleUse = True,
    usedIn = []
    )

harava = Functional(
    name = "Harava",
    itemFound = "Vajan seinustalla nojaa myös harava. Toivottavasti se nyt kestää raskaampiakin töitä.",
    itemUsed = "Haravoit pellolta lehtiä, heinää ja muuta roskaa. Jossain kohtaa haravasi kuitenkin hajoaa.",
    itemNotUsed = "Vaikka kuinka tahtoisit pitää kaupunkia siistinä, sinulla ei ole nyt aikaa siihen.",
    isSingleUse = True,
    usedIn = []
    )

rahaa = Functional(
    name = "Rahaa",
    itemFound = "Löysit possupankkisi, jonka tungit aikoinaan täyteen seteleitä. Juuri sopivasti rahaa rakennusmateriaalien ostamiseen.",
    itemUsed = "Et ole säästänyt turhaan kaikkien näiden vuosien ajan. Kaikki rahasi kuluu rakennusmateriaaleihin ja nyt toivot ettei lisäkustannuksia tule enempää.",
    itemNotUsed = "Sinulla ei ole mitään ostettavaa.",
    isSingleUse = True,
    usedIn = []
    )

materiaalit = Functional(
    name = "Materiaalit",
    itemFound = "Hankit myös kasan lautaa, ruuveja, nauloja, peltiä ja kaikkea muuta tarvittavaa.",
    itemUsed = "Nyt kun vihdoin löysit kaiken tarvitsemasi, sait rakennettua pienen koulun. Budjettisi ei ollut kovin suuri, joten tiloja on rajallisesti. Voit nyt halutessasi palata kotiin nukkumaan tai jatkaa tutkimista. Koulu avataan vasta huomenna.",
    itemNotUsed = "Et voi rakentaa mitään juuri nyt. Varmista, että sinulla on työkalusi mukana ja että olet työmaalla.",
    isSingleUse = True,
    usedIn = []
    )

romua = Functional(
    name = "Romua",
    itemFound = "Löysit ison kasan romua, jota voit käyttää rakennusmateriaalina. Näillä saat laajennettua koulun tiloja huomattavasti.",
    itemUsed = "Laajensit koulua rakentamalla uusia luokkahuoneita sekä varastotilan.",
    itemNotUsed = "Et voi rakentaa mitään juuri nyt. Varmista, että sinulla on työkalusi mukana ja että olet työmaalla.",
    isSingleUse = True,
    usedIn = []
    )

yöpuku = Functional(
    name = "Yöpuku",
    itemFound = "Nappaat kaapistasi sinisen yöpukusi. Näytät ihan Herra Hakkaraiselta se päällä. Et halua kuitenkaan mennä vielä nukkumaan likaiset vaatteet ylläsi.",
    itemUsed = "Ai että. Pitkästä aikaa pääsee taas nukkumaan.",
    itemNotUsed = "Älä nyt hyvä ihminen rupea täällä vaihtamaan vaatteita!!",
    isSingleUse = False,
    usedIn = []
    )

allItemNames = ["Kartta", "Kärryt", "Kirjat", "Työkalut", "Rakennuslupa", "Sorkkarauta", "Avain", "Harava", "Rahaa", "Materiaalit", "Romua", "Yöpuku"]


# Sijainnit
keskusta = Location(
    name = "Keskusta",
    searchText = "Kaupunki on täynnä vilinää ja melua. Nauttisit mieluummin ajastasi luonnossa.",
    isLocked = True,
    lockedText = "Pakkaa tavarasi mukaan ennen keskustaan suuntaamista. Tutki aluetta kunnes inventaariostasi löytyy sekä kartta että rakennuslupa.",
    hasItem = [],
    acceptsItem = [rakennuslupa, sorkkarauta]
    )

koti = Location(
    name = "Koti",
    searchText = "Kotisi näyttää ihanan tunnelmalliselta. Tahtoisit mennä takaisin nukkumaan, mutta sinulla riittää vielä tekemistä.",
    isLocked = False,
    lockedText = "Rahoja etsiessä työnsit vahingossa kellarin oven kiinni ja lukitsit sen. Olet jumissa...",
    hasItem = [kartta, rakennuslupa],
    acceptsItem = [kirjat]
)

kellari = Location(
    name = "Kellari",
    searchText = "Ikivanha hämärä kellarisi haisee tunkkaiselta. Toivottavasti ei ole mitään homeongelmia tai muuten voi tulla kalliiksi.",
    isLocked = False,
    lockedText = "Huhhuh. Tonne ei kannata enää mennä.",
    hasItem = [],
    acceptsItem = []
)

kuja = Location(
    name = "Kuja",
    searchText = 'Kujalla on erittäin ahdasta ja likaista. Kujan toisessa päässä on ovi, jossa on numerolukko. Oven vieressä on pieni lappu, jossa lukee "Koti, Kauppa, Keskusta, Pelto, Kuja".',
    isLocked = True,
    lockedText = "Kujalle vievä portti on muurattu kiinni laudoilla. Koitat repiä niitä irti mutta naulat ovat liian lujasti kiinni.",
    hasItem = [],
    acceptsItem = []
)

metsä = Location(
    name = "Metsä",
    searchText = "Tunnet raikkaan ilman keuhkoissasi ja nenääsi tunkeutuu ihana luonnon tuoksu. Ehkä joku päivä voisit tulla tänne telttaretkelle.",
    isLocked = True,
    lockedText = "Pakkaa tavarasi mukaan ennen metsään suuntaamista. Tutki aluetta kunnes inventaariostasi löytyy sekä kartta että rakennuslupa.",
    hasItem = [],
    acceptsItem = [avain]
)

kauppa = Location(
    name = "Kauppa",
    searchText = "Kaupan hyllyt ovat täynnä rakennusmateriaaleja.",
    isLocked = False,
    lockedText = "Sinun kannattaa hakea kotoa rahaa ennen kauppaan palaamista.",
    hasItem = [],
    acceptsItem = []
)

raunio = Location(
    name = "Raunio",
    searchText = "Löydät metsän laidalta raunion. Mahtaa olla jokin hylätty tehdas. Alueelta löytyy erilaisia materiaaleja joista voisi olla hyötyä koulun rakentamisessa. Et jaksa kuitenkaan kantaa niitä.",
    isLocked = False,
    lockedText = "Ei ole lukittu",
    hasItem = [],
    acceptsItem = []
)

varasto = Location(
    name = "Varasto",
    searchText = "Laitat varaston valot päälle. Tomua kaikkialla. Et välttämättä halua lorvailla täällä turhan kauaa ellet halua tuberkuloosia.",
    isLocked = True,
    lockedText = "Rakennuksen ovi on lukossa. Anna 5-numeroinen koodi päästäksesi sisään: ",
    hasItem = [kirjat],
    acceptsItem = []
)

pelto = Location(
    name = "Pelto",
    searchText = "Tämä pelto ei ole mikään kaunein nähtävyys. Enemmän sitä voisi kutsua ryteiköksi tai vaikka taistelukentäksi.",
    isLocked = False,
    lockedText = "Ei ole lukittu",
    hasItem = [],
    acceptsItem = [rakennuslupa, harava]
)

vaja = Location(
    name = "Vaja",
    searchText = "Haistat jotain mätääntynyttä. Et muista milloin viimeksi olisit käynyt täällä.",
    isLocked = True,
    lockedText = "Tirkistelet lautojen välistä vajan sisään. Näet kottikärryt sekä haravan. Ovi on lukittu, mutta avaimen pitäisi löytyä kotoasi.",
    hasItem = [kärryt, harava],
    acceptsItem = []
)

allLocationNames = ["Keskusta", "Koti", "Kellari", "Kuja", "Metsä", "Kauppa", "Raunio", "Varasto", "Pelto", "Vaja"]

# Sijaintien väliset yhteydet
keskusta.connections = [koti, metsä, kauppa, kuja]
koti.connections = [keskusta, metsä]
kellari.connections = [koti]
kuja.connections = [keskusta, varasto]
metsä.connections = [koti, keskusta, pelto, raunio]
kauppa.connections = [keskusta]
raunio.connections = [metsä, pelto]
varasto.connections = [kuja]
pelto.connections = [metsä, raunio]
vaja.connections = [metsä]