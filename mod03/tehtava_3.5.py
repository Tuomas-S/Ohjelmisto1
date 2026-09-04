leiviskät = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

naulat = naulat + leiviskät * 20
luodit = luodit + naulat * 32
gramma = luodit * 13.3 % 1000
kilogramma = (luodit * 13.3) // 1000

print("_  _  _  _  _  _  _  _\n")
print("Massa nykymittojen mukaan:")
print(str(round(kilogramma)) + "kg ja " + str(round(gramma, 2)) + "g")