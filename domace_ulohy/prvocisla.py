# overime, ci je cislo prvocislo
def jePrvocislo(n):
    # zacneme od 2, protoze 1 nie je prvocislo
    cislo = 2

    # ak je n delitelne nejakym cislom, tak to nie je prvocislo
    while cislo * cislo <= n:
        if n % cislo == 0:
            return False
        cislo += 1

    return True


# generujeme prvocisla
def gen_prvocisla(n):
    if n < 2:
        return

    # 2 je prvocislo, takze ho vratime
    yield 2

    # zacneme od 3 a budeme skakat po 2, pretoze parne cisla nie su prvocisla
    for cislo in range(3, n + 1, 2):
        if jePrvocislo(cislo):
            yield cislo


# vypiseme prvocisla
for cislo in gen_prvocisla(10):
    print(cislo)
