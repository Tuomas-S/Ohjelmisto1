pituus = float(input("Anna kuhan pituus (cm): "))
puute = 37 - pituus
if pituus < 37:
    print("Laske kuha takaisin järveen. Kuhan pituus on " + str(puute) + "cm sallittua pyyntimittaa (37cm) lyhyempi.")
else:
    print("On se iso!")