import multiprocessing

def funkcia(parameter):
    return parameter ** 2

if __name__ == "__main__":
    procesy = multiprocessing.Pool(processes=4)
    vysledok = procesy.map(funkcia, range(1, 9))
    print(vysledok)

