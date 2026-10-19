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

class Sähköauto(Auto):
    def __init__(self, rekisteri, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteri, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri, huippunopeus, bensatankin_koko):
        super().__init__(rekisteri, huippunopeus)
        self.bensatankin_koko = bensatankin_koko


sahkoauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdyta(150)
polttomoottoriauto.kiihdyta(120)

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"Sähköauto ({sahkoauto.rekisteri}):")
print(f"  Akkukapasiteetti: {sahkoauto.akkukapasiteetti} kWh")
print(f"  Nopeus: {sahkoauto.nopeus} km/h")
print(f"  Matkamittari: {sahkoauto.matka} km\n")

print(f"Polttomoottoriauto ({polttomoottoriauto.rekisteri}):")
print(f"  Bensatankin koko: {polttomoottoriauto.bensatankin_koko} l")
print(f"  Nopeus: {polttomoottoriauto.nopeus} km/h")
print(f"  Matkamittari: {polttomoottoriauto.matka} km")