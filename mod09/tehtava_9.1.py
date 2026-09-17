class Auto:
    def __init__(self, rekisteri, huippunopeus, nopeus = 0, matka = 0):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

auto1 = Auto("ABC-123", 142)

print(f"Auton rekisterinumero on {auto1.rekisteri}, huippunopeus on {auto1.huippunopeus}km/h, nykyinen nopeus on {auto1.nopeus}km/h ja kuljettu matka on {auto1.matka}km")