kaupungit = []
a = 3

for i in range(1, 6):
    nimi = input("Anna " + str(i) + ". kaupungin nimi: ")
    kaupungit.append(nimi)

print("")

for i in range(5):
    print(kaupungit[i])