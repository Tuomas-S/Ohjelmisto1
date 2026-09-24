from classes import *

def tutorial(player):
    while kartta not in player.inventory:
        player.menu("Pakkaa tavarasi mukaan")
    keskusta.isLocked = metsä.isLocked = False
    return("Tutoriaali valmis")

def building_spot(player):
    while rakennuslupa.usedIn != None:
        player.menu("Valitse rakennuspaikka")
        if rakennuslupa.usedIn == [keskusta]:
            return("Kaupunki valittu")
        if rakennuslupa.usedIn == [niitty]:
            return("Niitty valittu")


