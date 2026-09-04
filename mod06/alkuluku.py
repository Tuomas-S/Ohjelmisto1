luku = int(input("Etsi alkuluvut väliltä 1-"))
alkuluvut = []
jako = 2
alkuluku = True

for kokeiltava in range (1, luku+1):
    while jako <= kokeiltava:
        if kokeiltava % jako == 0 and jako != kokeiltava:
            alkuluku = False
            jako += 1
        else:
            jako += 1
    if alkuluku == True:
        alkuluvut.append(kokeiltava)
        jako = 2
    else:
        alkuluku = True
        jako = 2

print(alkuluvut)