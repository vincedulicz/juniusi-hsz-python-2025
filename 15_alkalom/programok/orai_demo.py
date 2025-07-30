class Number(object):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        print("getter")
        return self._value

    @value.setter
    def value(self, new_value):
        print("setter")
        if new_value != 0:
            self._value = new_value
            return
        print("nem lehet 0")

    def __eq__(self, other):
        """ obj1 == obj2 """
        return self._value == other._value

    def __ne__(self, other):
        """ obj1 != obj2 """
        return self._value != other._value

    def __add__(self, other):
        """ obj1 + obj2 """
        return Number(self._value + other._value)

    def __sub__(self, other):
        """ obj1 - obj2 """
        return Number(self._value - other._value)

    def __iadd__(self, other):
        """ obj1 += obj2 """
        print("iadd")
        if other._value == 10:
            print("10-et nem lehet hozzáadni")
            return
        self._value += other._value
        return self

    def __lt__(self, other):
        """ obj1 < obj2 """
        return self._value < other._value

    def __gt__(self, other):
        """ obj1 > obj2"""
        return self._value > other._value

    def __le__(self, other):
        """ obj1 <= obj2 """
        return self._value <= other._value

    def __ge__(self, other):
        """ obj1 >= obj2 """
        return self._value >= other._value

    def __str__(self):
        return f'ez egy number object {self.value}'

"""
szam = Number(3)
masik_szam = Number(10)

print(szam)

print(szam == masik_szam)
print(szam != masik_szam)
print(szam > masik_szam)
szam += masik_szam
print(szam)
"""

