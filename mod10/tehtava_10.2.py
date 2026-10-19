class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen = alin

    def kerros_ylös(self):
        if self.nykyinen < self.ylin:
            self.nykyinen += 1
            print(f"Hissi on kerroksessa: {self.nykyinen}")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.nykyinen > self.alin:
            self.nykyinen -= 1
            print(f"Hissi on kerroksessa: {self.nykyinen}")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.alin or kohde_kerros > self.ylin:
            print(f"Virhe: Kerrosta {kohde_kerros} ei ole olemassa.")
            return
        
        while self.nykyinen < kohde_kerros:
            self.kerros_ylös()
        while self.nykyinen > kohde_kerros:
            self.kerros_alas()

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.hissit = []
        
        for i in range(hissien_lkm):
            uusi_hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(uusi_hissi)

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        if hissin_numero < 1 or hissin_numero > len(self.hissit):
            print(f"Virhe: Tässä talossa ei ole hissiä numero {hissin_numero}.")
            return
            
        print(f"\nAjetaan hissiä numero {hissin_numero} kerrokseen {kohde_kerros}")
        valittu_hissi = self.hissit[hissin_numero - 1]
        valittu_hissi.siirry_kerrokseen(kohde_kerros)


talo = Talo(1, 7, 3)
print(f"Talo luotu. Kerrokset {talo.alin}-{talo.ylin}, hissejä {len(talo.hissit)} kpl.")
talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 3)
talo.aja_hissiä(1, 1)