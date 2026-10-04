from classes import *

name = input("\n  Nimi: ")
age = input("  Ikä:  ")
while True:
    try:
        int(age)
    except ValueError:
        age = input("  Anna oikea ikä: ")
    else:
        break
age = int(age)
if age < 12:
    input("\n  Olet alaikäinen, suljetaan sovellus... ")
    exit()
else:
    player = User(name, age, koti, "Pakkaa tavarasi mukaan", [])
    input(f"\n  Tervetuloa {name}! \n  [enter] = aloita peli ")

# Tähän intro.txt, seuraava rakenne on väliaikainen
input(f"{split} \n{format("Olet muuttanut uuteen kaupunkiin ja huomaat, ettei alueella ole mahdollisuutta minkäänlaiseen koulutukseen. Otat tehtäväksesi rakentaa kaupungin asukkaille laadukkaan koulun. Muista ottaa tavarasi mukaan ennen lähtöä.")} ")

def check_environment(player):
    if keskusta in sorkkarauta.usedIn:
        kuja.isLocked = False

    if työkalut not in player.inventory and player.location in rakennuslupa.usedIn:
        player.location.acceptsItem.remove(materiaalit)
        player.location.acceptsItem.remove(romua)

    if työkalut in player.inventory and player.location in rakennuslupa.usedIn:
        player.location.acceptsItem.extend([materiaalit, romua])

    if romua in player.inventory and raunio not in romua.usedIn:
        romua.usedIn.append(raunio)
        input(f"{format("Samalla kun lastaat romua kottikärryihisi, joku varastaa sinun työkalusi ja juoksee metsän syvyyksiin. Varas ei voi piileksiä kaukana. Etsi hänet ja ota työkalusi takaisin.")} ")
        player.inventory.remove(työkalut)
        random.choice([keskusta.hasItem, metsä.hasItem, kauppa.hasItem, pelto.hasItem]).append(työkalut)
        työkalut.itemFound = "Löydät työkaluvarkaan piileksimästä ja otat työkalusi takaisin. Varas juoksee itkien karkuun ja katoaa taivaan tuuliin."

while player.status == "Pakkaa tavarasi mukaan":
    while kartta not in player.inventory:
        player.game_menu(player.status)
        subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    player.status = "Valitse rakennuspaikka"

while player.status == "Valitse rakennuspaikka":
    keskusta.isLocked = metsä.isLocked = False
    while rakennuslupa.usedIn != None:
        player.game_menu(player.status)
        if keskusta in rakennuslupa.usedIn:
            keskusta.acceptsItem.extend([materiaalit, romua])
            keskusta.searchText = "Rakennustyömaasi kohoaa uljaasti keskustan ytimessä. Tästä tulee vielä hieno koulu."
            player.status = "Hanki työkalut ja materiaalit"
        if pelto in rakennuslupa.usedIn:
            pelto.acceptsItem.extend([materiaalit, romua])
            pelto.searchText = "Rakennustyömaasi pistää inhottavasti silmään. Ei ehkä mikään kaunein näky, mutta ajatus on nyt tärkein."
            player.status = "Hanki vajan avain"

while player.status == "Hanki työkalut ja materiaalit":
    kauppa.searchText = "Kaupan hyllyt ovat täynnä rakennusmateriaaleja. Huomaat kuitenkin, että unohdit rahasi kotiin."
    while player.location != kauppa:
        player.game_menu(player.status)
        check_environment(player)
    input(f"{split} \n{format("Saapuessasi kauppaan muistat, ettet pakannut rahojasi mukaan. Onneksi kotiin ei ole pitkä matka. ")} ")
    kauppa.isLocked = True
    koti.connections.append(kellari)
    koti.searchText = "Etsit ja etsit rahojasi kaikkialta ilman minkäänlaista tulosta. Muistat, että veit eilen tavaroitasi kellariin. Ehkä rahat löytyisivät sieltä."
    player.status = "Käy hakemassa rahaa"

while player.status == "Hanki vajan avain":
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
    player.status = "Raivaa työmaa-alue"

