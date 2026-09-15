import math

def suhde(halkaisija_cm, hinta):
    ala_m = math.pi * (halkaisija_cm / 200) ** 2
    suhde = hinta / ala_m
    return suhde

p1_halkaisija = int(input("Anna 1. pizzan halkaisija senttimetreinä: "))
p1_hinta = int(input("Anna 1. pizzan hinta euroina: "))
p1_suhde = suhde(p1_halkaisija, p1_hinta)

p2_halkaisija = int(input("Anna 2. pizzan halkaisija senttimetreinä: "))
p2_hinta = int(input("Anna 2. pizzan hinta euroina: "))
p2_suhde = suhde(p2_halkaisija, p2_hinta)

print(f"\nPizza 1 maksaa {p1_suhde:.2f}€/m².")
print(f"Pizza 2 maksaa {p2_suhde:.2f}€/m².")
if p1_suhde < p2_suhde:
    print("Täten pizza 1 antaa paremman vastineen rahalle.")
elif p1_suhde > p2_suhde:
    print("Täten pizza 2 antaa paremman vastineen rahalle.")
else:
    print("Pizzat maksavat saman verran kokoonsa nähden.")