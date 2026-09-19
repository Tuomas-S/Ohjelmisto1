import time
import random
#import game
import description
split = "_  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _\n"

class item:
    def __init__(self, name, desc, used, used_in = None, is_heavy = False):
        self.name = name # esineen nimi
        self.desc = desc # esineen kuvaus
        self.used = used # tuloste käytön jälkeen
        self.used_in = used_in # missä käytetään
        self.is_heavy = is_heavy # voiko esineen ottaa vain apuvälineen kanssa
        
class room:
    def __init__(self, name, enter, access_to = [], item = None):
        self.name = name # huoneen nimi
        self.enter = enter # Tämä tulostuu kun siirryt huoneeseen
        self.access_to = access_to # lista paikoista mihin tästä huoneesta pääsee
        self.item = item # sijainnissa oleva esine

class user:
    def __init__(self, name, age, location, inventory = [], can_carry = False):
        self.name = name # pelaajan asettama nimi
        self.age = age # pelaajan asettama ikä
        self.inventory = inventory # inventaario (lista)
        self.location = location # nykyinen sijainti
        self.can_carry = can_carry # voiko lisätä painavia esineitä inventaarioon (True/False)

    def name_change(self, name_current):
        print(f"\nNykyinen nimesi: {name_current}")
        self.name = input("Anna uusi nimi: ")

    def move(self, location):
        print(f"Siirrytään huoneeseen [{location.name}].")
        self.location = location

    def search(self, location):
        print("Tutkitaan aluetta...")
        time.sleep(random.randint(1,3))
        if location.item != None:
            if location.item.is_heavy == True and self.can_carry == False:
                print(f"Löysit esineen [{location.item.name}], mutta se on liian raskas kannettavaksi. Tarvitset kottikärryt.")
            else:
                print(f"Löysit esineen [{location.item.name}], lisätään se inventaarioosi")
                self.inventory.append(location.item)
                self.location.item = None
        else:
            print("Et löytänyt huoneesta mitään.")

    def inv_show(self):
        if self.inventory == []:
            print(f"{split} \nReppusi on tyhjä. Täältä näet löytämäsi esineet.")
        else:
            print(f"{split} \nRepussasi on:")
            for item in self.inventory:
                print(f"- {item.name}")
            choice = input("\n[enter] = takaisin \nKirjoita esineen nimi tutkiaksesi sitä: ")
            while choice != "":
                for item in self.inventory:
                    if item.name.lower() == choice.lower():
                        print("Tutkitaan esinettä...")
                        time.sleep(random.randint(1, 3))
                        print(f"\n{item.desc}")
                        input("Paina [enter] jatkaaksesi. ")
                        break
                else:
                    input(f"{split} \nEsinettä ei löytynyt. \nPaina [enter] jatkaakesesi. ")
                print(f"{split} \nRepussasi on:")
                for item in self.inventory:
                    print(f"- {item.name}")
                choice = input("\n[enter] = takaisin \nKirjoita esineen nimi tutkiaksesi sitä: ")

    def item_use(self, item):
        if item.used_in == self.location:
            print(item.used)
            self.inventory.remove(item)
        else:
            print("Hmm... Et voi käyttää esinettä juuri nyt.")

# Luodaan esineet, huoneet ja pelaaja

lappu = item
kärryt = item
materiaalit = item
työkalut = item
kirjat = item("Kirjoi", "Jotain paskaa luettavaa vaan", "Käytit kirjoja")
keskusta = room("Keskusta", "Saavut keskustaan")
romu = item("Romu", "Sälää", "Käytit romun", keskusta)

start = room("Start", "Start_enter", romu)
kauppa = room
metsä = room
työmaa = room
reuna = room
kirjavarasto = room

#player = user(game.name, game.age, start)
player = user("Pena", 16, start)


player.inventory.append(romu)
player.inventory.append(kirjat)
print(player.inventory)
player.inv_show()

