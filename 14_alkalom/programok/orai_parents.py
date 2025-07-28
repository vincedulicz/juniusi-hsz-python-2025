class Eloleny(object):
    def __init__(self, nev):
        self.nev = nev

    def lelegzik(self):
        print(f'{self.nev} levegőt vesz')

class Emlos(Eloleny):
    def __init__(self, nev, szorzet_szine):
        super().__init__(nev)
        self.szorzet_szine = szorzet_szine

    def mozog(self):
        return f'{self.nev} négy lábon jár'

class Kutya(Emlos):
    def __init__(self, nev, szorzet_szine, fajta):
        super().__init__(nev, szorzet_szine)
        self.fajta = fajta

    def mozog(self):
        return f'{self.fajta} +4 lábon legalább jár'

    def lelegzik(self):
        return f'{self.nev} máshogy lélegzik'


kutya = Kutya("Buksi", "barna", "vizsla") # példányosítás
print(kutya.lelegzik())
print(kutya.mozog())


emlos = Emlos("emlős", "barna")
emlos.lelegzik()
print(emlos.nev)

peldany = Eloleny("cica")

peldany.lelegzik()

peldany_ = Eloleny("kutya")

peldany_.lelegzik()