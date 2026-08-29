vuosi = int(input("Anna vuosiluku.\n"))

if vuosi % 4 == 0:
    if vuosi % 100 == 0 and not vuosi % 400 == 0:
        print("\nVuosi ei ole karkausvuosi.")
    else:
        print("\nVuosi on karkausvuosi.")
else:
    print("\nVuosi ei ole karkausvuosi.")