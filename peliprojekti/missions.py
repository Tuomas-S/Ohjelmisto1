from classes import *

def check_environment(player):
    if keskusta in sorkkarauta.usedIn:
        kuja.isLocked = False

    if työkalut not in player.inventory and player.location in rakennuslupa.usedIn:
        player.location.acceptsItem.discard(materiaalit) # Discard ei välitä onko olio joukossa vai ei toisin kuin remove
        player.location.acceptsItem.discard(romua)

    if työkalut in player.inventory and player.location in rakennuslupa.usedIn:
        player.location.acceptsItem.add(materiaalit)
        player.location.acceptsItem.add(romua)

    if romua in player.inventory and raunio not in romua.usedIn:
        romua.usedIn.add(raunio)
        input(f"{format("Samalla kun lastaat romua kottikärryihisi, joku varastaa sinun työkalusi ja juoksee metsän syvyyksiin. Varas ei voi piileksiä kaukana. Etsi hänet ja ota työkalusi takaisin.")} ")
        player.inventory.remove(työkalut)
        random.choice([keskusta.hasItem, metsä.hasItem, kauppa.hasItem, pelto.hasItem]).append(työkalut)
        työkalut.itemFound = format("Löydät työkaluvarkaan piileksimästä ja otat työkalusi takaisin. Varas juoksee itkien karkuun ja katoaa taivaan tuuliin.")

def tutorial(player):
    while kartta not in player.inventory:
        player.game_menu(player.status)
        check_environment(player)
    return("Valitse rakennuspaikka")

def building_spot(player):
    keskusta.isLocked = metsä.isLocked = False
    while rakennuslupa.usedIn != None:
        player.game_menu(player.status)
        check_environment(player)
        if keskusta in rakennuslupa.usedIn:
            keskusta.acceptsItem.add(materiaalit)
            keskusta.acceptsItem.add(romua)
            keskusta.searchText = format("Rakennustyömaasi kohoaa uljaasti keskustan ytimessä. Tästä tulee vielä hieno koulu.")
            return("Hanki työkalut ja materiaalit")
        if pelto in rakennuslupa.usedIn:
            pelto.acceptsItem.add(materiaalit)
            pelto.acceptsItem.add(romua)
            pelto.searchText = format("Rakennustyömaasi pistää inhottavasti silmään. Ei ehkä mikään kaunein näky, mutta ajatus on nyt tärkein.")
            return("Pelto valittu")

def clear_pelto(player):
    while True:
        player.game_menu(player.status)
        check_environment(player)

def get_tools(player):
    kauppa.searchText = format("Kaupan hyllyt ovat täynnä rakennusmateriaaleja. Huomaat kuitenkin, että unohdit rahasi kotiin.")
    while player.location != kauppa:
        player.game_menu(player.status)
        check_environment(player)
    input(f"{split} \n{format("Saapuessasi kauppaan muistat, ettet pakannut rahojasi mukaan. Onneksi kotiin ei ole pitkä matka. ")} ")
    kauppa.isLocked = True
    koti.connections.append(kellari)
    koti.searchText = format("Etsit ja etsit rahojasi kaikkialta ilman minkäänlaista tulosta. Muistat, että veit eilen tavaroitasi kellariin. Ehkä rahat löytyisivät sieltä.")
    return("Hae rahaa")

def get_money(player):
    while rahaa not in player.inventory:
        player.game_menu(player.status)
        check_environment(player)
    kauppa.searchText = format("Kaupan hyllyt ovat täynnä rakennusmateriaaleja.")
    koti.searchText = format("Kotisi näyttää ihanan tunnelmalliselta. Tahtoisit mennä takaisin nukkumaan, mutta sinulla riittää vielä tekemistä.")
    keskusta.acceptsItem.add(romua)
    kauppa.isLocked = False
    return("Palaa maan päälle")

def escape_cellar(player):
    koti.isLocked = True
    työkalut.useText = format("Työkalulaatikossasi on saha, vasara, pora sekä ruuvimeisseli. Koitat avata kellarin ovea vasaralla, mutta vipuvoima ei yksinkertaisesti riitä. Ehkä kellarista voisi löytyä jotain järeämpää.")
    kellari.hasItem.append(sorkkarauta)
    while player.location != koti:
        player.game_menu(player.status)
        check_environment(player)
        if kellari in sorkkarauta.usedIn:
            koti.isLocked = False
            sorkkarauta.useText = format("Sorkkarauta uppoaa hyvin kujaa peittävien lautojen alle. Saat kangettua naulat irti ja avaat reitin kujalle.")
    työkalut.useText = format("Työkalulaatikossasi on saha, vasara, pora sekä ruuvimeisseli. Tarvitset näitä koulun rakentamiseen.")
    return("Käy ostamassa materiaalit")

def buy_materials(player):
    kauppa.hasItem = [kärryt, materiaalit]
    while rahaa in player.inventory:
        player.game_menu(player.status)
        check_environment(player)
        if materiaalit in player.inventory and rahaa in player.inventory:
            keskusta.isLocked = True
            keskusta.lockedText = format("Ennen kuin ehdit poistua kaupasta, myyjä nappaa sinua olkapäästä kiinni ja syyttää sinua varastamisesta. Senkin lurjus!")
            kauppa.acceptsItem.add(rahaa)
    keskusta.isLocked = False
    raunio.hasItem.append(romua)
    raunio.searchText = format("Metsän laidalla sijaitsee ruhjuinen raunio. Mahtaa olla jokin hylätty tehdas tai muu teollisuusrakennus.")
    input(f"{format("Voit nyt palata rakennusalueelle. Materiaalien tulisi riittää pienen koulun rakentamiseen.")} ")
    return("Rakenna koulu")

def finale(player):
    while materiaalit.usedIn != rakennuslupa.usedIn:
        player.game_menu(player.status)
        check_environment(player)
    koti.searchText = format("Kotisi näyttää ihanan tunnelmalliselta. Takanasi on raskas päivä ja sänkysi näyttää ihanan pehmeältä.")
    return("Palaa kotiisi nukkumaan")

def ending(player):
    confirm = "definitely not ok"
    koti.hasItem.append(yöpuku)
    koti.acceptsItem.add(yöpuku)
    while confirm != "ok":
        yöpuku.usedIn = set()
        player.game_menu(player.status)
        check_environment(player)
        if koti in yöpuku.usedIn:
            confirm = input('╭─────────────────────────────────────────────────────────────╮ \n\│ Haluatko vaihtaa yövaatteet päälle ja painua sänkyyn?       │ \n╰─────────────────────────────────────────────────────────────╯ \n\n  Kirjoita "ok" vahvistaaksesi. \n  [enter] = peruuta \n\n  Valitse toiminto: ')
    return("Peli läpäisty")