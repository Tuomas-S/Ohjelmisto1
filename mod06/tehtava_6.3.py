luku = int(input("Anna kokonaisluku: "))
alkuluku = True

for i in range (3, luku, 2):
    if luku % i == 0:
        alkuluku = False
        break

if alkuluku == False:
    print("Luku ei ole alkuluku.")
if alkuluku == True:
    print("Luku on alkuluku.")