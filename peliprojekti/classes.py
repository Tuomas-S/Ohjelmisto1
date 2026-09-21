split = "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━▶\n"
import time
import random
#import game

class item:
    def __init__(self, name, found_text, is_heavy = False, is_used = False):
        self.name = name # esineen nimi
        self.found_text = found_text # tämä tulostuu esineen löytyessä
        self.is_heavy = is_heavy # voiko esineen ottaa vain apuvälineen kanssa
        self.is_used = is_used # onko pelaaja käyttänyt esineen
        
class location:
    def __init__(self, name, search_text, item = None, accepts_item = None, access_to = None):
        self.name = name # sijainnin nimi
        self.search_text = search_text # tämä tulostetaan kun sijaintia tutkitaan
        self.item = item # sijainnista löytyvä esine
        self.accepts_item = accepts_item # mitä esinettä sijainnissa voi käyttää
        self.access_to = access_to # lista paikoista mihin tästä sijainnista pääsee

class user:
    def __init__(self, name, age, location, inventory = [], can_carry = False):
        self.name = name # pelaajan asettama nimi
        self.age = age # pelaajan asettama ikä
        self.inventory = inventory # inventaario
        self.location = location # nykyinen sijainti
        self.can_carry = can_carry # voiko lisätä painavia esineitä inventaarioon

    def move(self, move_to):
        has_moved = False
        while has_moved == False:
            print(f"{split} \nVoit liikkua seuraaviin paikkoihin:")
            for location in move_to.access_to:
                print(f"- {location.name}")
            choice = input("\n[enter] = Takaisin \nLiiku paikkaan kirjoittamalla sen nimi. \n\nValitse toiminto: ")
            if choice == "":
                has_moved = True
                break
            else:
                for location in move_to.access_to:
                    if choice.lower() == location.name.lower():
                        input(f"{split} \nSiirrytään paikkaan {location.name.lower()}. ")
                        self.location = location
                        has_moved = True
                        break
                else:
                    input(f"{split} \nSijaintia ei löytynyt. ")

    def search(self, location):
        if location.item != None:
            if location.item.is_heavy == True and self.can_carry == False:
                print(f"{split} \n{location.search_text}")
                input("\nTäältähän löytyy paljon romua. \nOn kyl vähän liian raskasta kannettavaks. ")
            else:
                print(f"{split} \n{location.search_text}")
                input(f"\n{location.item.found_text} ")
                self.inventory.append(location.item)
                location.item = None
        else:
            print(f"{split} \n{location.search_text}")
            input("\nEt löytänyt alueelta mitään merkittävää. ")

    def item_use(self, choice):
        if choice.lower() == "kartta":
            print(f"{split} \nAvataan kartta...")
            time.sleep(random.randrange(1, 3))
            input("\n   ╭── [ Keskusta ] ──┬── [ Koti ] \n   │        │         │       │ \n[ Kuja ]    │         ╰── [ Metsä ] ───╮ \n   │        │                 │        │ \n   │    [ Kauppa ]            │    [ Raunio ] \n   │                          │        │ \n   ╰─ [ ??? ]             [ Aukio ] ───╯ \n\n[enter] = Takaisin")
            return(False)
        else:
            for item in self.inventory:
                if choice.lower() == item.name.lower():
                    if item == self.location.accepts_item:
                        print(f"{split} \nKäytetään {item.name.lower()}...")
                        time.sleep(random.randrange(1, 3))
                        item.is_used = True
                        self.inventory.remove(item)
                        return(True)
                    else:
                        input(f"{split} \nEt voi käyttää esinettä juuri nyt. ")
                        return(False)
            else:
                input(f"{split} \nEsinettä ei löytynyt inventaariostasi. ")
                return(False)

    def inv_show(self):
        is_used = False
        while is_used == False:
            if self.inventory == []:
                input(f"{split} \nInventaariosi on tyhjä. Täältä näet löytämäsi esineet. \n\n[enter] = Takaisin \n\nValitse toiminto: ")
                break
            else:
                print(f"{split} \nInventaariossasi on:")
                for item in self.inventory:
                    print(f"- {item.name}")
                choice = input("\n[enter] = Takaisin \nKäytä esine kirjoittamalla sen nimi. \n\nValitse toiminto: ")
                if choice == "":
                    break
                else:
                    is_used = self.item_use(choice)

    def menu(self):
        print(f"{split} \nNykyinen sijaintisi: [{self.location.name}] \nNykyinen tehtäväsi:  [Kokeile toimiiko peli] \n\n1 = Siirry toiseen paikkaan \n2 = Tutki aluetta \n3 = Avaa inventaario \n4 = Sulje peli")
        choice = input("\nValitse toiminto: ")
        if choice == "1":
            player.move(self.location)
        elif choice == "2":
            print("Tutkitaan aluetta...")
            time.sleep(random.randrange(1,3))
            self.search(self.location)
        elif choice == "3":
            print("Avataan inventaario...")
            time.sleep(1)
            self.inv_show()
        elif choice == "4":
            confirm = input(f"{split} \nSuljetaako peli? \n\n[enter] = peruuta \n Sulje  = vahvista \n\nValitse toiminto: ")
            if confirm.lower() == "sulje":
                exit()
        else:
            input(f"{split} \nKyseistä toimintoa ei löydy. Valitse toiminto \nkirjoittamalla sitä vastaava numero. ")


# Luodaan esineet, huoneet ja pelaaja

kartta = item("Kartta", "Löysit kartan. Tästä voi olla paljon hyötyä.", None)
kirjat = item("Kirjoi", "Aa kirjoi, otan mukaan korkeintaan polttoaineeksi.")
romu = item
lappu = item
kärryt = item
materiaalit = item
työkalut = item

koti = location("Koti", "Kotisi on täynnä sälää ja kaikkea muuta kivaa. Tahtoisit mennä \ntakaisin nukkumaan mutta sinulla riittää vielä tekemistä.", kartta, kirjat)
keskusta = location("Keskusta", "Kaupunki on täynnä vilinää ja sen sellaista. Näet kaverisi Juhan \nja näytät hänelle keskaria. Hän heittää sinua kirjoilla.", kirjat, romu)
kauppa = location
metsä = location
raunio = location
aukio = location
varasto = location

keskusta.access_to = [koti]
koti.access_to = [keskusta]


#player = user(game.name, game.age, start)
player = user("Pena peluri", 16, keskusta) #Testivaiheessa luodaan pelaaja ilman nimen tai iän kysymistä testailun nopeuttamiseksi

while kirjat.is_used == False:
    player.menu()
print("Läpäisit pelin!! ")
