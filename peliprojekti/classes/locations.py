from classes.items import *

class Location:
    def __init__(self, name, searchText, isLocked, lockedText, hasItem, acceptsItem, connections = None):
        self.name = name # sijainnin nimi
        self.searchText = searchText # tämä tulostetaan kun sijaintia tutkitaan
        self.isLocked = isLocked # onko pelaajalla pääsyä sijaintiin vai ei
        self.lockedText = lockedText # tämä tulostuu jos koitetaan siirtyä lukittuun sijaintiin
        self.hasItem = hasItem # sijainnista löytyvät esineet (lista)
        self.acceptsItem = acceptsItem # mitä esinettä sijainnissa voi käyttää
        self.connections = connections # joukko paikoista mihin tästä sijainnista pääsee

    # Muokkaa olion sanakirjamuotoon
    def to_dictionary(self):
        return {
            "name": self.name,
            "searchText": self.searchText,
            "isLocked": self.isLocked,
            "lockedText": self.lockedText,
            "hasItem": [item.name for item in self.hasItem],
            "acceptsItem": [item.name for item in self.acceptsItem],
            "connections": [location.name for location in self.connections]
        }
    

keskusta = Location(
    name = "Keskusta",
    searchText = "Kaupunki on täynnä vilinää ja melua. Nauttisit mieluummin ajastasi luonnossa.",
    isLocked = True,
    lockedText = "Pakkaa tavarasi mukaan ennen keskustaan suuntaamista. Tutki aluetta kunnes inventaariostasi löytyy sekä kartta että rakennuslupa.",
    hasItem = [],
    acceptsItem = [rakennuslupa, sorkkarauta],
    connections = []
    )

koti = Location(
    name = "Koti",
    searchText = "Kotisi näyttää ihanan tunnelmalliselta. Tahtoisit mennä takaisin nukkumaan, mutta sinulla riittää vielä tekemistä.",
    isLocked = False,
    lockedText = "Rahoja etsiessä työnsit vahingossa kellarin oven kiinni ja lukitsit sen. Olet jumissa...",
    hasItem = [kartta, rakennuslupa],
    acceptsItem = [kirjat],
    connections = []
)

kellari = Location(
    name = "Kellari",
    searchText = "Rähjäinen hämärä kellarisi haisee tunkkaiselta. Toivottavasti ei ole mitään homeongelmia tai muuten voi tulla kalliiksi.",
    isLocked = False,
    lockedText = "Huhhuh. Tonne ei kannata enää mennä.",
    hasItem = [],
    acceptsItem = [],
    connections = []
)

kuja = Location(
    name = "Kuja",
    searchText = 'Kujalla on erittäin ahdasta ja likaista. Kujan toisessa päässä on ovi, jossa on numerolukko. Oven vieressä on pieni lappu, jossa lukee "Koti, Kauppa, Keskusta, Pelto, Kuja".',
    isLocked = True,
    lockedText = "Kujalle vievä portti on muurattu kiinni laudoilla. Koitat repiä niitä irti mutta naulat ovat liian lujasti kiinni.",
    hasItem = [],
    acceptsItem = [],
    connections = []
)

metsä = Location(
    name = "Metsä",
    searchText = "Tunnet raikkaan ilman keuhkoissasi ja nenääsi tunkeutuu ihana luonnon tuoksu. Ehkä joku päivä voisit tulla tänne telttaretkelle.",
    isLocked = True,
    lockedText = "Pakkaa tavarasi mukaan ennen metsään suuntaamista. Tutki aluetta kunnes inventaariostasi löytyy sekä kartta että rakennuslupa.",
    hasItem = [],
    acceptsItem = [avain],
    connections = []
)

kauppa = Location(
    name = "Kauppa",
    searchText = "Kaupan hyllyt ovat täynnä rakennusmateriaaleja.",
    isLocked = False,
    lockedText = "Sinun kannattaa hakea kotoasi rahaa ennen kauppaan palaamista.",
    hasItem = [],
    acceptsItem = [],
    connections = []
)

raunio = Location(
    name = "Raunio",
    searchText = "Löydät metsän laidalta raunion. Mahtaa olla jokin hylätty tehdas. Alueelta löytyy erilaisia materiaaleja joista voisi olla hyötyä koulun rakentamisessa. Et jaksa kuitenkaan kantaa niitä.",
    isLocked = False,
    lockedText = "Ei ole lukittu",
    hasItem = [],
    acceptsItem = [],
    connections = []
)

varasto = Location(
    name = "Varasto",
    searchText = "Laitat varaston valot päälle. Tomua kaikkialla. Et välttämättä halua lorvailla täällä turhan kauaa ellet halua tuberkuloosia.",
    isLocked = True,
    lockedText = "Rakennuksen ovi on lukossa. Anna 5-numeroinen koodi päästäksesi sisään: ",
    hasItem = [kirjat],
    acceptsItem = [],
    connections = []
)

pelto = Location(
    name = "Pelto",
    searchText = "Tämä pelto ei ole mikään kaunein nähtävyys. Enemmän sitä voisi kutsua ryteiköksi tai vaikka taistelukentäksi.",
    isLocked = False,
    lockedText = "Ei ole lukittu",
    hasItem = [],
    acceptsItem = [rakennuslupa, harava],
    connections = []
)

vaja = Location(
    name = "Vaja",
    searchText = "Haistat jotain mätääntynyttä. Et muista milloin viimeksi olisit käynyt täällä.",
    isLocked = True,
    lockedText = "Tirkistelet lautojen välistä vajan sisään. Näet kottikärryt sekä haravan. Ovi on lukittu, mutta avaimen pitäisi löytyä kotoasi.",
    hasItem = [kärryt, harava],
    acceptsItem = [],
    connections = []
)

# Sijaintien väliset yhteydet
keskusta.connections.extend([koti, metsä, kauppa, kuja])
koti.connections.extend([keskusta, metsä])
kellari.connections.extend([koti])
kuja.connections.extend([keskusta, varasto])
metsä.connections.extend([koti, keskusta, pelto, raunio])
kauppa.connections.extend([keskusta])
raunio.connections.extend([metsä, pelto])
varasto.connections.extend([kuja])
pelto.connections.extend([metsä, raunio])
vaja.connections.extend([metsä])

allLocations = [keskusta, koti, kellari, kuja, metsä, kauppa, raunio, varasto, pelto, vaja]