sukupuoli = input("Oletko mies (M) vai nainen (N)?\n")

if sukupuoli != "M" or sukupuoli != "N":
    sukupuoli = input("\nKirjoita joko M tai N.\n")

hemoglobiini = float(input("\nMikä on hemoglobiiniarvosi (g/l)?\n"))

if sukupuoli == "M":
    if hemoglobiini < 134:
        print("\nHemoglobiiniarvosi on alhainen")
    elif 134 <= hemoglobiini <= 195:
        print("\nHemoglobiiniarvosi on normaali")
    elif hemoglobiini > 195:
        print("\nHemoglobiiniarvosi on korkea")

if sukupuoli == "N":
    if hemoglobiini < 117:
        print("\nHemoglobiiniarvosi on alhainen")
    elif 117 <= hemoglobiini <= 175:
        print("\nHemoglobiiniarvosi on normaali")
    elif hemoglobiini > 175:
        print("\nHemoglobiiniarvosi on korkea")