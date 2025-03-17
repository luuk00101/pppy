def zisti_pocet_vozidiel(pocet_osob):
    pass


def vypocitaj_cenu(pocet_osob, km):
    rozlozenieVozidiel = zisti_pocet_vozidiel(pocet_osob)

    celkova_cena = (
        rozlozenieVozidiel["Auto"] * km * 0.4
        + rozlozenieVozidiel["autobus"] * km * 0.87
    )

    return celkova_cena
