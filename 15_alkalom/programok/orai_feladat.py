class Ember:
    def __init__(self, nev, eletkor):
        # TODO: property get/set
        self.nev = nev
        self.eletkor = eletkor

    def bemutatkozik(self):
        print(f'nev: {self.nev}, eletkor: {self.eletkor}')

class Tanar(Ember):
    def __init__(self, nev, eletkor, tantargy):
        super().__init__(nev, eletkor)
        self.tantargy = tantargy
        self.osztaly = None

    def osztaly_kap(self, osztaly):
        self.osztaly = osztaly

    def bemutatkozik(self):
        super().bemutatkozik()
        print(f'tantrágy: {self.tantargy}')
        if self.osztaly:
            print(f'tanít az osztályban: {self.osztaly}')

class Diak(Ember):
    def __init__(self, nev, eletkor):
        super().__init__(nev, eletkor)
        self.osztalyzatok = []
        self.osztaly = None

    def add_grade(self, grade):
        self.osztalyzatok.append(grade)

    def avarage(self):
        if len(self.osztalyzatok) == 0:
            return 0
        return sum(self.osztalyzatok) / len(self.osztalyzatok)

    def set_osztaly(self, osztaly):
        self.osztaly = osztaly

    def bemutatkozik(self):
        super().bemutatkozik()
        if self.osztaly:
            print(f'osztály: {self.osztaly}')
        print(f'osztályzatok: {self.osztalyzatok}')
        print(f'átlag: {self.avarage():.2f}')

class Osztaly:
    def __init__(self, nev):
        self.nev = nev
        self.diakok = []
        self.tanarok = []

    def add_diak(self, diak):
        self.diakok.append(diak)
        diak.set_osztaly(self.nev)

    def add_tanar(self, tanar):
        self.tanarok.append(tanar)
        tanar.osztaly_kap(self.nev)

    def osztaly_info(self):
        print(f'osztály: {self.nev}')
        print("tanárok")
        for tanar in self.tanarok:
            print(f" - {tanar.nev} tantrágy: {tanar.tantargy}")
        print("diákok")
        for diak in self.diakok:
            print(f'{diak.nev} {diak.eletkor} éves és osztályzatok {diak.osztalyzatok}, átlag: {diak.avarage():.2f}')

def main():
    osztaly = Osztaly("10.A")

    tanar = Tanar("NAgy Péter", 40, "matek")
    osztaly.add_tanar(tanar)

    diak1 = Diak("Kovács ANna", 16)
    diak1.add_grade(5)
    diak1.add_grade(3)
    diak1.add_grade(4)

    osztaly.add_diak(diak1)

    diak2 = Diak("Szabló Lázsló", 17)
    diak2.add_grade(2)
    diak2.add_grade(3)

    osztaly.add_diak(diak2)

    osztaly.osztaly_info()


main()
