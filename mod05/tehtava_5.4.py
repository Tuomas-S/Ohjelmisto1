import random
luku = random.randint(1, 10)
arvaus = int(input("Arvaa luku väliltä 1 ja 10: "))

while arvaus != luku:
    if arvaus < luku:
        arvaus = int(input("Liian pieni luku! Arvaa uudestaan: "))
    if arvaus > luku:
        arvaus = int(input("Liian suuri luku! Arvaa uudestaan: "))

print("Oikein!")