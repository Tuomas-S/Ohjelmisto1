import time
import random
import textwrap

# Tekstin formatointia
split = "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━▶\n"
def format(text):
    lines = textwrap.wrap(text, width=64)
    return "» " + "\n  ".join(lines)

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
    def __init__(self, name, searchText, isLocked, cantEnter, hasItem, acceptsItem, connections = None):
        self.name = name # sijainnin nimi
        self.searchText = searchText # tämä tulostetaan kun sijaintia tutkitaan
        self.isLocked = isLocked # onko pelaajalla pääsyä sijaintiin vai ei
        self.cantEnter = cantEnter # tämä tulostuu jos koitetaan siirtyä lukittuun sijaintiin
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
            print(f"{split} \n╭─────────────────────────────────────────────╮ \n│ Voit siirtyä seuraaviin paikkoihin:         │")
            for i in self.location.connections:
                print(f"│ » {i.name:<42}│")
            choice = input("╰─────────────────────────────────────────────╯ \n\n  Liiku paikkaan kirjoittamalla sen nimi. \n  [enter] = takaisin \n\n  Valitse toiminto: ")
            if choice == "":
                hasMoved = True
                break
            else:
                for i in self.location.connections:
                    if choice.lower() == i.name.lower():
                        if i.isLocked:
                            code = input(f"{split} \n{format(i.cantEnter)} ")
                            if self.location == kuja and code == "52971" and varasto.isLocked == True:
                                varasto.isLocked = False
                                kuja.searchText = "Kujalla on erittäin ahdasta ja likaista. Onneksi et kärsi ahtaan paikan kammosta."
                                input(f"{format("Lukko aukeaa.")} ")
                            break
                        print("  Siirrytään...")
                        time.sleep(random.randrange(1, 3))
                        self.location = i
                        hasMoved = True
                        break
                else:
                    input(f"{split} \n  Sijaintia ei löytynyt. ")

    # Nykyisen sijainnin tutkiminen
    def search(self):
        input(f"{split} \n{format(self.location.searchText)} ")
        if self.location.hasItem == []:
            input("\n  Et löytänyt alueelta mitään mukaan otettavaa. ")
        else:
            for i in self.location.hasItem:
                input(f"{format(i.itemFound)} ")
                self.inventory.append(i)
            self.location.hasItem = []

    # Esineen käyttäminen
    def item_use(self, choice):
        for i in self.inventory:
            if choice.lower() == i.name.lower():
                if isinstance(i, Functional):
                    if i in self.location.acceptsItem:
                        if self.location in i.usedIn:
                            input(f"{split} \n  Olet jo käyttänyt esineen tässä paikassa. ")
                            return(False)
                        print("  Käytetään esine...")
                        time.sleep(random.randrange(1, 3))
                        input(f"{split} \n{format(i.itemUsed)} ")
                        i.usedIn.append(self.location)
                        if i.isSingleUse:
                            self.inventory.remove(i)
                        return(True)
                    else:
                        input(f"{split} \n{format(i.itemNotUsed)} ")
                        return(False)
                else:
                    print("  Käytetään esine...")
                    time.sleep(random.randrange(1, 3))
                    if choice.lower() == "kartta":
                        input(f"{split} \n{kartta.itemUsed} ")
                    else:
                        input(f"{split} \n{format(i.itemUsed)} ")
                    return(True)
        else:
            input(f"{split} \n  Esinettä ei löytynyt inventaariostasi. ")
            return(False)
        
    # Inventaario ja esineen valinta
    def inv_show(self):
        itemWasUsed = False
        while itemWasUsed == False:
            if self.inventory == []:
                input(f"{split}"
                      "\n╭───────────────────────────────────────╮ \n│ Inventaariosi on tyhjä.               │ \n│ Täältä näet löytämäsi esineet.        │ \n╰───────────────────────────────────────╯ \n\n  [enter] = takaisin ")
                break
            else:
                print(f"{split} \n╭─────────────────────────────────────────╮ \n│ Inventaariossasi on:                    │")
                for i in self.inventory:
                    print(f"│ » {i.name:<38}│")
                choice = input("╰─────────────────────────────────────────╯ \n\n  Käytä esine kirjoittamalla sen nimi. \n  [enter] = takaisin \n\n  Valitse toiminto: ")
                if choice == "":
                    break
                else:
                    itemWasUsed = self.item_use(choice)

    # Pelin sisäinen valikko
    def game_menu(self, mission):
        print(f"{split} \n╭─────────────────────────────────────────────────────╮ \n│ [⌂] SIJAINTI: {self.location.name:<38}│ \n│ [≡] TEHTÄVÄ:  {mission:<38}│ \n╰─────────────────────────────────────────────────────╯ \n\n  [1] = Vaihda sijaintia \n  [2] = Tutki aluetta \n  [3] = Avaa inventaario \n  [4] = Sulje peli")
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
            confirm = input(f'{split} \n╭────────────────────────────────────╮ \n│ Suljetaako peli?                   │ \n╰────────────────────────────────────╯ \n\n  Kirjoita "ok" vahvistaaksesi. \n  [enter] = peruuta \n\n  Valitse toiminto: ')
            if confirm.lower() == "ok":
                exit()
        else:
            input(f"{split} \n  Kyseistä toimintoa ei löydy. Valitse toiminto \n  kirjoittamalla sitä vastaava numero. ")



