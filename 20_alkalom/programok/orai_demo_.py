class NeCsinaljIlyet:
    _teszt = 0

    def __init__(self):
        pass

    def set_teszt(self, new_value):
        self.teszt = new_value

    def get_teszt(self):
        return self.teszt

ncsi = NeCsinaljIlyet()

# ncsi.set_teszt(1)
print(ncsi.get_teszt())

# print(ncsi.get_teszt())
# print(ncsi.teszt)


class Kavegep:
    GYARTO = "bestcoffer inc. 4 ever" # osztályváltozó
    _teszt = 0

    def __init__(self, modell):
        self.modell = modell # példányváltozó
        self._viz = ""

    @property
    def viz(self):
        return self._viz

    @viz.setter
    def viz(self, uj_viz):
        self._viz = uj_viz

    def foo(self):
        print(f"{self.modell} print goes brrr")



    @classmethod
    def modosits_gyartot(cls, uj_gyarto):
        if not uj_gyarto.strip():
            print("hiba")
            return
        cls.GYARTO = uj_gyarto
        print("modify gyarto done...")


"""
k = Kavegep("modelllerr2000")
k.foo()

masik_k = Kavegep("fosmodelllll30000000")
masik_k.foo()

print(k.GYARTO)
print(masik_k.GYARTO)
print(Kavegep.GYARTO)
k.GYARTO = "fosgyártó inc kft lehúza.."

print(k.GYARTO)
print(masik_k.GYARTO)
print(Kavegep.GYARTO)

k.modosits_gyartot("fostalicskakft2000")
print(k.GYARTO)
print(masik_k.GYARTO)
print(Kavegep.GYARTO)
"""