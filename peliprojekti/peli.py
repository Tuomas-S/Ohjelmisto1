import profiili

profiili.nimi = profiili.nimi_lisää()
profiili.ikä = profiili.ikä_lisää()

valinta = True
while valinta != "lopeta":
    print("\n\n(1) Lisää esine reppuun.\n(2) Avaa reppu.\n(3) Muuta nimeä.\n")
    valinta = input("Valitse toiminto: ")
    if valinta == "1":
        profiili.inv_lisää()
    elif valinta == "2":
        profiili.inv_näytä()
    elif valinta == "3":
        profiili.nimi_muuta(profiili.nimi)