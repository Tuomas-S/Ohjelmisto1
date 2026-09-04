luvut = []
luku = float(input("Anna luku: "))

while luku != "":
    luku = float(luku)
    luvut.append(luku)
    luku = input("Anna luku: ")

luvut.sort(reverse=True)
print("\nViisi suurinta lukua järjestyksessä ovat:\n" + str(luvut[0:5]))