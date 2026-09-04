nimi = input("Nimi:\n")
ikä = input("\nIkä:\n")

# Kokeilee onko ikä kokonaisluku
while True:
    try:
        int(ikä)
    except ValueError:
        ikä = input("\nAnna oikea ikä:\n")
    else:
        break

ikä = int(ikä)