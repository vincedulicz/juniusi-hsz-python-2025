class A:
    def __init__(self):
        self.nev = "A"
        self._protected_tag = 0

    def _procted_method(self):
        return 0

    def __privat_method(self):
        return "private method"

    def kiir(self):
        return f'Ez a(z) {self.nev} osztály.'

    @staticmethod
    def display():
        print("cool")

a = A()
print(a.kiir())
print(A.kiir(a))
A.display()

class B(A):
    def __init__(self):
        super().__init__()
        self.nev = "B"
        self._procted_tag = 1

class C(A):
    def __init__(self):
        super().__init__()
        self.nev = "C"

a = A()
b = B()
b._procted_method()

c = C()
print(f'a: {a.kiir()} b: {b.kiir()} c: {c.kiir()}')


class D(B, C):
    def __init__(self):
        super().__init__()

d = D()
print(d.kiir())

print(D.mro())