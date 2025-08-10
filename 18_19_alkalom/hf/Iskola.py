
class Iskola:
    osztalyvaltozo = 0

    def __init__(self, nev):
        self.ez_meg_peldany_valtozo = 0
        self.nev = nev
        self.osztalyok = []

    def add_osztaly(self, osztaly):
        for existing_osztaly in self.osztalyok:
            if existing_osztaly.nev == osztaly.nev:
                print(f"Hiba: Már létezik '{osztaly.nev}' nevű osztály az iskolában!")
                return

        self.osztalyok.append(osztaly)
        print(f"'{osztaly.nev}' osztály sikeresen hozzáadva az iskolához.")

    def iskola_info(self):
        print(f"Iskola: {self.nev}")
        for osztaly in self.osztalyok:
            osztaly.osztaly_info()
            print()