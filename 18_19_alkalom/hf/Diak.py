from Ember import Ember
class Diak(Ember):
    def __init__(self, nev, eletkor):
        super().__init__(nev, eletkor)
        self._osztaly = None
        self.osztalyzatok = []

    @property
    def osztaly(self):
        return self._osztaly

    @osztaly.setter
    def osztaly(self, osztaly):
        self._osztaly = osztaly

    def add_grade(self, grade):
        self.osztalyzatok.append(grade)

    def average(self):
        if not self.osztalyzatok:
            return 0
        return sum(self.osztalyzatok) / len(self.osztalyzatok)

    def bemutatkozik(self):
        super().bemutatkozik()
        print(f"Osztály: {self.osztaly}")
        print(f"Osztályzatok: {self.osztalyzatok}")
        print(f"Átlag: {self.average():.2f}")