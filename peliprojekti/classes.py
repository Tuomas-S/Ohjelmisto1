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
    def __init__(self, name, itemFound, useText, useFail, isSingleUse, usedIn):
        super().__init__(name, itemFound, useText)
        self.useFail = useFail # tämä tulostuu kun esinettä ei voi käyttää
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
                            code = input(f"{split} \n{i.lockedText} ")
                            if self.location == kuja and code == "52971" and varasto.isLocked == True:
                                varasto.isLocked = False
                                kuja.searchText = format("Kujalla on erittäin ahdasta ja likaista. Onneksi et kärsi ahtaan paikan kammosta.")
                                input(format("Varaston ovi aukeaa. Juuri ennen kuin astut varaston ovesta sisään, joku varastaa sinun työkalusi ja juoksee karkuun. Löydä varas saadaksesi työkalut takaisin."))
                                self.inventory.remove(työkalut)
                                allLocations[random.randint(2, 7)].hasItem.append(työkalut)
                                työkalut.itemFound = format("Löydät työkaluvarkaan piileksimästä ja otat työkalusi takaisin. Varas juoksee itkien karkuun ja katoaa taivaan tuuliin.")
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
        if self.location.hasItem == []:
            input("\n  Et löytänyt alueelta mitään mukaan otettavaa. ")
        else:
            for i in self.location.hasItem:
                input(f"{i.itemFound} ")
                self.inventory.append(i)
            location.hasItem = []

    # Esineen käyttäminen (choice on pelaajan tekemä valinta)
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
                        input(f"{split} \n{i.useText} ")
                        i.usedIn.add(self.location)
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

    def main_menu(self):
        return

    # Pelin sisäinen valikko josta pelaaja voi valita eri funktioita
    def game_menu(self, mission):
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

# Luodaan esineet ja lista kaikista esineistä pelin tallennusta varten (name, itemFound, useText, (useFail, isSingleUse, usedIn))
kartta = Item("Kartta", format("Löysit kartan. Tästä voi olla paljon hyötyä."), "  ╭───────────────═══════════════════───────═════╗ \n  │           皿  ⌂ ⌂              5         ^   ║ \n  ║    ╭╌╌ [ Keskusta ] ══╤═ [ Koti ]        N   ║ \n  ║    ┆      9 ║ ⌂⌂      │      ┆              ─╢ \n  │ [ Kuja ]  ⌂ ╚═╗       ╰─ [ Metsä ] ╌╌╌╮      │ \n  │    ┆ 1        ║          ♣Ψ  │ ♣      ┆ 4    │ \n  ║    ┆      [ Kauppa ]       ♣ │    [ Raunio ] ║ \n  ╠═   ┆           2             │ Ψ      ┆      ║ \n  ║    ╰╌ [ ??? ] † †        [ Pelto ] ╌╌╌╯      ║ \n  ║                †      ▲▲      7      ~~~     │ \n  ╚═════════─────════════────────────────────────╯ \n\n» Kartta kaikista kaupungin sijainneista. \n  Jotkut sijainnit eivät ole aina saatavilla.")
kärryt = Item("Kärryt", format("Löysit kottikärryt. Niillä saat kannettua raskaat rakennusmateriaalit paikasta toiseen."), format("Näihin kottikärryihin mahtuu yllättävän paljon tavaraa. Nyt saat kuljetettua myös raskaita esineitä."))
kirjat = Item("Kirjat", format(""), format(""))
työkalut = Item("Työkalut", format("Löysit sattumalta myös ikivanhan työkalulaatikkosi. Nappaat mukaasi sahan, vasaran, poran, sekä ruuvimeisselin. Nyt on aika palata takaisin kauppaan."), format("Työkalulaatikossasi on saha, vasara, pora sekä ruuvimeisseli. Tarvitset näitä koulun rakentamiseen."))
rakennuslupa = Functional("Rakennuslupa", format("Otat mukaan myös rakennusluvan. Voit nyt lähteä seikkailemaan ympäri kaupunkia. Valitse rakennuspaikka käyttämällä rakennuslupa inventaariostasi."), format("Pääset vihdoin aloittamaan rakennusurakkasi. Sinulta puuttuu kuitenkin vielä työkalut sekä materiaalit."), format("Et voi rakentaa tähän. Keskustasta ja pellolta pitäisi löytyä rakennusalueita."), True, set())
sorkkarauta = Functional("Sorkkarauta", format("Paniikki meinaa iskeä, kunnes havaitset huoneen nurkassa olevan sorkkaraudan. Ehkä saat oven tiirikoitua auki."), format("Revit oven hajalle sorkkaraudalla ja näet taas päivänvaloa. Melkein kävi huonosti."), format("Et ole nyt väkivaltaisella tuulella."), False, set())
rahaa = Functional("Rahaa", format("Löysit possupankkisi, jonka tungit aikoinaan täyteen seteleitä. Juuri sopivasti rahaa rakennusmateriaalien ostamiseen."), format("Et ole säästänyt turhaan nämä kaikki vuodet. Kaikki rahasi kuluu rakennusmateriaaleihin ja nyt toivot ettei lisäkustannuksia tule enempää."), format("Sinulla ei ole mitään ostettavaa."), True, set())
materiaalit = Functional("Materiaalit", format("Hankit myös kasan lautaa, ruuveja, nauloja, peltiä ja kaikkea muuta tarvittavaa."), format("Nyt kun vihdoin löysit kaiken tarvitsemasi, sait rakennettua pienen koulun. Budjettisi ei ole kovin suuri, joten tiloja on rajallisesti. Voit nyt palata kotiin nukkumaan, sillä koulu avataan vasta huomenna."), format("Et voi rakentaa mitään juuri nyt. Varmista, että sinulla on työkalusi mukana ja että olet työmaalla."), True, set())
romua = Functional("Romua", format("Löysit ison kasan romua, jota voit käyttää rakennusmateriaalina. Materiaalit riittävät nyt myös ruokalan rakentamiseen."), format("Rakensit pienen ruokalan ylimääräiselle alueelle. Toivottavasti ruoka maistuu, kun koulu avataan."), format("Et voi rakentaa mitään juuri nyt. Varmista, että sinulla on työkalusi mukana ja että olet työmaalla."), True, set())
allItems = [kartta, kärryt, rakennuslupa, kirjat, työkalut, sorkkarauta, rahaa, materiaalit, romua]