# Esineet
kartta = Item(
    name = "Kartta",
    itemFound = "Löysit kartan. Tästä voi olla paljon hyötyä.",
    itemUsed = "  ╭───────────────═══════════════════───────═════╗ \n"
               "  │           皿  ⌂ ⌂              5         ^   ║ \n"
               "  ║    ╭╌╌ [ Keskusta ] ══╤═ [ Koti ]        N   ║ \n"
               "  ║    ┆      9 ║ ⌂⌂      │      ┆              ─╢ \n"
               "  │ [ Kuja ]  ⌂ ╚═╗       ╰─ [ Metsä ] ╌╌╌╮      │ \n"
               "  │    ┆ 1        ║          ♣Ψ  │ ♣      ┆ 4    │ \n"
               "  ║    ┆      [ Kauppa ]       ♣ │    [ Raunio ] ║ \n"
               "  ╠═   ┆           2             │ Ψ      ┆      ║ \n"
               "  ║    ╰╌ [ ??? ] † †        [ Pelto ] ╌╌╌╯      ║ \n"
               "  ║                †      ▲▲      7      ~~~     │ \n"
               "  ╚═════════─────════════────────────────────────╯ \n\n"
               "» Kartta kaikista kaupungin sijainneista.\n"
               "  Jotkut sijainnit eivät ole aina saatavilla."
    )

kärryt = Item(
    name = "Kärryt",
    itemFound = "Löysit kottikärryt. Niillä saat kannettua raskaat rakennusmateriaalit paikasta toiseen.",
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
    UsedIn = []
    )

sorkkarauta = Functional(
    name = "Sorkkarauta",
    itemFound = "Paniikki meinaa iskeä, kunnes havaitset huoneen nurkassa olevan sorkkaraudan. Ehkä saat oven tiirikoitua auki.",
    itemUsed = "Revit oven hajalle sorkkaraudalla ja näet taas päivänvaloa. Melkein kävi huonosti.",
    itemNotUsed = "Et ole nyt väkivaltaisella tuulella.",
    isSingleUse = False,
    UsedIn = []
    )

avain = Functional(
    name = "Avain",
    itemFound = "Kurotat sorkkaraudalla lipaston alle ja nappaat vajan avaimen mukaan.",
    itemUsed = "Avaat vajan lukon.",
    itemNotUsed = "Avain ei käy tähän.",
    isSingleUse = True,
    UsedIn = []
    )

harava = Functional(
    name = "Harava",
    itemFound = "",
    itemUsed = "",
    itemNotUsed = "",
    isSingleUse = True,
    UsedIn = []
    )

rahaa = Functional(
    name = "Rahaa",
    itemFound = "Löysit possupankkisi, jonka tungit aikoinaan täyteen seteleitä. Juuri sopivasti rahaa rakennusmateriaalien ostamiseen.",
    itemUsed = "Et ole säästänyt turhaan kaikkien näiden vuosien ajan. Kaikki rahasi kuluu rakennusmateriaaleihin ja nyt toivot ettei lisäkustannuksia tule enempää.",
    itemNotUsed = "Sinulla ei ole mitään ostettavaa.",
    isSingleUse = True,
    UsedIn = []
    )

materiaalit = Functional(
    name = "Materiaalit",
    itemFound = "Hankit myös kasan lautaa, ruuveja, nauloja, peltiä ja kaikkea muuta tarvittavaa.",
    itemUsed = "Nyt kun vihdoin löysit kaiken tarvitsemasi, sait rakennettua pienen koulun. Budjettisi ei ollut kovin suuri, joten tiloja on rajallisesti. Voit nyt halutessasi palata kotiin nukkumaan tai jatkaa tutkimista. Koulu avataan vasta huomenna.",
    itemNotUsed = "Et voi rakentaa mitään juuri nyt. Varmista, että sinulla on työkalusi mukana ja että olet työmaalla.",
    isSingleUse = True,
    UsedIn = []
    )

romua = Functional(
    name = "Romua",
    itemFound = "Löysit ison kasan romua, jota voit käyttää rakennusmateriaalina. Näillä saat laajennettua koulun tiloja huomattavasti.",
    itemUsed = "Laajensit koulua rakentamalla uusia luokkahuoneita sekä varastotilan.",
    itemNotUsed = "Et voi rakentaa mitään juuri nyt. Varmista, että sinulla on työkalusi mukana ja että olet työmaalla.",
    isSingleUse = True,
    UsedIn = []
    )

