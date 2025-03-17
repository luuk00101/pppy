class Bod:
    def __init__(self, x, y):
        self.nastav_x(x)
        self.nastav_y(y)
        self.__index = 0

    def nastav_x(self, x):
        if not isinstance(x, (int, float)):
            raise ValueError("x musí byť číslo")
        self.__x = x

    def nastav_y(self, y):
        if not isinstance(y, (int, float)):
            raise ValueError("y musí byť číslo")
        self.__y = y

    def zisti_x(self):
        return self.__x

    def zisti_y(self):
        return self.__y

    x = property(zisti_x, nastav_x)
    y = property(zisti_y, nastav_y)

    def __str__(self):
        return f"Bod({self.x}, {self.y})"

    def vzdialenost_od_ineho_bodu(self, iny_bod):
        if not isinstance(iny_bod, Bod):
            raise ValueError("Argument musí byť inštanciou triedy Bod")

        return ((self.x - iny_bod.x) ** 2 + (self.y - iny_bod.y) ** 2) ** 0.5

    def __eq__(self, other):
        if not isinstance(other, Bod):
            return False
        return self.x == other.x and self.y == other.y
