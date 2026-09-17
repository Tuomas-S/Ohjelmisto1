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

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit


auto1 = Auto("ABC-123", 142, 0, 80)

print(f"\nAuton rekisterinumero on {auto1.rekisteri}, huippunopeus on {auto1.huippunopeus}km/h, nykyinen nopeus on {auto1.nopeus}km/h ja kuljettu matka on {auto1.matka}km")  

print("\nKiihdytetään...")
auto1.kiihdyta(30)

print(f"Nopeutesi on nyt {auto1.nopeus}km/h. Kuljetaan 2 tunnin ajan...")
auto1.kulje(2)

print(f"\nOlet nyt kulkenut {auto1.matka} kilometria.")