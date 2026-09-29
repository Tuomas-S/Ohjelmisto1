from classes import *

def check_environment(player):
    if kärryt in player.inventory:
        raunio.hasItem.append(romua)
    if keskusta in sorkkarauta.usedIn:
        kuja.isLocked = False

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
            player.location = työmaa
            keskusta.connections.append(työmaa)
            kauppa.connections.append(työmaa)
            työmaa.connections.append(keskusta)
            työmaa.connections.append(kauppa)
            return("Kaupunki valittu")
        if pelto in rakennuslupa.usedIn:
            player.location = työmaa
            metsä.connections.remove(pelto)
            metsä.connections.append(työmaa)
            raunio.connections.remove(pelto)
            raunio.connections.append(työmaa)
            työmaa.connections.append(metsä)
            työmaa.connections.append(raunio)
            return("Pelto valittu")

def clear_area(player):
    while True:
        player.menu("testi")
        check_environment(player)

def get_tools(player):
    kauppa.searchText = format("Kaupan hyllyt ovat täynnä rakennusmateriaaleja. Huomaat kuitenkin, että unohdit rahasi kotiin.")
    while player.location != kauppa:
        player.menu("Hanki työkalut ja materiaalit")
        check_environment(player)
    input(f"{split} \n{format("Saapuessasi kauppaan muistat, ettet pakannut rahojasi mukaan. Onneksi kotiin ei ole pitkä matka.")}")
    koti.connections.append(kellari)
    koti.searchText = format("Etsit ja etsit rahojasi kaikkialta ilman minkäänlaista tulosta. Muistat, että veit eilen tavaroitasi kellariin. Ehkä rahat löytyisivät sieltä.")
    while rahaa not in player.inventory:
        player.menu("Hae rahaa")
        check_environment(player)
    kauppa.searchText = format("Kaupan hyllyt ovat täynnä rakennusmateriaaleja.")
    input(format("Nyt on aika palata takaisin kauppaan. "))
    return("Lukossa kellarissa")

def cellar_escape(player):
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
            keskusta.isLocked = työmaa.isLocked = True
            keskusta.lockedText = format("Senkin varas! Et voi poistua ennen kuin olet maksanut ostoksesi.")
            kauppa.acceptsItem.add(rahaa)
    keskusta.isLocked = työmaa.isLocked = False
    input(f"{split} \n{format("Voit nyt palata rakennusalueelle ja rakentaa koulun. ")}")
    return("Finaali")

def finale(player):
    while materiaalit.usedIn != rakennuslupa.usedIn or työkalut.usedIn != rakennuslupa.usedIn:
        player.menu("Rakenna koulu")
        check_environment(player)