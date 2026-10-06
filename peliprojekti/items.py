# Kerättävät esineet
class Item:
    def __init__(self, name, foundText, usedText):
        self.name = name # esineen nimi
        self.foundText = foundText # tämä tulostuu esineen löytyessä
        self.usedText = usedText # tämä tulostuu kun esinettä käytetään

    # Muokkaa esineen sanakirjamuotoon
    def to_dictionary(self):
        return {
            "type": "Item",
            "name": self.name,
            "foundText": self.foundText,
            "usedText": self.usedText
        }
    
# Käytettävät esineet
class Functional(Item):
    def __init__(self, name, foundText, usedText, itemNotUsed, isSingleUse, usedIn):
        super().__init__(name, foundText, usedText)
        self.itemNotUsed = itemNotUsed # tämä tulostuu kun esinettä ei voi käyttää
        self.isSingleUse = isSingleUse # onko esine kertakäyttöinen
        self.usedIn = usedIn # missä sijainnissa esine on käytetty (joukko)

    # Muokkaa esineen sanakirjamuotoon
    def to_dictionary(self):
        return {
            "type": "Functional",
            "name": self.name,
            "foundText": self.foundText,
            "usedText": self.usedText,
            "itemNotUsed": self.itemNotUsed,
            "isSingleUse": self.isSingleUse,
            "usedIn": [location.name for location in self.usedIn] if self.usedIn else []
        }


kartta = Item(
    name = "Kartta",
    foundText = "Löysit kartan. Tästä voi olla paljon hyötyä.",
    usedText = "  ╭───────────────═══════════════════───────═════╗\n"
               "  │                                              ║\n"
               "  │           皿  ⌂ ⌂             ₅        ^     ║\n"
               "  ║    ╭╌╌ [ Keskusta ] ══╤═ [ Koti ]      N     ║\n"
               "  ║    ┆      ⁹ ║ ⌂⌂      │      ┆              ─╢\n"
               "  │ [ Kuja ]  ⌂ ╚═╗       ╰─ [ Metsä ] ╌╌╌╮      │\n"
               "  │    ┆ ¹        ║          ♣Ψ  │ ⌂      ┆ ₄    │\n"
               "  ║    ┆      [ Kauppa ]       ♣ │    [ Raunio ] ║\n"
               "  ╠═   ┆           ²             │ Ψ      ┆      ║\n"
               "  ║    ╰╌ [ ??? ] † †        [ Pelto ] ╌╌╌╯      ║\n"
               "  ║                †      ▲▲      ⁷      ~~~     │\n"
               "  ║                                              │\n"
               "  ╚═════════─────════════────────────────────────╯\n"
    )

kärryt = Item(
    name = "Kärryt",
    foundText = "Löysit kottikärryt. Niillä saat kannettua raskaat tavarat paikasta toiseen.",
    usedText = "Näihin kottikärryihin mahtuu yllättävän paljon tavaraa. Nyt saat kuljetettua myös raskaita esineitä."
    )

kirjat = Item(
    name = "Kirjat",
    foundText = "Tila on täynnä erilaisia oppikirjoja. Mitä koulu olisikaan ilman oppimateriaaleja? Päätät ottaa ison kasan kirjoja mukaan.",
    usedText = "Kirjakokoelmastasi löytyy mm. historiaa, matikkaa, äidinkieltä ja luonnontieteitä. Loppupäivästä jos sinulla on aikaa, voit silmäillä kirjat läpi ja päättää haluatko käyttää niitä opetusmateriaaleina."
    )

työkalut = Item(
    name = "Työkalut",
    foundText = "Löysit sattumalta myös ikivanhan työkalulaatikkosi. Nappaat mukaasi sahan, vasaran, poran, sekä ruuvimeisselin. Nyt on aika palata takaisin kauppaan.",
    usedText = "Työkalulaatikossasi on saha, vasara, pora sekä ruuvimeisseli. Tarvitset näitä koulun rakentamiseen."
    )

# Funktionaaliset esineet
rakennuslupa = Functional(
    name = "Rakennuslupa",
    foundText = "Otat mukaan myös rakennusluvan. Voit nyt lähteä seikkailemaan ympäri kaupunkia. Valitse rakennuspaikka käyttämällä rakennuslupa inventaariostasi.",
    usedText = "Pääset vihdoin aloittamaan rakennusurakkasi. Sinulta puuttuu kuitenkin vielä työkalut sekä materiaalit.",
    itemNotUsed = "Et voi rakentaa tähän. Keskustasta ja pellolta pitäisi löytyä rakennusalueita.",
    isSingleUse = True,
    usedIn = []
    )

