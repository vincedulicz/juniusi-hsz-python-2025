class Person:
    name = "John"
    age = 36
    country = "hu"

    def _protected_fuggveny(self):
        pass

    def __private_method(self):
        pass

    def public_method(self):
        return self.__privat

"""
ertek = getattr(Person, 'age')
print(ertek)

setattr(Person, 'age', 40)
ertek = getattr(Person, 'age')

print(ertek)

print(hasattr(Person, 'name2'))

"""


class Cica(object):
    def __init__(self):
        self._nev = "Cirmi" # protected
        self.__privat = "str" # privát

    def __str__(self):
        return f'cica: {self._nev}'

    def __eq__(self, other):
        if isinstance(other, Cica):
            return self._nev == other.nev

    @property
    def nev(self):
        return self._nev

    @nev.setter
    def nev(self, value):
        if value == "cirmi":
            print("nem lehet ilyen név")
            return

        self._nev = value

    @nev.deleter
    def nev(self):
        print("deleter")
        del self._nev

c = Cica() # példány létrehozása
print(c)

c.nev = "cirmi2" # set

print(c.nev) # get

c2 = Cica()
c2.nev = "cirmi3"

print(c2)

print(c == c2)