lk1 = float(input("Kirjoita luku (1/3): "))
lk2 = float(input("Kirjoita luku (2/3): "))
lk3 = float(input("Kirjoita luku (3/3): "))

summa = lk1 + lk2 + lk3
tulo = lk1 * lk2 * lk3
keskiarvo = summa / 3

print("_  _  _  _  _  _  _  _\n")
print("Lukujen summa on" , round(summa, 5))
print("Lukujen tulo on" , round(tulo, 5))
print("Lukujen keskiarvo on" , round(keskiarvo, 5))