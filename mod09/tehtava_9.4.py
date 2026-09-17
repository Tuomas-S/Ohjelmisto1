import random

class Auto:
    def __init__(self, rekisteri, huippunopeus, nopeus = 0, matka = 0):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihdyta(self, kiihdytys):
        if self.nopeus + kiihdytys >= self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus + kiihdytys <= 0:
            self.nopeus = 0
        else:
            self.nopeus += kiihdytys

    def kulje(self, tunnit = 1):
        self.matka += self.nopeus * tunnit

autot = []

for i in range(1,11):
    i = Auto(f"ABC-{i}", random.randint(100, 200))
    autot.append(i)

voitto = False
while True:
    for i in autot:
        i.kiihdyta(random.randint(-10, 15))
        i.kulje()
        if i.matka >= 10000:
            voitto = True
        print(f"{i.rekisteri} on kulkenut {i.matka}km")
    if voitto:
        break


autot.sort(key = lambda i: i.matka, reverse = True)
# lambda luo väliaikaisen muuttujan (i), ja toimii samalla tavalla kuin for toistorakenne
# lambda on funktio joka palauttaa arvonaan autojen matkan ja key antaa säännön miten lista järjestetään

print(f"\n{"Sijoitus":^12s}{"Rekisterinumero":^19s}{"Huippunopeus":^16s}{"Kuljettu matka":^18s}")
for i in autot:
    print(f"{str(autot.index(i) + 1) + ".":^12s}{i.rekisteri:^19s}{str(i.huippunopeus) + "km/h":^16s}{str(i.matka) + "km":^18s}")
print("")