sorkkarauta = Functional(
    name = "Sorkkarauta",
    foundText = "Paniikki meinaa iskeä, kunnes havaitset huoneen nurkassa olevan sorkkaraudan. Ehkä saat oven tiirikoitua auki.",
    usedText = "Sorkkarauta uppoaa hyvin kujaa peittävien lautojen alle. Saat kangettua naulat irti ja avaat reitin kujalle.",
    itemNotUsed = "Et ole nyt väkivaltaisella tuulella.",
    isSingleUse = False,
    usedIn = []
    )

avain = Functional(
    name = "Avain",
    foundText = "Ojennat sorkkaraudan lipaston alle ja nykäiset vajan avaimen kätesi ulottuville.",
    usedText = "Vajan lukko aukeaa ja näet sisällä kaikenlaista siistiä.",
    itemNotUsed = "Avain ei käy tähän.",
    isSingleUse = True,
    usedIn = []
    )

harava = Functional(
    name = "Harava",
    foundText = "Vajan seinustalla nojaa myös harava. Toivottavasti se nyt kestää raskaampiakin töitä.",
    usedText = "Haravoit pellolta lehtiä, heinää ja muuta roskaa. Jossain kohtaa haravasi kuitenkin hajoaa.",
    itemNotUsed = "Vaikka kuinka tahtoisit pitää kaupunkia siistinä, sinulla ei ole nyt aikaa siihen.",
    isSingleUse = True,
    usedIn = []
    )

rahaa = Functional(
    name = "Rahaa",
    foundText = "Löysit possupankkisi, jonka tungit aikoinaan täyteen seteleitä. Juuri sopivasti rahaa rakennusmateriaalien ostamiseen.",
    usedText = "Et ole säästänyt turhaan kaikkien näiden vuosien ajan. Kaikki rahasi kuluu rakennusmateriaaleihin ja nyt toivot ettei lisäkustannuksia tule enempää.",
    itemNotUsed = "Sinulla ei ole mitään ostettavaa.",
    isSingleUse = True,
    usedIn = []
    )

materiaalit = Functional(
    name = "Materiaalit",
    foundText = "Hankit myös kasan lautaa, ruuveja, nauloja, peltiä ja kaikkea muuta tarvittavaa.",
    usedText = "Nyt kun vihdoin löysit kaiken tarvitsemasi, sait rakennettua pienen koulun. Budjettisi ei ollut kovin suuri, joten tiloja on rajallisesti. Voit nyt halutessasi palata kotiin nukkumaan tai jatkaa tutkimista. Koulu avataan vasta huomenna.",
    itemNotUsed = "Et voi rakentaa mitään juuri nyt. Varmista, että sinulla on työkalusi mukana ja että olet työmaalla.",
    isSingleUse = True,
    usedIn = []
    )

romua = Functional(
    name = "Romua",
    foundText = "Löysit ison kasan romua, jota voit käyttää rakennusmateriaalina. Näillä saat laajennettua koulun tiloja huomattavasti.",
    usedText = "Laajensit koulua rakentamalla uusia luokkahuoneita sekä varastotilan.",
    itemNotUsed = "Et voi rakentaa mitään juuri nyt. Varmista, että sinulla on työkalusi mukana ja että olet työmaalla.",
    isSingleUse = True,
    usedIn = []
    )

yöpuku = Functional(
    name = "Yöpuku",
    foundText = "Nappaat kaapistasi sinisen yöpukusi. Näytät ihan Herra Hakkaraiselta se päällä. Et halua kuitenkaan mennä vielä nukkumaan likaiset vaatteet ylläsi.",
    usedText = "Ai että. Pitkästä aikaa pääsee taas nukkumaan.",
    itemNotUsed = "Älä nyt hyvä ihminen rupea täällä vaihtamaan vaatteita!!",
    isSingleUse = False,
    usedIn = []
    )

allItems = [kartta, kärryt, kirjat, työkalut, rakennuslupa, sorkkarauta, avain, harava, rahaa, materiaalit, romua, yöpuku]