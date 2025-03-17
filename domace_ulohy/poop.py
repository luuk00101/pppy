class Dlzka(float):
    def __new__(cls, hodnota, jednotka='m'):
        instancia = super().__new__(cls, hodnota)
        instancia.jednotka = jednotka
        return instancia

    def __str__(self):
        return f'{self.real} {self.jednotka}'
    
    
class Trieda:
    pass

def mocnina(cislo):
    return cislo ** 2

o = Trieda()
o.x = 10
o.f = mocnina
print(o.__dict__)
print(o.f(5))
