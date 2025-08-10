from Ember import Ember

class Tanar(Ember):
    def __init__(self, nev, eletkor, tantargy):
        super().__init__(nev, eletkor)
        self.tantargy = tantargy
        self.osztalyok = []


    def add_osztaly(self, osztaly):
        if osztaly not in self.osztalyok:
            self.osztalyok.append(osztaly)

    def bemutatkozik(self):
        super().bemutatkozik()
        print(f"Tantárgy: {self.tantargy}")
        print(f"Tanít az osztályokban: {', '.join(self.osztalyok)}")

