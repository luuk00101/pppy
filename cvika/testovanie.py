import math
import doctest


def obsah_kruhu(polomer):
    if not isinstance(polomer, (int, float)):
        raise ValueError("Polomer nemoze byt retazec.")
    if polomer < 0:
        raise ValueError("Polomer nemoze byt zaporny.")

    return math.pi * polomer**2


if __name__ == "__main__":
    doctest.testfile("testy.txt")
