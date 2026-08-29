kanta = float(input("Kirjoita suorakulmion kanta: "))
korkeus = float(input("Kirjoita suorakulmion korkeus: "))

piiri = 2 * kanta + 2 * korkeus
ala = kanta * korkeus

print("_  _  _  _  _  _  _  _  _  _  _\n")
print("Suorakulmion piiri on " + str(round(piiri, 4)))
print("Suorakulmion pinta-ala on " + str(round(ala, 5)))