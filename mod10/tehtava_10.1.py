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
        print(f"\nSiirrytään kerrokseen {kohde_kerros}")
        while self.nykyinen < kohde_kerros:
            self.kerros_ylös()
        while self.nykyinen > kohde_kerros:
            self.kerros_alas()

h = Hissi(1, 10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)