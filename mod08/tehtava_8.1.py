vuodenajat = ("talvi", "talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy")

kuukausi = int(input("Anna kuukauden numero: "))
if 1 <= kuukausi <= 12:
    print(f"\nKuukautta vastaava vuodenaika on {vuodenajat[kuukausi - 1]}.")
else:
    print("Kuukautta ei löytynyt")