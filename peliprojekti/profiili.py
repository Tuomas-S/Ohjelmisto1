import time

# Inventaario
inventaario = []

def inv_lisää():
    inventaario.append(input("\nAnna esineelle nimi: "))
    return inventaario

def inv_näytä():
    if inventaario == []:
        print("\nReppusi on tyhjä")
    else:
        print("\nRepussasi on\n")
        for i in inventaario:
            print(f"- {i}")


# Profiili
nimi = True
def nimi_lisää():
    nimi = input("Nimi: ")
    return nimi

ikä = True
def ikä_lisää():
    ikä = input("Ikä: ")
    while True:
        try:
            int(ikä)
        except ValueError:
            ikä = input("\nAnna oikea ikä:\n")
        else:
            break
    ikä = int(ikä)
    if ikä < 12:
        print("\nOlet alaikäinen, suljetaan sovellus...")
        time.sleep(3)
        exit()
    else:
        print(f"\nTervetuloa, {nimi}!")
    return ikä

def nimi_muuta(nimi_new):
    print(f"\nNykyinen nimesi: {nimi_new}")
    nimi_new = input("Anna uusi nimi: ")
    return nimi_new