alue = int(input("Etsi alkuluvut väliltä 1-"))

alkuluvut = []
jako = 3 # ohjelma ei tarkasta yhden tai kahden jaollisuutta optimisoinnin vuoksi
on_alkuluku = True # ohjelma olettaa alussa kaikkien lukujen olevan alkulukuja

# lisätään alkuluku 2, jos tarvetta
if alue >= 2:
    alkuluvut.append(2)
else:
    print("Ei alkulukuja.")
    exit()

# ohjelma pyrkii todistamaan, ettei luku ole alkuluku jakamalla luvun sitä pienemmillä kokonaisluvuilla
# niin kauan, kunnes luku on jaollinen, tai ohjelma jakaa luvun itsellään
for luku in range (3, alue + 1, 2):
    while jako <= luku:
        if luku % jako == 0 and jako != luku:
            on_alkuluku = False
            break
        else:
            jako += 1

# jos ohjelma ei todistanut luvun olevan alkuluku, luku lisätään listaan
    if on_alkuluku == True:
        alkuluvut.append(luku)
        jako = 3

# jos ohjelma toteaa ettei luku ole alkuluku, palataan takaisin alkuasetuksiin ja kokeillaan seuraavaa lukua
    else:
        on_alkuluku = True
        jako = 3

# kun toistorakenne päättyy, tulostetaan kaikki alkuluvut
print(alkuluvut)