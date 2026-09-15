import random
import time

def noppa(tahko):
    print("Heitetään noppaa...\n")
    time.sleep(1)
    tulos = random.randint(1,tahko)
    while tulos != tahko:
        print(tulos)
        tulos = random.randint(1,tahko)
        time.sleep(0.02)
    print(tulos)

noppa(int(input(("Anna nopan tahko: "))))