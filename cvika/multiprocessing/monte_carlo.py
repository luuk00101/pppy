import multiprocessing
import random


def simuluj_hody(pocet_hodov, zapisovac):
    dlzka_steny = 50
    pocet_trafenych = 0

    for i in range(pocet_hodov):
        x = random.uniform(-1, 1) * dlzka_steny
        y = random.uniform(-1, 1) * dlzka_steny

        if x**2 + y**2 <= dlzka_steny**2:
            pocet_trafenych += 1

    zapisovac.put((pocet_trafenych, pocet_hodov - pocet_trafenych))


def vypocitaj_pi(pocet_jadier, zapisovac):
    pocet_vysledkov = 0
    hodnoty_pi = []

    while pocet_vysledkov < pocet_jadier:
        pocet_trafenych, pocet_nezasiahol = zapisovac.get()
        pocet_vysledkov += 1

        pi = 4 * pocet_trafenych / (pocet_trafenych + pocet_nezasiahol)
        hodnoty_pi.append(pi)

    print(sum(hodnoty_pi) / pocet_jadier)


if __name__ == "__main__":
    pocet_jadier = multiprocessing.cpu_count()

    zapisovac = multiprocessing.Queue()
    pocet_hodov = 1_000_000_000

    procesy = []
    for i in range(pocet_jadier):
        proces = multiprocessing.Process(
            target=simuluj_hody, args=(pocet_hodov, zapisovac)
        )
        proces.start()
        procesy.append(proces)

    vystup = multiprocessing.Process(
        target=vypocitaj_pi, args=(pocet_jadier, zapisovac)
    )
    vystup.start()

    for proces in procesy:
        proces.join()
        proces.close()

    vystup.join()
    vystup.close()
