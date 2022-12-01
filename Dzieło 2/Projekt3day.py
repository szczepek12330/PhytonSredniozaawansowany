#
# print("Cena 50m2 mieszkania w Warszawie uwzględniająca inflacje oraz miejsce parkingowe")
#

class RealnyKosztMieszkania:
    def __init__(self, value):
        self.value = value


class CenaRynkowaMieszkania(RealnyKosztMieszkania):
    def __init__(self):
        RealnyKosztMieszkania.__init__(self, 500000)


class Inflacja:
    def __init__(self):
        self.value *= 1,18


class Parking:
    def __init__(self):
        self.value = 20000
        self.value += 20000


class ALL1(RealnyKosztMieszkania, Parking, Inflacja):
    def __init__(self, value):
        RealnyKosztMieszkania.__init__(self, value)
        Inflacja.__init__(self)
        Parking.__init__(self)


class ALL2(RealnyKosztMieszkania, Inflacja, Parking):
    def __init__(self, value):
        RealnyKosztMieszkania.__init__(self, value)
        Inflacja.__init__(self)
        Parking.__init__(self)


class Inlfacja2(RealnyKosztMieszkania):
    def __init__(self, value):
        RealnyKosztMieszkania.__init__(self, value)
        self.value *= 1,20


class Parking2(RealnyKosztMieszkania):
    def __init__(self, value):
        RealnyKosztMieszkania.__init__(self, value)
        self.value += 30000


class Wynik1(Inlfacja2, Parking2):
    def __init__(self, value):
        Inflacja2.__init__(self, value)
        Parking2.__init__(self, value)


class Inflacja2(RealnyKosztMieszkania):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 1,20


class Parking2(RealnyKosztMieszkania):
    def __init__(self, value):
        super().__init__(value)
        self.value += 30000


class Wynik2(Inflacja2, Parking2):
    def __init__(self, value):
        super().__init__(value)


k3 = Wynik1(500000)
print("Powinno być (500000*1,20) + 30000 = x, ale jest", k3.value)

k4 = Wynik2(500000)
print("Powinno być (500000*1,20) + 30000 = 98 i jest ", k4.value)


k1 = ALL1(500000)
print('Jenda z możliwych kolejności działań to (500000 * 1,18) + 20000 =', k1.value)
k2 = ALL2(500000)
print('Jenda z możliwych kolejności działań to (500000 * 1,18) + 20000 =', k2.value)

mro_str = '\n'.join(repr(cls) for cls in Wynik2.mro())
print(mro_str)