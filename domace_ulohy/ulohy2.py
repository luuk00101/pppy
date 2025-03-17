from collections import deque


def jePalindrom(slovo):
    upravene_slovo = slovo.lower().strip().replace(" ", "")
    return upravene_slovo == upravene_slovo[::-1]


def gen_fib(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


# for cislo in gen_fib(10):
#     if cislo % 2 == 0:
#         print(cislo)


def point_distance_2D(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def point_distance_3D(x1, y1, z1, x2, y2, z2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5


def point_distance_from_origin_2D(x, y):
    return (x**2 + y**2) ** 0.5


def calculate_factorial(n):
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)


def number_of_k_member_variants(k, n):
    return calculate_factorial(n) / calculate_factorial(n - k)


def validate_birth_number(birth_number):
    if len(birth_number) != 10 and len(birth_number) != 9:
        return False

    if not birth_number.isdigit():
        return False

    if (
        int(birth_number[2:4]) > 61
        or (int(birth_number[2:4]) < 51 and int(birth_number[2:4]) > 12)
        or int(birth_number[2:4]) < 1
        or int(birth_number[4:6]) > 31
        or int(birth_number[4:6]) < 1
    ):
        return False

    if int(birth_number) % 11 != 0:
        return False

    return True


# print(validate_birth_number("1201211766"))


def prihod_do_kosu(kos, pradlo):
    kos.append(pradlo)


def vyhod_z_kosu(kos):
    kos.pop()


def pozri_vrch_kosu(kos):
    return kos[-1]


def je_kos_prazdny(kos):
    return len(kos) == 0


def presyp_do_ineho_kosu(kos1, kos2):
    kos2.extend(kos1)
    kos1.clear()


kos_na_pradlo = deque()

prihod_do_kosu(kos_na_pradlo, "tricko")
prihod_do_kosu(kos_na_pradlo, "ponozky")

pole_bodov = [[1, 2], [4, 1], [0, 1]]
pole_bodov.sort(key=lambda bod: point_distance_from_origin_2D(bod[0], bod[1]))
# print(pole_bodov)

# ZORADENIE slov - urobím si funkciu, kde chytím zoznam znakov môjho usporiadania,
# prejdem slovo, ktoré som dostal a vytvorím si zoznam, kde budem mať
# indexy znakov z mojho usporiadania a na koniec vrátim zoznam indexov, ktorym
# budem môcť usporiadať slovo - to použijem ako key pre sort (lambda funkcia)


def custom_sort_order(word, order):
    order_index = {char: index for index, char in enumerate(order)}
    return [order_index.get(char, -1) for char in word]


words = ["banana", "apple", "orange"]
custom_order = "abcdefghijklmnopqrstuvwxyz"
words.sort(key=lambda word: custom_sort_order(word, custom_order))


def je_prvocislo(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def gen_prvocisla(n):
    cislo = 1

    while cislo < n:
        cislo += 1
        if je_prvocislo(cislo):
            yield cislo


def vytvor_zoznam_prvocisel(n):
    return list(gen_prvocisla(n))


# print(vytvor_zoznam_prvocisel(10))

# TODO: upraviť úlohu na riešenie pre ľubovoľný počet čísel


def super_sum(*argv):
    suma = 0
    for prvok in argv:
        if isinstance(prvok, list) or isinstance(prvok, tuple):
            suma += super_sum(*prvok)  # Use * to unpack the list or tuple
        else:
            suma += prvok
    return suma


print(super_sum(1, 2, (3, [4]), [5], [[[[[6]]]]]))
