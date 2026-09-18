import time
import random
#import game
import description

class item:
    def __init__(self, name, desc, used, used_in, is_heavy = True):
        self.name = name # esineen nimi
        self.desc = desc # esineen kuvaus (voi sisältää esim koodin)
        self.used = used # tuloste käytön jälkeen
        self.used_in = used_in # missä käytetään
        self.is_heavy = is_heavy # voiko esineen ottaa vain apuvälineen kanssa
        
class room:
    def __init__(self, name, enter, item = None):
        self.name = name # huoneen nimi
        self.enter = enter # Tämä tulostuu kun siirryt huoneeseen
        self.item = item # huoneessa sijaitseva esine

class user:
    def __init__(self, name, age, room, inventory = [], can_carry = False):
        self.name = name # pelaajan asettama nimi
        self.age = age # pelaajan asettama ikä
        self.inventory = inventory # inventaario (lista)
        self.room = room # nykyinen huone
        self.can_carry = can_carry # voiko lisätä painavia esineitä inventaarioon (True/False)

    def name_change(self, name_current):
        print(f"\nNykyinen nimesi: {name_current}")
        self.name = input("Anna uusi nimi: ")

    def move(self, room):
        choice = input(f"Siirrytäänkö huoneeseen {room.name}? (kyllä/ei)\n")
        while True:
            if choice == "kyllä" or choice == "Kyllä":
                self.room = room
                print(room.enter)
                break
            elif choice == "ei" or choice == "Ei":
                print("Palataan takaisin.")
                break
            else:
                choice = input("Vastaa kyllä/ei: ")

    def search(self, room):
        print("Tutkitaan aluetta...")
        time.sleep(random.randint(2,5))
        if room.item != None:
            if room.item.is_heavy == True and player.can_carry == False:
                print(f"Löysit esineen [{room.item.name}], mutta se on liian raskas kannettavaksi. Tarvitset kottikärryt.")
            else:
                print(f"Löysit esineen [{room.item.name}], lisätään se inventaarioosi")
                player.inventory.append(room.item)
                player.room.item = None
        else:
            print("Et löytänyt huoneesta mitään.")


    def inv_show(self):
        if self.inventory == []:
            print("\nReppusi on tyhjä. Täältä näet löytämäsi esineet.")
        else:
            print("\nRepussasi on\n")
            for item in self.inventory:
                print(f"- {item.name}")

    def item_use(self, item):
        if item.used_in == player.room:
            print(item.used)
            player.inventory.remove(item)
        else:
            print("Hmm... Et voi käyttää esinettä juuri nyt.")

# Luodaan esineet, huoneet ja pelaaja

lappu = item
kärryt = item
resurssit = item
työkalut = item
kirjat = item
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

print("\nTutkit huonetta ilman kottikärryjä:")
player.search(start)

player.can_carry = True
print("\nTutkit huonetta ja sinulla on kottikärryt:")
player.search(start)

print("\nTutkit huonetta lisää")
player.search(start)

print("\nKoitat käyttää romua (Romua ei voi käyttää huoneessa start)")
player.item_use(romu)
player.inv_show()

player.room = keskusta
print(f"\nNykyinen huoneesi on {player.room.name}, koitat käyttää romua uudestaan")
player.item_use(romu)
player.inv_show()

