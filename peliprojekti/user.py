import time
import random
import json
from items import *
from locations import *
from text_format import *

class User:
    def __init__(self, name, age, location, status, inventory):
        self.name = name # pelaajan asettama nimi
        self.age = age # pelaajan asettama ikä
        self.location = location # nykyinen sijainti
        self.status = status # pelaajan tämänhetkinen tilanne
        self.inventory = inventory # inventaario

    def to_dictionary(self):
        return {
            "name": self.name,
            "age": self.age,
            "location": self.location.name,
            "status": self.status,
            "inventory": [item.name for item in self.inventory] if self.inventory else []
        }


    # Pelin tallennus
    def save_game(self):
        data = {
            "items": [item.to_dictionary() for item in allItems],
            "locations": [location.to_dictionary() for location in allLocations],
            "user": self.to_dictionary()
        }
        with open("peliprojekti/game_data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    # Pelin lataus
    def load_game(self):
        with open("peliprojekti/game_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        itemLookup = {item.name: item for item in allItems}
        locationLookup = {location.name: location for location in allLocations}

        # Ladataan esineet
        for itemData in data["items"]:
            item = itemLookup[itemData["name"]]
            item.name = itemData["name"]
            item.foundText = itemData["foundText"]
            item.usedText = itemData["usedText"]
            if isinstance(item, Functional):
                item.itemNotUsed = itemData["itemNotUsed"]
                item.isSingleUse = itemData["isSingleUse"]
                item.usedIn = [locationLookup[locationName] for locationName in itemData["usedIn"]]

        # Ladataan sijainnit
        for locationData in data["locations"]:
            location = locationLookup[locationData["name"]]
            location.name = locationData["name"]
            location.searchText = locationData["searchText"]
            location.isLocked = locationData["isLocked"]
            location.lockedText = locationData["lockedText"]
            location.isLocked = locationData["isLocked"]
            location.hasItem = [itemLookup[itemName] for itemName in locationData["hasItem"]]
            location.acceptsItem = [itemLookup[itemName] for itemName in locationData["acceptsItem"]]
            location.connections = [locationLookup[locationName] for locationName in locationData["connections"]]

        # Ladataan käyttäjä
        userData = data["user"]
        self.name = userData["name"]
        self.age = userData["age"]
        self.location = locationLookup[userData["location"]]
        self.status = userData["status"]
        self.inventory = [itemLookup[itemName] for itemName in userData["inventory"]]


    # Pelaajan liikkuminen
    def move(self):
        hasMoved = False
        while hasMoved == False:
            clear_shell()
            print("╭─────────────────────────────────────────────╮ \n│ Voit siirtyä seuraaviin paikkoihin:         │")
            for location in self.location.connections:
                print(f"│ » {location.name:<42}│")
            choice = input("╰─────────────────────────────────────────────╯ \n\n  Liiku paikkaan kirjoittamalla sen nimi. \n  [enter] = takaisin \n\n  Valitse toiminto: ")
            if choice == "":
                hasMoved = True

            else:
                for location in self.location.connections:
                    if choice.lower() == location.name.lower():
                        if location.isLocked:
                            code = input(fancyLine + divide(location.lockedText))
                            if self.location == kuja and code == "52971" and varasto.isLocked == True:
                                varasto.isLocked = False
                                kuja.lookupText = "Kujalla on erittäin ahdasta ja likaista. Onneksi et kärsi ahtaan paikan kammosta."
                                input("\n» Lukko aukeaa.")
                            break
                        print("  Siirrytään...")
                        time.sleep(random.randrange(1, 3))
                        self.location = location
                        hasMoved = True
                        break
                else:
                    input(f"{fancyLine}  Sijaintia ei löytynyt.")


    # Nykyisen sijainnin tutkiminen
    def lookup(self):
        input(fancyLine + divide(self.location.lookupText))
        if self.location.hasItem == []:
            input("\n  Et löytänyt alueelta mitään mukaan otettavaa.")
            clear_shell()

        else:
            for item in self.location.hasItem:
                input(f"\n{divide(item.foundText)}")
                self.inventory.append(item)
            self.location.hasItem = []


    # Esineen käyttäminen
    def item_use(self, choice):
        for item in self.inventory:
            if choice.lower() == item.name.lower():
                if isinstance(item, Functional):
                    if item in self.location.acceptsItem:
                        if self.location in item.usedIn:
                            input(f"{fancyLine}  Olet jo käyttänyt esineen tässä paikassa.")
                            return(False)
                        print("  Käytetään esine...")
                        time.sleep(random.randrange(1, 3))
                        input(fancyLine + divide(item.usedText))
                        item.usedIn.append(self.location)
                        if item.isSingleUse:
                            self.inventory.remove(item)
                        return(True)
                    else:
                        input(fancyLine + divide(item.itemNotUsed))
                        return(False)

                else:
                    print("  Käytetään esine...")
                    time.sleep(random.randrange(1, 3))
                    if choice.lower() == "kartta":
                        clear_shell()
                        print(f"\n{kartta.usedText}")
                        print(f"{fancyLine}{divide("Kartta kaikista kaupungin sijainneista. Jotkut sijainnit eivät ole aina saatavilla.")}\n")
                        input(f"» Nykyinen sijaintisi: {self.location.name}")
                        return(False)
                    else:
                        input(fancyLine + divide(item.usedText))
                    return(True)
        else:
            input(f"{fancyLine}  Esinettä ei löytynyt inventaariostasi.")
            return(False)

        
    # Inventaario ja esineen valinta
    def inv_show(self):
        itemWasUsed = False
        while itemWasUsed == False:
            clear_shell()
            if self.inventory == []:
                input("╭───────────────────────────────────────╮ \n│ Inventaariosi on tyhjä.               │ \n│ Täältä näet löytämäsi esineet.        │ \n╰───────────────────────────────────────╯ \n\n  [enter] = takaisin")
                break
            else:
                print("╭─────────────────────────────────────────╮ \n│ Inventaariossasi on:                    │")
                for item in self.inventory:
                    print(f"│ » {item.name:<38}│")
                choice = input("╰─────────────────────────────────────────╯ \n\n  Käytä esine kirjoittamalla sen nimi. \n  [enter] = takaisin \n\n  Valitse toiminto: ")
                if choice == "":
                    clear_shell()
                    break
                else:
                    itemWasUsed = self.item_use(choice)
                    clear_shell()

    
    # Pelin sisäinen valikko
    def menu(self, mission):
        clear_shell()
        print(f"╭─────────────────────────────────────────────────────╮ \n│ [⌂] SIJAINTI: {self.location.name:<38}│ \n│ [≡] TEHTÄVÄ:  {mission:<38}│ \n╰─────────────────────────────────────────────────────╯ \n\n  [1] = Vaihda sijaintia \n  [2] = Tutki aluetta \n  [3] = Avaa inventaario \n  [4] = Takaisin valikkoon")
        choice = input("\n  Valitse toiminto: ")
        if choice == "1":
            self.move()
        elif choice == "2":
            print("  Tutkitaan aluetta...")
            time.sleep(random.randrange(1,3))
            self.lookup()
        elif choice == "3":
            print("  Avataan inventaario...")
            time.sleep(1)
            self.inv_show()
        elif choice == "4":
            clear_shell()
            confirm = input('╭────────────────────────────────────╮ \n│ Tallenna ja sulje peli             │ \n╰────────────────────────────────────╯ \n\n  Kirjoita "ok" vahvistaaksesi. \n  [enter] = peruuta \n\n  Valitse toiminto: ')
            if confirm.lower() == "ok":
                self.save_game()
                exit()
        else:
            input(f"{fancyLine}  Kyseistä toimintoa ei löydy. Valitse toiminto \n  kirjoittamalla sitä vastaava numero.")

# Luodaan pelaaja self, name, age, location, status, inventory
player = User(
    name = "",
    age = "",
    location = koti,
    status = "Pakkaa tavarasi mukaan",
    inventory = []
)