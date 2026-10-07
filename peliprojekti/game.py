from user import *
from text_format import *

while True:
    player.main_menu()

    def check_environment(player):
        if keskusta in sorkkarauta.usedIn:
            kuja.isLocked = False

        if työkalut not in player.inventory and player.location in rakennuslupa.usedIn:
            if materiaalit in player.location.acceptsItem:
                player.location.acceptsItem.remove(materiaalit)
            if romua in player.location.acceptsItem:
                player.location.acceptsItem.remove(romua)
        if työkalut in player.inventory and player.location in rakennuslupa.usedIn:
            player.location.acceptsItem.extend([materiaalit, romua])

        if romua in player.inventory and raunio not in romua.usedIn:
            romua.usedIn.append(raunio)
            input(f"\n{divide("Samalla kun lastaat romua kottikärryihisi, joku varastaa sinun työkalusi ja juoksee metsän syvyyksiin. Varas ei voi piileksiä kaukana. Etsi hänet ja ota työkalusi takaisin.")}")
            player.inventory.remove(työkalut)
            random.choice([keskusta.hasItem, metsä.hasItem, kauppa.hasItem, pelto.hasItem]).append(työkalut)
            työkalut.foundText = "Löydät työkaluvarkaan piileksimästä ja otat työkalusi takaisin. Varas juoksee itkien karkuun ja katoaa taivaan tuuliin."

    while player.status == "Pakkaa tavarasi mukaan":
        input(divide("Olet muuttanut uuteen kaupunkiin ja huomaat, ettei alueella ole mahdollisuutta minkäänlaiseen koulutukseen. Otat tehtäväksesi rakentaa kaupungin asukkaille laadukkaan koulun. Muista ottaa tavarasi mukaan ennen lähtöä."))
        clear_shell()
        while kartta not in player.inventory:
            player.game_menu(player.status)
        keskusta.isLocked = metsä.isLocked = False
        player.status = "Valitse rakennuspaikka"

    while player.status == "Valitse rakennuspaikka":
        while rakennuslupa in player.inventory:
            player.game_menu(player.status)
        if keskusta in rakennuslupa.usedIn:
            keskusta.acceptsItem.extend([materiaalit, romua])
            keskusta.searchText = "Rakennustyömaasi kohoaa uljaasti keskustan ytimessä. Tästä tulee vielä hieno koulu."
            kauppa.searchText = "Kaupan hyllyt ovat täynnä rakennusmateriaaleja. Huomaat kuitenkin, että unohdit rahasi kotiin."
            player.status = "Hanki työkalut ja materiaalit"
        if pelto in rakennuslupa.usedIn:
            pelto.acceptsItem.extend([materiaalit, romua])
            pelto.searchText = "Rakennustyömaasi pistää inhottavasti silmään. Ei ehkä mikään kaunein näky, mutta ajatus on nyt tärkein."
            koti.searchText = "Löydät avaimesi lipaston alta, muttet yletä ottamaan sitä. Ehkä kellarista löytyisi jotain kättä pidempää."
            sorkkarauta.foundText = "Kellarin seinustalla nojaava sorkkarauta voisi olla tarpeeksi pitkä avaimen saamiseen."
            metsä.connections.append(vaja)
            koti.connections.append(kellari)
            kellari.hasItem.append(sorkkarauta)
            input(f"\n{divide("Ennen kuin pääset rakentamaan pellolle, sinun tulee raivata alue. Kotisi lähellä metsän siimeksessä sijaitsee pieni vaja, jossa on työvälineitä. Muistaisit sen olevan lukossa.")}")
            player.status = "Hanki vajan avain"

    while player.status == "Hanki työkalut ja materiaalit":
        while player.location != kauppa:
            player.game_menu(player.status)
            check_environment(player)
        kauppa.isLocked = True
        koti.connections = [keskusta, metsä, kellari]
        koti.searchText = "Etsit ja etsit rahojasi kaikkialta ilman minkäänlaista tulosta. Muistat, että veit eilen tavaroitasi kellariin. Ehkä rahat löytyisivät sieltä."
        kellari.hasItem.extend([rahaa, työkalut])
        input(fancyLine + divide("Saapuessasi kauppaan muistat, ettet pakannut rahojasi mukaan. Onneksi kotiin ei ole pitkä matka."))
        player.status = "Käy hakemassa rahaa"

    while player.status == "Hanki vajan avain":
        while avain not in player.inventory:
            player.game_menu(player.status)
            check_environment(player)
            if sorkkarauta in player.inventory and koti not in sorkkarauta.usedIn:
                koti.hasItem.append(avain)
                sorkkarauta.usedIn.append(koti)
                koti.searchText = "Kotisi näyttää ihanan tunnelmalliselta. Tahtoisit mennä takaisin nukkumaan, mutta sinulla riittää vielä tekemistä."
        vaja.lockedText = "Vajan ovi on lukittu. Käytä avain päästäksesi sisään."
        pelto.searchText = "Tarvitset haravan sekä kottikärryt raivataksesi pellon. Ne löytyvät vajasta metsän vierestä."
        input(f"\n{divide("Tämän avaimen tulisi käydä vajan oveen. Käy hakemassa työvälineet ja ryhdy talkoisiin.")}")
        player.status = "Raivaa pelto"

    while player.status == "Käy hakemassa rahaa":
        while rahaa not in player.inventory:
            player.game_menu(player.status)
            check_environment(player)
        kauppa.searchText = "Kaupan hyllyt ovat täynnä rakennusmateriaaleja."
        koti.searchText = "Kotisi näyttää ihanan tunnelmalliselta. Tahtoisit mennä takaisin nukkumaan, mutta sinulla riittää vielä tekemistä."
        keskusta.acceptsItem.append(romua)
        kauppa.isLocked = False
        koti.isLocked = True
        sorkkarauta.usedText = "Revit oven hajalle sorkkaraudalla ja näet taas päivänvaloa. Melkein kävi huonosti."
        työkalut.usedText = "Työkalulaatikossasi on saha, vasara, pora sekä ruuvimeisseli. Koitat avata kellarin ovea vasaralla, mutta vipuvoima ei yksinkertaisesti riitä. Ehkä kellarista voisi löytyä jotain järeämpää."
        kellari.hasItem.append(sorkkarauta)
        kellari.acceptsItem.append(sorkkarauta)
        player.status = "Palaa maan päälle"

    while player.status == "Raivaa pelto":
        while pelto not in harava.usedIn:
            player.game_menu(player.status)
            check_environment(player)
            if metsä in avain.usedIn:
                vaja.isLocked = False
            if kärryt in player.inventory:
                raunio.searchText = "Metsän laidalla sijaitsee ruhjuinen raunio. Alue on täynnä käyttökelpoista materiaalia. Et omista työkaluja joilla saisit kerättyä nämä talteen."
        input(f"\n{divide("Onneksi sait suurimman osan alueesta siistittyä. Nyt sinun kannattaa hakea kaupasta työkalut ja rakennusmateriaalit.")}")
        pelto.searchText = "Rakennustyömaasi pistää inhottavasti silmään. Ei ehkä mikään kaunein näky, mutta ajatus on nyt tärkein."
        player.status = "Käy kaupassa"

    while player.status == "Palaa maan päälle":
        while player.location != koti:
            player.game_menu(player.status)
            check_environment(player)
            if kellari in sorkkarauta.usedIn:
                koti.isLocked = False
                sorkkarauta.usedText = "Sorkkarauta uppoaa hyvin kujaa peittävien lautojen alle. Saat kangettua naulat irti ja avaat reitin kujalle."
        työkalut.usedText = "Työkalulaatikossasi on saha, vasara, pora sekä ruuvimeisseli. Tarvitset näitä koulun rakentamiseen."
        kauppa.hasItem.extend([kärryt, materiaalit])
        player.status = "Osta rakennustarvikkeet"

    while player.status == "Käy kaupassa":
        while player.location != metsä:
            player.game_menu(player.status)
            check_environment(player)
        kauppa.hasItem.extend([työkalut, materiaalit])
        työkalut.foundText = "Ihailet kiiltäviä työvälineitä ja päätät ottaa niitä ihan runsaasti. Mukaasi lähtee vasara, pihdit, saha, mittanauha, sekä Milwaukeen ruuvinväännin."
        rahaa.usedText = "Mikä mäihä! Oravan antamat rahat menivät hyvään käyttöön. Säästät huomattavasti rahaa ja nyt voit jopa tilata huoltomiehet tarkistamaan kellarisi hajuhaittojen lähteen."
        player.inventory.append(rahaa)
        input(fancyLine + divide("Kulkiessasi metsän läpi törmäät puhuvaan oravaan. Hän näkee kottikärryissäsi kasan lehtiä ja tarjoaa rahaa vastineeksi niistä."))
        input(f"\n{divide("Hetken hämmästeltyäsi päätät ottaa tarjouksen vastaan ja saat oravalta huiman kasan rahaa. Mitäköhän laittomuuksia näihinkin seteleihin liittyy...")}")
        player.status = "Osta rakennustarvikkeet"

    while player.status == "Osta rakennustarvikkeet":
        while kauppa not in rahaa.usedIn:
            player.game_menu(player.status)
            check_environment(player)
            if materiaalit in player.inventory and rahaa in player.inventory:
                keskusta.isLocked = True
                keskusta.lockedText = "Ennen kuin ehdit poistua kaupasta, myyjä nappaa sinua olkapäästä kiinni ja syyttää sinua varastamisesta. Senkin lurjus!"
                kauppa.acceptsItem = [rahaa]
        raunio.searchText = "Metsän laidalla sijaitsee ruhjuinen raunio. Mahtaa olla jokin hylätty tehdas tai muu teollisuusrakennus. Kottikärrysi ovat täynnä rakennusmateriaaleja ja sinun tulee palata takaisin tyhjien kärryjen kanssa, jos haluat kerätä lisää materiaaleja."
        keskusta.isLocked = False
        input(f"\n{divide("Voit nyt palata rakennusalueelle. Materiaalien tulisi riittää pienen koulun rakentamiseen. Käytä materiaalit rakennusalueellasi aloittaaksesi rakentamisen.")}")
        player.status = "Viimeistele koulu"

    while player.status == "Viimeistele koulu":
        while materiaalit.usedIn != rakennuslupa.usedIn:
            player.game_menu(player.status)
            check_environment(player)
        koti.searchText = "Kotisi näyttää ihanan tunnelmalliselta. Takanasi on raskas päivä ja sänkysi näyttää ihanan pehmeältä."
        raunio.hasItem.append(romua)
        rakennuslupa.usedin[0].searchText = "Siinä se koulu seisoo uljaana. Saat olla aika ylpeä siitä, mitä olet saanut aikaan."
        raunio.searchText = "Metsän laidalla sijaitsee ruhjuinen raunio. Mahtaa olla jokin hylätty tehdas tai muu teollisuusrakennus."
        koti.hasItem.append(yöpuku)
        koti.acceptsItem.append(yöpuku)
        player.status = "Palaa kotiisi nukkumaan"

    while player.status == "Palaa kotiisi nukkumaan":
        confirm = "hereillä ollaan"
        while confirm.lower() != "zzz":
            yöpuku.usedIn = []
            player.game_menu(player.status)
            check_environment(player)
            if koti in yöpuku.usedIn:
                confirm = input('\n» Kirjoita "Zzz" nukahtaaksesi: ')
        player.status = "Peli läpäisty"

    clear_shell()
    if kirjat in player.inventory:
        if keskusta not in romua.usedIn and pelto not in romua.usedIn:
            input(fancyLine + divide("Rakensit koulun ja koulutuksen laatu on erinomaista. Kaupungin asukkaat kuitenkin valittavat tilojen ja luokkahuoneiden puutteesta. \n\n  Pisteet: ★ ★ ☆"))
        else:
            input(fancyLine + divide("Rakensit koulun ja koulutuksen laatu on erinomaista. Uusien tilojen ansiosta oppilailla on viihtyisämpää koulussa. \n\n  Pisteet: ★ ★ ★"))
    else:
        if keskusta not in romua.usedIn and pelto not in romua.usedIn:
            input(fancyLine + divide("Rakensit koulun, mutta koulutuksen laadussa on puutteita. Kaupungin asukkaat valittavat myös tilojen ja luokkahuoneiden puutteesta \n\n  Pisteet: ★ ☆ ☆"))
        else:
            input(fancyLine + divide("Rakensit koulun, mutta koulutuksen laadussa on puutteita. Olet saanut kuitenkin kehuja koulun tiloista ja viihtyvyydestä. \n\n  Pisteet: ★ ★ ☆"))
    os.remove("peliprojekti/game_data.json")
    clear_shell()