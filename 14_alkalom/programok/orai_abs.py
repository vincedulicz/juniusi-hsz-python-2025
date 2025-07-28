from abc import ABC, abstractmethod


class Jarmu(ABC):
    def __init__(self, sebesseg):
        self.sebesseg = sebesseg

    def alap_info(self):
        return f'Sebesség: {self.sebesseg}'

    @abstractmethod
    def halad(self):
        """ megoldás: :) """
        pass

    @abstractmethod
    def fogyasztas(self):
        pass


class Auto(Jarmu):
    def __init__(self, sebesseg, utasok, tipus):
        super().__init__(sebesseg)
        self.utasok = utasok
        self.tipus = tipus

    def halad(self):
        return f'{self.sebesseg} km/h halad az autó'

    def fogyasztas(self):
        return f'nincs fogyasztas'

    def tipus_info(self):
        return f'{self.tipus} ez a típusa'

    def utasok_adat(self):
        return f'{self.utasok} darab ember'

    def alap_info(self):
        return f'{self.tipus} + {self.utasok}'

class ElektromosAuto(Auto):
    def __init__(self, sebesseg, utasok, tipus, akku_kapacitas):
        super().__init__(sebesseg, utasok, tipus)
        self.akku_kapacitas = akku_kapacitas

    def halad(self):
        return f'elektromos autó {self.sebesseg} km/h halad'

    def akku_info(self):
        return f'kapacitás: {self.akku_kapacitas}'


e_auto = ElektromosAuto(120, 5, "tesla", 12)
print(e_auto.tipus_info())
print(e_auto.halad())

a = Auto(200, 4, "ford")
print(a.alap_info())
print(a.utasok_adat())

