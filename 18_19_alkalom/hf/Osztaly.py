
class Osztaly:
    def __init__(self, nev):
        self.nev = nev
        self.diakok = []
        self.tanarok = []

    def add_diak(self, diak):
        self.diakok.append(diak)
        diak.osztaly = self.nev

    def add_tanar(self, tanar):
        self.tanarok.append(tanar)
        tanar.add_osztaly(self.nev)

    def osztaly_info(self):
        def atlag_szerint_rendezesi_kulcs(diak):
            return diak.average()

        print(f"Osztály: {self.nev} \n Tanár(ok):")

        for tanar in self.tanarok:
            print(f" - {tanar.nev} (tantárgy: {tanar.tantargy})")

        print("Diák(ok):")
        sorted_diakok = sorted(self.diakok, key=atlag_szerint_rendezesi_kulcs, reverse=True)

        for diak in sorted_diakok:
            print(f" - "
                  f"{diak.nev} ({diak.eletkor} éves), "
                  f"Osztályzatok: {diak.osztalyzatok}, "
                  f"Átlag: {diak.average():.2f}"
                  )