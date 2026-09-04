import random
import math
koordinaatti_x = 0
koordinaatti_y = 0
luku = 0 
n = 0   #ympyrän sisällä olevien pisteiden lukumäärä
m = 10000000   #pisteiden kokonaismäärä


while luku < m:
    koordinaatti_x = random.uniform(-1, 1)
    koordinaatti_y = random.uniform(-1, 1)
    if koordinaatti_x ** 2 + koordinaatti_y ** 2 < 1:
        n = n + 1
    luku = luku + 1

pi = 4 * n / m
print("\nPiin likiarvo on " + [pi])
print("\nPiin oikea arvo on", math.pi, "\n")