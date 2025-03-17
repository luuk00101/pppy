def nacitaj_data(subor):
    import json

    with open(subor) as subor:
        data = json.loads(subor.read())

    return data


def filtruj(data, popis="", ulica="", cislo=""):
    cache = data.copy()
    nove_data = []

    for budova in cache:
        if (
            popis.lower() not in budova["Popis"].lower()
            or ulica.lower() not in budova["Ulica"].lower()
            or cislo not in budova["Orient._č."]
        ):
            continue

        nove_data.append(budova)

    return nove_data


def pocet(data, popis, ulica, cislo):
    nove_data = filtruj(data, popis, ulica, cislo)

    return len(nove_data)


def usporiadaj_podla_ulica_cislo(data):
    data.sort(key=lambda budova: (budova["Ulica"], budova["Súp._č."]))


def uloz_data_csv(data, subor):
    import csv

    f = open(subor, "w")

    csv_writer = csv.writer(f)

    hlavicka = data[0].keys()
    csv_writer.writerow(hlavicka)

    for budova in data:
        udaje = budova.values()

        riadok = ""

        for udaj in udaje:
            if "," in udaj:
                riadok += '"' + udaj + '"'
            else:
                riadok += udaj

        csv_writer.writerow(udaje)

    f.close()
