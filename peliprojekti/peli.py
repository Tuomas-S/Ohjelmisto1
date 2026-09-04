import random
import sys

nimi = input("Nimi: ")
ikä = input("Ikä: ")

# Kokeilee onko ikä kokonaisluku
while True:
    try:
        int(ikä)
    except ValueError:
        ikä = input("\nAnna oikea ikä:\n")
    else:
        break

ikä = int(ikä)
if ikä < 12:
    print("Olet alaikäinen, suljetaan sovellus.")
    sys.exit()
else:
    print("\nTervetuloa, " + nimi + "!")

valinta = 0
while valinta != "lopeta":
    valinta = input('\nKirjoita "lopeta" poistuaksesi.\n1 Kerro vitsi.\n2 Anna satunnaisluku [1, 10].\n3 Muuta nimeä.\n\n')
    if valinta == "1":
        print("\nEn jaksa.")
    elif valinta == "2":
        print("\nSatunnaislukusi on " + str(random.randint(1,10)))
    elif valinta == "3":
        nimi = input("\nAnna uusi nimi: ")
        print("\nUusi nimesi on " + nimi + "!")
