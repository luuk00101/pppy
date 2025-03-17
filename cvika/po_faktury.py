import json
def uprav_cenu(cena_str):
    cena_cislo = cena_str.replace(' ', '')
    cena_cislo = cena_cislo.replace(',', '.')
    cena_cislo = float(cena_cislo)
    return cena_cislo
def citaj_data(subor):
    with open(subor, 'rt', encoding='utf-8') as f:
        data = json.load(f)
    for zaznam in data:
        zaznam['Celková_cena'] = uprav_cenu(zaznam['Celková_cena'])
    return data


def spracuj_data(data):
    nove_data = {}
    for faktura in data:
        dodavatel = faktura['Dodávateľ']
        suma = faktura['Celková_cena']
        rok = faktura['Dátum_zverejnenia'][-4:]
        zaplatene = faktura['Stav_zaplatenia']
        if dodavatel not in nove_data:
            nove_data[faktura['Dodávateľ']]

def uloz_data(data, subor):
    pass

data = citaj_data('Zoznam_Dodávateľské_faktúry.json')
# for zaznam in data:
#     print(zaznam['Celková_cena'])
# print(data)

nove_data = spracuj_data(data)