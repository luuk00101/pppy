class T1:
    def __init__(self, t1):
        self.t1 = t1

    def id(self):
        return f"T1 - {self.t1}"


class T2:
    def __init__(self, t2):
        self.t2 = t2

    def id(self):
        return f"T2 - {self.t2}"


class T3(T2, T1):
    def __init__(self, t1, t2, t3):
        super(T3, self).__init__(t2)
        super(T2, self).__init__(t1)
        self.t3 = t3

    def id(self):
        return f"T3 - {self.t3}"

    def predkovia(self):
        print(self.t1, self.t2, self.t3)
        print(super(T2, self).id())
        print(super(T3, self).id())
        print(self.id())


objekt = T3(1, 2, 3)
print(objekt.t1)
print(objekt.t2)
print(objekt.t3)

print()

print(objekt.id())

print()

objekt.predkovia()

print()

print(T3.__mro__)
