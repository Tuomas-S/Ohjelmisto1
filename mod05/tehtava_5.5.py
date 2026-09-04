tunnus = "python"
salasana = "rules"

tunnus_user = input("Anna käyttäjätunnus: ")
salasana_user = input("Anna salasana: ")
yritykset = 1

while tunnus_user != tunnus and salasana_user != salasana and yritykset < 5:
    print("\nKäyttäjätunnus tai salasana on väärin.\nYrityksiä jäljellä:", 5 - yritykset)
    yritykset = yritykset + 1
    tunnus_user = input("\nAnna käyttäjätunnus: ")
    salasana_user = input("Anna salasana: ")

if yritykset == 5:
    print("\nPääsy evätty.")
else:
    print("\nTervetuloa!")