# Luodaan sijainnit ja lista kaikista sijainneista pelin tallennusta varten (name, searchText, isLocked, lockedText, hasItem, acceptsItem, connections)
keskusta = Location("Keskusta", format("Kaupunki on täynnä vilinää ja melua. Nauttisit mieluummin ajastasi luonnossa."), True, format("Pakkaa tavarasi mukaan ennen keskustaan suuntaamista. Tutki aluetta kunnes inventaariostasi löytyy kartta sekä rakennuslupa."), [], {rakennuslupa, sorkkarauta})
koti = Location("Koti", format("Kotisi näyttää ihanan tunnelmalliselta. Tahtoisit mennä takaisin nukkumaan, mutta sinulla riittää vielä tekemistä."), False, format("Rahoja etsiessä työnsit vahingossa kellarin oven kiinni ja lukitsit sen. Olet jumissa..."), [kartta, rakennuslupa], {kirjat})
kellari = Location("Kellari", format("Kellarisi haisee tunkkaiselta."), False, "  Lukittu... (Väliaikainen)", [rahaa, työkalut], {sorkkarauta})
kuja = Location("Kuja", format('Kujalla on erittäin ahdasta ja likaista. Kujan toisessa päässä on ovi, jossa on numerolukko. Oven vieressä on pieni lappu, jossa lukee "Koti, Kauppa, Keskusta, Pelto, Kuja".'), True, format("Kujalle vievä portti on muurattu kiinni laudoilla. Koitat repiä niitä irti mutta naulat ovat liian lujasti kiinni."), [], set())
metsä = Location("Metsä", "  Tutkitaan... (Väliaikainen)", True, "  Lukittu... (Väliaikainen)", [], set())
kauppa = Location("Kauppa", format("Kaupan hyllyt ovat täynnä rakennusmateriaaleja."), False, format("Sinun kannattaa hakea kotoa rahaa ennen kauppaan palaamista."), [], set())
raunio = Location("Raunio", format("Löydät metsän laidalta raunion. Mahtaa olla jokin hylätty tehdas. Alueelta löytyy erilaisia materiaaleja joista voisi olla hyötyä koulun rakentamisessa. Et jaksa kuitenkaan kantaa niitä ja suurin osa materiaalista on jokatapauksessa käyttökelvotonta."), False, "", [], set())
varasto = Location("Varasto", "  Tutkitaan... (Väliaikainen)", True, format("Rakennuksen ovi on lukossa. Anna 5-numeroinen koodi päästäksesi sisään:"), [kirjat], set())
pelto = Location("Pelto", "  Tutkitaan... (Väliaikainen)", False, "  Lukittu... (Väliaikainen)", [], {rakennuslupa})
allLocations = [koti, kellari, keskusta, kuja, metsä, kauppa, raunio, varasto, pelto]

# Lisätään alueiden väliset yhteydet
keskusta.connections = [koti, metsä, kauppa, kuja]
koti.connections = [keskusta, metsä]
kellari.connections = [koti]
kuja.connections = [keskusta, varasto]
metsä.connections = [koti, keskusta, pelto, raunio]
kauppa.connections = [keskusta]
raunio.connections = [metsä, pelto]
varasto.connections = [kuja]
pelto.connections = [metsä, raunio]