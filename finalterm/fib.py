import multiprocessing
import time
import sys


def fibonacci_cifry(n):
    """
    Pre zadane n vrati dvojicu: n a pocet cifier n-teho clena fibonacciho postupnosti

    :param n: index clena fibonacciho postupnosti
    :type n: int|str
    :return: dvojica (index, pocet cifier clena fibonacciho postupnosti)
    :rtype: tuple[int, int]
    """
    try:
        n = int(n)
    except ValueError:
        raise TypeError("Vstup musi byt konvertovatelny na int")
    if n < 0:
        raise ValueError("Vstupna hodnota musi reprezentovat kladne cislo")

    if n < 2:
        return n, 1
    a, b = 0, 1
    for i in range(n):
        b, a = a + b, b
    return n, len(str(a))


sys.set_int_max_str_digits(1000000)

if __name__ == "__main__":

    cas = time.time_ns()

    with open("indexy.txt", "r") as f:
        indexy = f.readlines()

    with multiprocessing.Pool() as pool:
        vysledky = pool.map(fibonacci_cifry, indexy)

    with open("cifry.txt", "w") as f:
        for index, cislo in vysledky:
            f.write(f"{index} : {cislo}\n")

    print((time.time_ns() - cas) / 10**9)
