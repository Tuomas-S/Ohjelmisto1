def pariton(lista):
    lista = [i for i in lista if i % 2 == 0]
    return lista

mones = 1
luvut = []
luku = input(f"Anna {mones}. kokonaisluku: ")

while luku != "":
    luku = int(luku)
    luvut.append(luku)
    mones += 1
    luku = input(f"Anna {mones}. kokonaisluku: ")

print(f"Parillisia lukuja näistä ovat {pariton(luvut)}")