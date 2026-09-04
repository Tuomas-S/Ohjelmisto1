tuuma = 0
cm = 0

while tuuma >= 0:
    tuuma = float(input("Anna tuumat: "))
    if tuuma <0:
        break
    else:
        cm = tuuma * 2.54
        print ("\n" + str(tuuma) + " tuumaa on " + str(cm) + " senttimetriä.\n")
print("\nToiminnot lopetettu.")