while player.status == "Käy hakemassa rahaa":
    kellari.hasItem.extend([rahaa, työkalut])
    while rahaa not in player.inventory:
        player.game_menu(player.status)
        check_environment(player)
    kauppa.searchText = "Kaupan hyllyt ovat täynnä rakennusmateriaaleja."
    koti.searchText = "Kotisi näyttää ihanan tunnelmalliselta. Tahtoisit mennä takaisin nukkumaan, mutta sinulla riittää vielä tekemistä."
    keskusta.acceptsItem.append(romua)
    kauppa.isLocked = False
    player.status = "Palaa maan päälle"

while player.status == "Palaa maan päälle":
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
    player.status = "Käy ostamassa materiaalit"

while player.status == "Käy ostamassa materiaalit":
    kauppa.hasItem = [kärryt, materiaalit]
    while rahaa in player.inventory:
        player.game_menu(player.status)
        check_environment(player)
        if materiaalit in player.inventory and rahaa in player.inventory:
            keskusta.isLocked = True
            keskusta.lockedText = "Ennen kuin ehdit poistua kaupasta, myyjä nappaa sinua olkapäästä kiinni ja syyttää sinua varastamisesta. Senkin lurjus!"
            kauppa.acceptsItem.append(rahaa)
    keskusta.isLocked = False
    raunio.searchText = "Metsän laidalla sijaitsee ruhjuinen raunio. Mahtaa olla jokin hylätty tehdas tai muu teollisuusrakennus. Kottikärrysi ovat täynnä rakennusmateriaaleja ja sinun tulee palata takaisin tyhjien kärryjen kanssa, jos haluat kerätä lisää materiaaleja."
    input(f"{format("Voit nyt palata rakennusalueelle. Materiaalien tulisi riittää pienen koulun rakentamiseen.")} ")
    player.status = "Rakenna koulu"

while player.status == "Rakenna koulu":
    while materiaalit.usedIn != rakennuslupa.usedIn:
        player.game_menu(player.status)
        check_environment(player)
    koti.searchText = "Kotisi näyttää ihanan tunnelmalliselta. Takanasi on raskas päivä ja sänkysi näyttää ihanan pehmeältä."
    raunio.hasItem.append(romua)
    raunio.searchText = "Metsän laidalla sijaitsee ruhjuinen raunio. Mahtaa olla jokin hylätty tehdas tai muu teollisuusrakennus."
    player.status = "Palaa kotiisi nukkumaan"

while player.status == "Palaa kotiisi nukkumaan":
    confirm = None
    koti.hasItem.append(yöpuku)
    koti.acceptsItem.append(yöpuku)
    while confirm != "ok":
        yöpuku.usedIn = set()
        player.game_menu(player.status)
        check_environment(player)
        if koti in yöpuku.usedIn:
            confirm = input('╭─────────────────────────────────────────────────────────────╮ \n\│ Haluatko vaihtaa yövaatteet päälle ja painua sänkyyn?       │ \n╰─────────────────────────────────────────────────────────────╯ \n\n  Kirjoita "ok" vahvistaaksesi. \n  [enter] = peruuta \n\n  Valitse toiminto: ')
    player.status = "Peli läpäisty"

if kirjat in player.inventory:
    if keskusta not in romua.usedIn and pelto not in romua.usedIn:
        input(f"{split} \n{format("Rakensit koulun ja koulutuksen laatu on erinomaista. Kaupungin asukkaat kuitenkin valittavat tilojen ja luokkahuoneiden puutteesta Pisteet: ★ ★ ☆")} ")
    else:
        input(f"{split} \n{format("Rakensit koulun ja koulutuksen laatu on erinomaista. Uusien tilojen ansiosta oppilailla on viihtyisämpää koulussa. Pisteet: ★ ★ ★")} ")
else:
    if keskusta not in romua.usedIn and pelto not in romua.usedIn:
        input(f"{split} \n{format("Rakensit koulun, mutta koulutuksen laadussa on puutteita. Kaupungin asukkaat valittavat myös tilojen ja luokkahuoneiden puutteesta Pisteet: ★ ☆ ☆")} ")
    else:
        input(f"{split} \n{format("Rakensit koulun, mutta koulutuksen laadussa on puutteita. Olet saanut kuitenkin kehuja koulun tiloista ja viihtyvyydestä. Pisteet: ★ ★ ☆")} ")