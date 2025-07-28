class Repulo:
    def __init__(self, sebesseg):
        self.sebesseg = sebesseg

    def repul(self):
        return f'a jármű {self.sebesseg} km/h halad'

    @staticmethod
    def foo():
        print("repulo foo")

class Auto:
    def __init__(self, kerek_szam):
        self.kerek_szam = kerek_szam

    def vezet(self):
        return f'a jármű {self.kerek_szam} kerékkel gurul'

    def foo(self):
        print("auto foo")


class RepuloAuto(Auto, Repulo):
    def __init__(self, sebesseg, kerek_szam):
        Repulo.__init__(self, sebesseg)
        Auto.__init__(self, kerek_szam)

    def jarmu_info(self):
        return f'ez egy repülő autó és ' \
               f'{self.kerek_szam} kerékkel és ' \
               f'{self.sebesseg} km/h-val halad'


repuloauto = RepuloAuto(300, 4)

print(repuloauto.repul())
print(repuloauto.vezet())
print(repuloauto.jarmu_info())

repuloauto.foo()