yöpuku = Functional(
    name = "Yöpuku",
    itemFound = "Nappaat kaapistasi sinisen yöpukusi. Näytät ihan Herra Hakkaraiselta se päällä. Et halua kuitenkaan mennä vielä nukkumaan likaiset vaatteet ylläsi.",
    itemUsed = "Ai että. Pitkästä aikaa pääsee taas nukkumaan.",
    itemNotUsed = "Älä nyt hyvä ihminen rupea täällä vaihtamaan vaatteita!!",
    isSingleUse = False,
    UsedIn = []
    )

allItemNames = ["Kartta", "Kärryt", "Kirjat", "Työkalut", "Rakennuslupa", "Sorkkarauta", "Avain", "Harava", "Rahaa", "Materiaalit", "Romua", "Yöpuku"]


# Sijainnit
keskusta = Location(
    name = "Keskusta",
    search = "Kaupunki on täynnä vilinää ja melua. Nauttisit mieluummin ajastasi luonnossa.",
    isLocked = True,
    cantEnter = "Pakkaa tavarasi mukaan ennen keskustaan suuntaamista. Tutki aluetta kunnes inventaariostasi löytyy kartta sekä rakennuslupa.",
    hasItem = [],
    acceptsItem = [rakennuslupa, sorkkarauta]
    )

koti = Location(
    name = "Koti",
    search = "Kotisi näyttää ihanan tunnelmalliselta. Tahtoisit mennä takaisin nukkumaan, mutta sinulla riittää vielä tekemistä.",
    isLocked = False,
    cantEnter = "Rahoja etsiessä työnsit vahingossa kellarin oven kiinni ja lukitsit sen. Olet jumissa...",
    hasItem = [kartta, rakennuslupa],
    acceptsItem = [kirjat]
)

kellari = Location(
    name = "Kellari",
    search = "Kellarisi haisee tunkkaiselta.",
    isLocked = False,
    cantEnter = "Ei lukittu",
    hasItem = [],
    acceptsItem = []
)

kuja = Location(
    name = "Kuja",
    search = 'Kujalla on erittäin ahdasta ja likaista. Kujan toisessa päässä on ovi, jossa on numerolukko. Oven vieressä on pieni lappu, jossa lukee "Koti, Kauppa, Keskusta, Pelto, Kuja".',
    isLocked = True,
    cantEnter = "Kujalle vievä portti on muurattu kiinni laudoilla. Koitat repiä niitä irti mutta naulat ovat liian lujasti kiinni.",
    hasItem = [],
    acceptsItem = []
)

metsä = Location(
    name = "Metsä",
    search = "Tunnet raikkaan ilman keuhkoissasi ja nenääsi tunkeutuu ihana luonnon tuoksu. Ehkä joku päivä voisit tulla tänne telttaretkelle.",
    isLocked = True,
    cantEnter = "",
    hasItem = [],
    acceptsItem = []
)

kauppa = Location(
    name = "Kauppa",
    search = "Kaupan hyllyt ovat täynnä rakennusmateriaaleja.",
    isLocked = False,
    cantEnter = "Sinun kannattaa hakea kotoa rahaa ennen kauppaan palaamista.",
    hasItem = [],
    acceptsItem = []
)

raunio = Location(
    name = "Raunio",
    search = "Löydät metsän laidalta raunion. Mahtaa olla jokin hylätty tehdas. Alueelta löytyy erilaisia materiaaleja joista voisi olla hyötyä koulun rakentamisessa. Et jaksa kuitenkaan kantaa niitä ja suurin osa materiaalista on jokatapauksessa käyttökelvotonta.",
    isLocked = False,
    cantEnter = "",
    hasItem = [],
    acceptsItem = []
)

varasto = Location(
    name = "Varasto",
    search = "Laitat varaston valot päälle. Tomua kaikkialla. Et välttämättä halua lorvailla täällä turhan kauaa ellet halua tuberkuloosia.",
    isLocked = True,
    cantEnter = "Rakennuksen ovi on lukossa. Anna 5-numeroinen koodi päästäksesi sisään:",
    hasItem = [kirjat],
    acceptsItem = []
)

pelto = Location(
    name = "Pelto",
    search = "",
    isLocked = False,
    cantEnter = "",
    hasItem = [],
    acceptsItem = [rakennuslupa]
)

vaja = Location(
    name = "Vaja",
    search = "Tutkitaan !!!!!!!!!!!!!!!!!!!!!!!!!! Väliaikainen",
    isLocked = True,
    cantEnter = "Vajan ovi on lukittu. Yleisavain löytyy kotoasi.",
    hasItem = [],
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