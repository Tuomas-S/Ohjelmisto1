import random
import time

def noppa():
    print("Nopan tahko: 6")
    print("Heitetään noppaa...")
    time.sleep(1.5)
    tulos = random.randint(1,6)
    while tulos != 6:
        print(tulos)
        tulos = random.randint(1,6)
        time.sleep(0.05)
    print(tulos)

noppa()