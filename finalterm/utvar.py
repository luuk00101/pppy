import abc
import math


class Utvar(abc.ABC):
    @abc.abstractmethod
    def obsah(self):
        """Vrati obsah utvaru"""
        raise NotImplemented

    @abc.abstractmethod
    def obvod(self):
        """Vrati obvod utvaru"""
        raise NotImplemented


class Kruh(Utvar):
    def __init__(self, polomer):
        self.__polomer = polomer

    def __zisti_polomer(self):
        return self.__polomer

    def __nastav_polomer(self, polomer):
        if not isinstance(polomer, (int, float)):
            raise TypeError("Polomer musi byt cislo")

        if polomer <= 0:
            raise ValueError("Polomer musi byt kladne cislo")

        self.__polomer = polomer

    polomer = property(__zisti_polomer, __nastav_polomer)

    def obsah(self):
        return math.pi * self.__polomer**2

    def obvod(self):
        return 2 * math.pi * self.__polomer

    def __str__(self):
        return f"Kruh s polomerom {self.__polomer}"

    def __lt__(self, other):
        if not isinstance(other, Kruh):
            raise TypeError("Porovnavat sa daju len kruhy")

        return self.__polomer < other.__polomer

    def __le__(self, other):
        if not isinstance(other, Kruh):
            raise TypeError("Porovnavat sa daju len kruhy")

        return self.__polomer <= other.__polomer

    def __gt__(self, other):
        if not isinstance(other, Kruh):
            raise TypeError("Porovnavat sa daju len kruhy")

        return self.__polomer > other.__polomer

    def __ge__(self, other):
        if not isinstance(other, Kruh):
            raise TypeError("Porovnavat sa daju len kruhy")

        return self.__polomer >= other.__polomer

    def __eq__(self, other):
        if not isinstance(other, Kruh):
            raise TypeError("Porovnavat sa daju len kruhy")

        return self.__polomer == other.__polomer

    def __ne__(self, other):
        if not isinstance(other, Kruh):
            raise TypeError("Porovnavat sa daju len kruhy")

        return self.__polomer != other.__polomer

    def uloz(self, subor):
        with open(subor, "w") as f:
            f.write(f"polomer = {self.__polomer}")

    def nacitaj(self, subor):
        with open(subor, "r") as f:
            self.__polomer = f.read().split("=")[1].strip()

    def __repr__(self):
        return f"Kruh({self.__polomer})"

    """"
    Metóda sa má použiť s __repr__ formátom, napr. Kruh(5)
    """

    def kruh_zo_suboru(subor):
        with open(subor, "r") as f:
            return eval(f.read())

    # Code has been deleted as per instructions
