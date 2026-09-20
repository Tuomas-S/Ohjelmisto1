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
    def __init__(self, name, search_text, item = None, accepts_item = None, access_to = []):
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

    def move(self, location):
        input(f"{split} \nSiirryit paikkaan {location.name}. ")
        self.location = location

    def search(self):
        if self.location.item != None:
            if self.location.item.is_heavy == True and self.can_carry == False:
                print(f"{split} \n{self.location.search_text}")
                input("\nTäältähän löytyy paljon romua. \nOn kyl vähän liian raskasta kannettavaks. ")
            else:
                print(f"{split} \n{self.location.search_text}")
                input(f"\n{self.location.item.found_text} ")
                self.inventory.append(self.location.item)
                self.location.item = None
        else:
            print(f"{split} \n{self.location.search_text}")
            input("\nEt löytänyt alueelta mitään merkittävää. ")
            
    def inv_show(self):
        if self.inventory == []:
            input(f"{split} \nInventaariosi on tyhjä. Täältä näet löytämäsi esineet. ")
        else:
            print(f"{split} \nInventaariossasi on:")
            for item in self.inventory:
                print(f"- {item.name}")
            input("\n[enter] = Takaisin ")

    def item_use(self):
        if self.inventory == []:
            input(f"{split} \nEt voi käyttää toimintoa juuri nyt, sillä inventaariosi on tyhjä. ")
        else:
            choice = input("Kirjoita esineen nimi: ")
            if choice.lower() == "kartta":
                print(f"{split} \nAvataan kartta...")
                time.sleep(random.randrange(1, 3))
                input("\n   ╭── [ Keskusta ] ──┬── [ Koti ] \n   │        │         │       │ \n[ Kuja ]    │         ╰── [ Metsä ] ───╮ \n   │        │                 │        │ \n   │    [ Kauppa ]            │    [ Raunio ] \n   │                          │        │ \n   ╰─ [ ??? ]             [ Aukio ] ───╯ \n\n[enter] = Takaisin")
            else:
                for item in self.inventory:
                    if choice.lower() == item.name.lower():
                        if item == self.location.accepts_item:
                            print("\nKäytetään esinettä...")
                            time.sleep(random.randrange(1, 3))
                            item.is_used = True
                            self.inventory.remove(item)
                        else:
                            input("\nEt voi käyttää esinettä juuri nyt. ")
                        break
                else:
                    input("\nEsinettä ei löytynyt inventaariostasi. ")

    def menu(self):
        print(f"{split} \nNykyinen sijaintisi: [{self.location.name}] \nNykyinen tehtäväsi:  [Kokeile toimiiko peli] \n\n1 = Siirry toiseen paikkaan \n2 = Tutki aluetta \n3 = Avaa inventaario \n4 = Käytä esine \n5 = Sulje peli")
        choice = input("\nValitse toiminto: ")
        if choice == "1": #seuraava on väliaikainen ja estää softlockin
            if self.location == keskusta:
                self.move(koti)
            elif self.location == koti:
                self.move(keskusta)
        elif choice == "2":
            print("Tutkitaan aluetta...")
            time.sleep(random.randrange(2,4))
            self.search()
        elif choice == "3":
            print("Avataan inventaariota...")
            time.sleep(1)
            self.inv_show()
        elif choice == "4":
            self.item_use()
        elif choice == "5":
            confirm = input(f"{split} \nSuljetaako peli? \n\n[enter] = peruuta \n Sulje  = vahvista \n\nValitse toiminto: ")
            if confirm.lower() == "sulje":
                exit()
        else:
            input(f"{split} \nKyseistä toimintoa ei löydy. Valitse toiminto \nkirjoittamalla sitä vastaava numero. ")


# Luodaan esineet, huoneet ja pelaaja

kartta = item("Kartta", "Löysit kartan. Tästä voi olla paljon hyötyä.")
kirjat = item("Kirjoi", "Aa kirjoi, otan mukaan korkeintaan polttoaineeksi.")
romu = item("Romua", "Hohhoijaa että on paljon romua... Ehkä voisin ottaa vähän sitä mukaan.", True)
lappu = item
kärryt = item
materiaalit = item
työkalut = item

koti = location("Koti", "Kotisi on täynnä sälää ja kaikkea muuta kivaa. Tahtoisit mennä \ntakaisin nukkumaan mutta sinulla riittää vielä tekemistä.", kartta, kirjat)
keskusta = location("Keskusta", "Kaupunki on täynnä vilinää ja sen sellasita. Näet kaverisi Juhan \nja näytät hänelle keskaria. Hän heittää sinua kirjoilla.", kirjat, romu)
kauppa = location
metsä = location
raunio = location
aukio = location
varasto = location

#player = user(game.name, game.age, start)
player = user("Pena peluri", 16, keskusta) #Testivaiheessa luodaan pelaaja ilman nimen tai iän kysymistä testailun nopeuttamiseksi

while kirjat.is_used == False:
    player.menu()
print("Läpäisit pelin!! ")
