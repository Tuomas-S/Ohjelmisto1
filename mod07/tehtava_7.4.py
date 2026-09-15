def summa(lista):
    yhteenlasku = sum(lista)
    return yhteenlasku

mones = 1
luvut = []
luku = input(f"Anna {mones}. kokonaisluku: ")

while luku != "":
    luku = int(luku)
    luvut.append(luku)
    mones += 1
    luku = input(f"Anna {mones}. kokonaisluku: ")

print(f"\nAntamiesi lukujen summa on {summa(luvut)}")