from classes import *

def check_environment(player):
    if keskusta in sorkkarauta.usedIn:
        kuja.isLocked = False
    if työkalut not in player.inventory and player.location in rakennuslupa.usedIn:
        player.location.acceptsItem = {rakennuslupa, sorkkarauta}
    if työkalut in player.inventory and player.location in rakennuslupa.usedIn:
        player.location.acceptsItem.add(materiaalit)
        player.location.acceptsItem.add(romua)

def tutorial(player):
    while kartta not in player.inventory:
        player.menu("Pakkaa tavarasi mukaan")
        check_environment(player)
    return("Tutoriaali valmis")

def building_spot(player):
    keskusta.isLocked = metsä.isLocked = False
    while rakennuslupa.usedIn != None:
        player.menu("Valitse rakennuspaikka")
        check_environment(player)
        if keskusta in rakennuslupa.usedIn:
            keskusta.acceptsItem.add(materiaalit)
            keskusta.acceptsItem.add(romua)
            return("Kaupunki valittu")
        if pelto in rakennuslupa.usedIn:
            pelto.acceptsItem.add(materiaalit)
            pelto.acceptsItem.add(romua)
            return("Pelto valittu")

def clear_niitty(player):
    while True:
        player.menu("testi")
        check_environment(player)

def get_tools(player):
    kauppa.searchText = format("Kaupan hyllyt ovat täynnä rakennusmateriaaleja. Huomaat kuitenkin, että unohdit rahasi kotiin.")
    while player.location != kauppa:
        player.menu("Hanki työkalut ja materiaalit")
        check_environment(player)
    input(f"{split} \n{format("Saapuessasi kauppaan muistat, ettet pakannut rahojasi mukaan. Onneksi kotiin ei ole pitkä matka. ")}")
    koti.connections.append(kellari)
    koti.searchText = format("Etsit ja etsit rahojasi kaikkialta ilman minkäänlaista tulosta. Muistat, että veit eilen tavaroitasi kellariin. Ehkä rahat löytyisivät sieltä.")
    while rahaa not in player.inventory:
        player.menu("Hae rahaa")
        check_environment(player)
    kauppa.searchText = format("Kaupan hyllyt ovat täynnä rakennusmateriaaleja.")
    keskusta.acceptsItem.add(romua)
    input(format("Nyt on aika palata takaisin kauppaan. "))
    return("Lukossa kellarissa")

def escape_cellar(player):
    koti.isLocked = True
    kellari.hasItem.append(sorkkarauta)
    while player.location != koti:
        player.menu("Osta materiaalit")
        check_environment(player)
        if kellari in sorkkarauta.usedIn:
            koti.isLocked = False
            sorkkarauta.useText = format("Sorkkarauta uppoaa hyvin kujaa peittävien lautojen alle. Saat kangettua naulat irti ja avaat reitin kujalle.")
    return("Kauppaan ostoksille")

def buy_materials(player):
    kauppa.hasItem = [kärryt, materiaalit]
    while rahaa in player.inventory:
        player.menu("Osta materiaalit")
        check_environment(player)
        if materiaalit in player.inventory and rahaa in player.inventory:
            keskusta.isLocked = True
            keskusta.lockedText = format("Senkin varas! Et voi poistua ennen kuin olet maksanut ostoksesi.")
            kauppa.acceptsItem.add(rahaa)
    keskusta.isLocked = False
    raunio.hasItem.append(romua)
    raunio.searchText = format("Metsän laidalla sijaitsee ruhjuinen raunio. Mahtaa olla jokin hylätty tehdas tai muu teollisuusrakennus.")
    input(format("Voit nyt palata rakennusalueelle ja rakentaa koulun. "))
    return("Finaali")

def finale(player):
    while materiaalit.usedIn != rakennuslupa.usedIn:
        player.menu("Rakenna koulu")
        check_environment(player)
    return("Kotiin nukkumaan")

def ending(player):
    while True:
        player.menu("Palaa kotiisi nukkumaan")
        check_environment(player)