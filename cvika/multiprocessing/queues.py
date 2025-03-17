import multiprocessing
import random
import time


def citaj_data(subor_in, pred, pocitadlo):
    # len simulujeme citanie zo suboru
    pocet_hodnot = random.randrange(10, 50)

    # kontrolny vypis na pocet hodnot
    print(f"pocet hodnot: {pocet_hodnot}")

    for i in range(pocet_hodnot):
        pred.put((i, random.randrange(100, 1000)))
        pocitadlo.value += 1
    pred.put("koniec")


def vykonaj_operaciu(pred, za):
    # POZOR, viac procesov cita z citac_pred a zapisuje do zapisovac_pred a zapisovac_za
    # tu by bolo vhodne zabezpecit nejaku synchronizaciu citania a zapisovania
    # alebo namiesto Pipe pouzit Queue

    while True:
        data = pred.get()
        if data == "koniec":
            pred.put("koniec")
            return
        # nezapisujeme cely velky vysledok, ale kvoli prehladnosti len jeho prvych 10 cifier
        vysledok = str(data[1] ** data[1])[:10]
        za.put((data[0], vysledok))


def zapis_data(subor_out, za, pocitadlo):
    # len simulujeme zapis do suboru
    pocet_ukoncenych = 0
    while pocet_ukoncenych < pocitadlo.value:
        data = za.get()
        pocet_ukoncenych += 1
        print(data)


if __name__ == "__main__":
    pred = multiprocessing.Queue()
    za = multiprocessing.Queue()

    # registrujeme kolko, kolko hodnot je potrebne spracovat
    pocitadlo = multiprocessing.Value("i", 0)
    pocet_jadier = multiprocessing.cpu_count()

    cas = time.time_ns()

    vstup = multiprocessing.Process(
        target=citaj_data, args=("data.in", pred, pocitadlo)
    )
    vstup.start()

    procesy = []
    for i in range(pocet_jadier):
        proces = multiprocessing.Process(target=vykonaj_operaciu, args=(pred, za))
        proces.start()
        procesy.append(proces)

    vystup = multiprocessing.Process(
        target=zapis_data, args=("data.out", za, pocitadlo)
    )
    vystup.start()

    vstup.join()
    vstup.close()

    for proces in procesy:
        proces.join()
        proces.close()

    vystup.join()
    vystup.close()

    print(f"cas: {(time.time_ns() - cas) / 10**9}")
