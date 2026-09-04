luku = float(input("Anna luku: "))
suurin = luku
pienin = luku

while luku != "":
    luku = float(luku)
    if luku > suurin:
        suurin = luku
    if luku < pienin:
        pienin = luku
    luku = input("Anna luku: ")

print("\nPienin luku on " + str(pienin) + "\nSuurin luku on " + str(suurin))
    