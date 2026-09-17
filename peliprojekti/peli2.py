import profiili

valinnat = [profiili.inv_lisää, profiili.inv_näytä, profiili.nimi_muuta]
valinnat_txt = ["1. Lisää esine inventaarioon", "2. Näytä inventaario", "3. Muuta nimeä"]
parametrit = [[], [], [profiili.nimi]]

valinta = True
while True:
    print()
    for i in valinnat_txt:
        print(i)
    valinta = input(f"\nValitse toiminto (1-{len(valinnat)}): ")
    if valinta == "lopeta":
        exit()
    else:
        try:
            int(valinta)
        except ValueError:
            break
        valinta = int(valinta)
        valinnat[valinta - 1](*parametrit[valinta - 1])
