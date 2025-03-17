import abc


class Vozidlo(abc.ABC):
    def __init__(self, kapacita, cenaZaKm):
        self.kapacita = kapacita
        self.cenaZaKm = cenaZaKm

    @abc.abstractmethod
    def cena_za_trasu(self, km):
        pass


class Auto(Vozidlo):
    def __init__(self):
        super().__init__(kapacita=15, cenaZaKm=0.4)

    @staticmethod
    def cena_za_trasu(self, km):
        return km * self.cenaZaKm


class Autobus(Vozidlo):
    def __init__(self):
        super().__init__(kapacita=51, cenaZaKm=0.87)

    @staticmethod
    def cena_za_trasu(self, km):
        return km * self.cenaZaKm
