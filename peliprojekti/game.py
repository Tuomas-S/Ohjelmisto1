import time
import classes

# while True:
#     print("\n1. Lisää esine reppuun.\n2. Avaa reppu.\n3. Muuta nimeä.\n")
#     choice = input("Valitse toiminto (1-3) tai kirjoita exit lopettaaksesi: ")
#     if choice == "1":
#         inv_add()
#     elif choice == "2":
#         inv_show()
#     elif choice == "3":
#         player.name = name_change(player.name)
#     elif choice == "exit":
#         exit()

name = input("Nimi: ")
age = input("Ikä: ")
while True:
    try:
        int(age)
    except ValueError:
        age = input("\nAnna oikea ikä:\n")
    else:
        break
age = int(age)
if age < 12:
    print("\nOlet alaikäinen, suljetaan sovellus...")
    time.sleep(3)
    exit()
else:
    print(f"\nTervetuloa {name}!")

# Tähän intro.txt

input("Aloita peli painamalla enter. ")

# while True:
#     print("\n1. Lisää esine reppuun.\n2. Avaa reppu.\n3. Muuta nimeä.\n")
#     choice = input("Valitse toiminto (1-3) tai kirjoita exit lopettaaksesi: ")
#     if choice == "1":
#         inv_add()
#     elif choice == "2":
#         inv_show()
#     elif choice == "3":
#         player.name = name_change(player.name)
#     elif choice == "exit":
#         exit()