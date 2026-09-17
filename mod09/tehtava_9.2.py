class Auto:
    def __init__(self, rekisteri, huippunopeus, nopeus = 0, matka = 0):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihdyta(self, kiihdytys):
        self.nopeus += kiihdytys
        if self.nopeus + kiihdytys >= self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus + kiihdytys <= 0:
            self.nopeus = 0


auto1 = Auto("ABC-123", 142)

print(f"\nAuton rekisterinumero on {auto1.rekisteri}, huippunopeus on {auto1.huippunopeus}km/h, nykyinen nopeus on {auto1.nopeus}km/h ja kuljettu matka on {auto1.matka}km")  

print("\nKiihdytetään...")
auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

print(f"\nAuton nopeus on nyt {auto1.nopeus}km/h. Suoritetaan hätäjarrutus...")
auto1.kiihdyta(-200)

print(f"\nNopeus on nyt {auto1.nopeus}km/h.")