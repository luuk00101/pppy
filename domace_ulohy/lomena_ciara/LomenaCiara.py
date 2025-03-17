from .Bod import Bod


class LomenaCiara:
    def __init__(self):
        self.__body = []
        self.__otvorena = True

    def pridaj_bod(self, bod):
        self.__body.append(bod)
        self.__body.sort(key=lambda bod: (bod.x, bod.y))

    def vrat_body(self):
        return self.__body

    def zmen_otvorenost(self):
        self.__otvorena = not self.__otvorena

    def vypis_otvorena(self):
        return self.__otvorena

    def zmaz_bod(self, bod):
        if bod in self.__body:
            self.__body.remove(bod)
        else:
            raise ValueError("Bod sa nenachádza v lomenej čiare")

    def dlzka(self):
        dlzka = 0

        for i in range(len(self.__body) - 1):
            dlzka += self.__body[i].vzdialenost_od_ineho_bodu(self.__body[i + 1])

        if not self.__otvorena and len(self.__body) > 2:
            dlzka += self.__body[-1].vzdialenost_od_ineho_bodu(self.__body[0])

        return dlzka

    def najdolezitejsi_bod(self):
        najkratsia_dlzka = self.dlzka()

        cache = LomenaCiara()

        for bod in self.__body:
            cache.__body = self.__body.copy()
            cache.zmaz_bod(bod)

            dlzka = cache.dlzka()

            if dlzka < najkratsia_dlzka:
                najkratsia_dlzka = dlzka
                najdolezitejsi_bod = bod

        return najdolezitejsi_bod

    def uloz_do_suboru(self, nazov_suboru):
        with open(nazov_suboru, "w") as f:
            for bod in self.__body:
                f.write(f"{bod}\n")

    def nacitaj_zo_suboru(self, nazov_suboru):
        with open(nazov_suboru, "r") as f:
            for line in f:
                self.pridaj_bod(eval(line.strip()))

    def __str__(self):
        return " -> ".join(f"({p.x}, {p.y})" for p in self.__body)

    def __getitem__(self, index):
        if isinstance(index, slice):
            vyrezanaCiara = LomenaCiara()
            vyrezanaCiara.__otvorena = self.__otvorena
            for bod in self.__body[index]:
                vyrezanaCiara.pridaj_bod(bod)
            return vyrezanaCiara
        elif isinstance(index, int):
            return self.__body[index]
        else:
            raise TypeError("Invalid argument type.")

    def __delitem__(self, index):
        if isinstance(index, slice):
            for bod in self.__body[index]:
                self.zmaz_bod(bod)
        elif isinstance(index, int):
            self.zmaz_bod(self.__body[index])
        else:
            raise TypeError("Invalid argument type.")

    def append(self, bod):
        if not isinstance(bod, Bod):
            raise ValueError("Value must be an instance of Bod")

        self.pridaj_bod(bod)

    def __contains__(self, bod):
        return bod in self.__body

    def __iter__(self):
        for bod in self.__body:
            yield bod

    def __len__(self):
        return len(self.__body)

    def index(self, bod):
        return self.__body.index(bod)
