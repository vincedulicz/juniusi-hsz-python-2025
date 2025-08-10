class Ember:
    def __init__(self, nev, eletkor):
        self.nev = nev
        self.eletkor = eletkor

    def bemutatkozik(self):
        print(f"Név: {self.nev}, Életkor: {self.eletkor}")
