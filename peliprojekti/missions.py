from classes import *

def check_environment(player):
    if keskusta in sorkkarauta.usedIn:
        kuja.isLocked = False

    if työkalut not in player.inventory and player.location in rakennuslupa.usedIn:
        player.location.acceptsItem.discard(materiaalit) # Discard ei välitä onko olio joukossa vai ei toisin kuin remove
        player.location.acceptsItem.discard(romua)

    if työkalut in player.inventory and player.location in rakennuslupa.usedIn:
        player.location.acceptsItem.extend([materiaalit, romua])

    if romua in player.inventory and raunio not in romua.usedIn:
        romua.usedIn.append(raunio)
        input(f"{format("Samalla kun lastaat romua kottikärryihisi, joku varastaa sinun työkalusi ja juoksee metsän syvyyksiin. Varas ei voi piileksiä kaukana. Etsi hänet ja ota työkalusi takaisin.")} ")
        player.inventory.remove(työkalut)
        random.choice([keskusta.hasItem, metsä.hasItem, kauppa.hasItem, pelto.hasItem]).append(työkalut)
        työkalut.itemFound = "Löydät työkaluvarkaan piileksimästä ja otat työkalusi takaisin. Varas juoksee itkien karkuun ja katoaa taivaan tuuliin."

def tutorial(player):
    while kartta not in player.inventory:
        player.game_menu(player.status)
    return("Valitse rakennuspaikka")

def building_spot(player):
    keskusta.isLocked = metsä.isLocked = False
    while rakennuslupa.usedIn != None:
        player.game_menu(player.status)
        if keskusta in rakennuslupa.usedIn:
            keskusta.acceptsItem.extend([materiaalit, romua])
            keskusta.searchText = "Rakennustyömaasi kohoaa uljaasti keskustan ytimessä. Tästä tulee vielä hieno koulu."
            return("Hanki työkalut ja materiaalit")
        if pelto in rakennuslupa.usedIn:
            pelto.acceptsItem.extend([materiaalit, romua])
            pelto.searchText = "Rakennustyömaasi pistää inhottavasti silmään. Ei ehkä mikään kaunein näky, mutta ajatus on nyt tärkein."
            return("Hanki vajan avain")

def get_key(player):
    input(f"{format("Ennen kuin pääset rakentamaan pellolle, sinun tulee raivata alue. Kotisi lähellä metsän siimeksessä sijaitsee pieni vaja, jossa on harava sekä kottikärryt. Muistaisit sen olevan lukossa.")} ")
    metsä.connections.append(vaja)
    koti.connections.append(kellari)
    kellari.hasItem.append(sorkkarauta)
    koti.searchText = "Löydät avaimesi lipaston alta, muttet yletä ottamaan sitä. Ehkä kellarista löytyisi jotain kättä pidempää."
    while avain not in player.inventory:
        player.game_menu(player.status)
        if sorkkarauta in player.inventory:
            koti.hasItem.append(avain)
            koti.searchText = "Kotisi näyttää ihanan tunnelmalliselta. Tahtoisit mennä takaisin nukkumaan, mutta sinulla riittää vielä tekemistä."
    return("Raivaa työmaa-alue")

def visit_store(player):
    kauppa.searchText = "Kaupan hyllyt ovat täynnä rakennusmateriaaleja. Huomaat kuitenkin, että unohdit rahasi kotiin."
    while player.location != kauppa:
        player.game_menu(player.status)
        check_environment(player)
    input(f"{split} \n{format("Saapuessasi kauppaan muistat, ettet pakannut rahojasi mukaan. Onneksi kotiin ei ole pitkä matka. ")} ")
    kauppa.isLocked = True
    koti.connections.append(kellari)
    koti.searchText = "Etsit ja etsit rahojasi kaikkialta ilman minkäänlaista tulosta. Muistat, että veit eilen tavaroitasi kellariin. Ehkä rahat löytyisivät sieltä."
    return("Käy hakemassa rahaa")

