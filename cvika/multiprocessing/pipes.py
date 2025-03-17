import multiprocessing
import random
import time

def citaj_data(subor_in, zapisovac_pred, pocitadlo):
    # len simulujeme citanie zo suboru
    pocet_hodnot = random.randrange(10, 50)

    # kontrolny vypis na pocet hodnot
    print(f'pocet hodnot: {pocet_hodnot}')
    
    for i in range(pocet_hodnot):
        zapisovac_pred.send((i, random.randrange(100, 1000)))
        pocitadlo.value += 1
    zapisovac_pred.send('koniec')


def vykonaj_operaciu(citac_pred, zapisovac_pred, zapisovac_za):
    # POZOR, viac procesov cita z citac_pred a zapisuje do zapisovac_pred a zapisovac_za
    # tu by bolo vhodne zabezpecit nejaku synchronizaciu citania a zapisovania
    # alebo namiesto Pipe pouzit Queue
    
    while True:
        data = citac_pred.recv()
        if data == 'koniec':
            zapisovac_pred.send('koniec')
            return
        # nezapisujeme cely velky vysledok, ale kvoli prehladnosti len jeho prvych 10 cifier
        vysledok = str(data[1] ** data[1])[:10]
        zapisovac_za.send((data[0], vysledok))


def zapis_data(subor_out, citac_za, pocitadlo):
    # len simulujeme zapis do suboru
    pocet_ukoncenych = 0
    while pocet_ukoncenych < pocitadlo.value:
        data = citac_za.recv()
        pocet_ukoncenych += 1
        print(data)


if __name__ == "__main__":
    citac_pred, zapisovac_pred = multiprocessing.Pipe()
    citac_za, zapisovac_za = multiprocessing.Pipe()

    # registrujeme kolko, kolko hodnot je potrebne spracovat
    pocitadlo = multiprocessing.Value('i', 0)
    pocet_jadier = multiprocessing.cpu_count()
    
    cas = time.time_ns()

    vstup = multiprocessing.Process(target=citaj_data, args=('data.in', zapisovac_pred, pocitadlo))
    vstup.start()

    procesy = []
    for i in range(pocet_jadier):
        proces = multiprocessing.Process(target=vykonaj_operaciu, args=(citac_pred, zapisovac_pred, zapisovac_za))
        proces.start()
        procesy.append(proces)

    vystup = multiprocessing.Process(target=zapis_data, args=('data.out', citac_za, pocitadlo))
    vystup.start()

    vstup.join()
    vstup.close()

    for proces in procesy:
        proces.join()
        proces.close()

    vystup.join()
    vystup.close()

    print(f'cas: {(time.time_ns() - cas) / 10**9}')