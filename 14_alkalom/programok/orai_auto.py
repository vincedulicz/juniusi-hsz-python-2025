class Auto:
    gyartok = ["Toyota", "BMW", "Tesla"] # osztály változó

    def __init__(self, marka, modell, evjarat): # konstruktor
        # példány változó
        self.marka = marka
        self.modell = modell
        self.evjarat = evjarat
        self.__km_ora = 0 # privát változó

    def info(self):
        """ public method """
        return f'{self.evjarat} {self.marka} {self.modell}, {self.__km_ora} km-rel'

    def __titkos_ugras(self):
        """ private method """
        print(f'{self.marka} gyorsan ugrik előre')

    def _novenyesitett_ora(self):
        """ protected method """
        self.__km_ora += 10

    def uj_km(self, km):
        """ setter a privát változóhoz """
        if km > self.__km_ora:
            self.__km_ora = km
        else:
            print("Nem állíthatod vissza az órát!")

    @classmethod
    def gyartok_listaja(cls):
        return cls.gyartok

    @staticmethod
    def uzemanyag_koltseg(km, liter_ar):
        return km * 0.06 * liter_ar

auto1 = Auto("Toyota", "Corolla", 2015)

# public method
print(auto1.info())

# setter
auto1.uj_km(15000)
print(auto1.info())

# protected method
auto1._novenyesitett_ora()
print(auto1.info())

# osztály metódus hívás
print('elérhető gyártok:', Auto.gyartok_listaja())

# statikus metódus hívása
print('üzemanyag költség 1000km-re:', Auto.uzemanyag_koltseg(1000, 400), "Ft")

# auto1.__titkos_ugras() # Ez hibát okoz!!!