def get_money(player):
    kellari.hasItem.extend([rahaa, työkalut])
    while rahaa not in player.inventory:
        player.game_menu(player.status)
        check_environment(player)
    kauppa.searchText = "Kaupan hyllyt ovat täynnä rakennusmateriaaleja."
    koti.searchText = "Kotisi näyttää ihanan tunnelmalliselta. Tahtoisit mennä takaisin nukkumaan, mutta sinulla riittää vielä tekemistä."
    keskusta.acceptsItem.append(romua)
    kauppa.isLocked = False
    return("Palaa maan päälle")

def escape_cellar(player):
    koti.isLocked = True
    työkalut.itemUsed = "Työkalulaatikossasi on saha, vasara, pora sekä ruuvimeisseli. Koitat avata kellarin ovea vasaralla, mutta vipuvoima ei yksinkertaisesti riitä. Ehkä kellarista voisi löytyä jotain järeämpää."
    kellari.hasItem.append(sorkkarauta)
    kellari.acceptsItem.append(sorkkarauta)
    while player.location != koti:
        player.game_menu(player.status)
        check_environment(player)
        if kellari in sorkkarauta.usedIn:
            koti.isLocked = False
            sorkkarauta.itemUsed = "Sorkkarauta uppoaa hyvin kujaa peittävien lautojen alle. Saat kangettua naulat irti ja avaat reitin kujalle."
    työkalut.itemUsed = "Työkalulaatikossasi on saha, vasara, pora sekä ruuvimeisseli. Tarvitset näitä koulun rakentamiseen."
    return("Käy ostamassa materiaalit")

def buy_materials(player):
    kauppa.hasItem = [kärryt, materiaalit]
    while rahaa in player.inventory:
        player.game_menu(player.status)
        check_environment(player)
        if materiaalit in player.inventory and rahaa in player.inventory:
            keskusta.isLocked = True
            keskusta.cantEnter = "Ennen kuin ehdit poistua kaupasta, myyjä nappaa sinua olkapäästä kiinni ja syyttää sinua varastamisesta. Senkin lurjus!"
            kauppa.acceptsItem.append(rahaa)
    keskusta.isLocked = False
    raunio.searchText = "Metsän laidalla sijaitsee ruhjuinen raunio. Mahtaa olla jokin hylätty tehdas tai muu teollisuusrakennus. Kottikärrysi ovat täynnä rakennusmateriaaleja ja sinun tulee palata takaisin tyhjien kärryjen kanssa, jos haluat kerätä lisää materiaaleja."
    input(f"{format("Voit nyt palata rakennusalueelle. Materiaalien tulisi riittää pienen koulun rakentamiseen.")} ")
    return("Rakenna koulu")

def finale(player):
    while materiaalit.usedIn != rakennuslupa.usedIn:
        player.game_menu(player.status)
        check_environment(player)
    koti.searchText = "Kotisi näyttää ihanan tunnelmalliselta. Takanasi on raskas päivä ja sänkysi näyttää ihanan pehmeältä."
    raunio.hasItem.append(romua)
    raunio.searchText = "Metsän laidalla sijaitsee ruhjuinen raunio. Mahtaa olla jokin hylätty tehdas tai muu teollisuusrakennus."
    return("Palaa kotiisi nukkumaan")

def ending(player):
    confirm = None
    koti.hasItem.append(yöpuku)
    koti.acceptsItem.append(yöpuku)
    while confirm != "ok":
        yöpuku.usedIn = set()
        player.game_menu(player.status)
        check_environment(player)
        if koti in yöpuku.usedIn:
            confirm = input('╭─────────────────────────────────────────────────────────────╮ \n\│ Haluatko vaihtaa yövaatteet päälle ja painua sänkyyn?       │ \n╰─────────────────────────────────────────────────────────────╯ \n\n  Kirjoita "ok" vahvistaaksesi. \n  [enter] = peruuta \n\n  Valitse toiminto: ')
    return("Peli läpäisty")