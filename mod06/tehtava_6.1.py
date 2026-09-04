import random

määrä = int(input("Anna noppien lukumäärä: "))
summa = 0

for i in range(määrä):
    luku = random.randint(1,6)
    summa += luku

print("Silmälukujen summa on",summa)