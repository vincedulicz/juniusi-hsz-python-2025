from Iskola import Iskola
from Tanar import Tanar
from Diak import Diak
from Osztaly import Osztaly


class UserMenu:
    def __init__(self):
        self.iskola = Iskola("Gimnázium")

    def run(self):
        while True:
            self.show_menu()

            valasz = input("Válassz egy lehetőséget: ")

            if valasz == "1":
                self.add_osztaly()
            elif valasz == "2":
                self.add_tanar_to_osztaly()
            elif valasz == "3":
                self.add_diak_to_osztaly()
            elif valasz == "4":
                self.show_iskola_info()
            elif valasz == "5":
                print("Kilépés...")
                break
            else:
                print("Érvénytelen választás! Próbáld újra.")

    def show_menu(self):
        print("\n| Iskola Kezelő Rendszer |")
        print("1. Új osztály hozzáadása")
        print("2. Tanár hozzáadása osztályhoz")
        print("3. Diák hozzáadása osztályhoz")
        print("4. Iskola információinak megjelenítése")
        print("5. Kilépés")

    def add_osztaly(self):
        nev = input("Add meg az osztály nevét: ")

        self.iskola.add_osztaly(Osztaly(nev))

    def add_tanar_to_osztaly(self):
        nev = input("Add meg a tanár nevét: ")

        eletkor = self.get_integer_input("Add meg a tanár életkorát: ")
        tantargy = input("Add meg a tanár tantárgyát: ")
        osztaly = self.find_osztaly()

        if osztaly:
            tanar = Tanar(nev, eletkor, tantargy)
            osztaly.add_tanar(tanar)
            print(f"{nev} tanár hozzáadva az {osztaly.nev} osztályhoz.")
        else:
            print("Az osztály nem található!")

    def add_diak_to_osztaly(self):
        nev = input("Add meg a diák nevét: ")

        eletkor = self.get_integer_input("Add meg a diák életkorát: ")
        osztaly = self.find_osztaly()

        if osztaly:
            diak = Diak(nev, eletkor)

            print("Osztályzatok hozzáadása (0 a befejezéshez):")
            while True:
                grade = self.get_integer_input("Adj osztályzatot: ", allow_zero=True)
                if grade == 0:
                    break
                diak.add_grade(grade)

            osztaly.add_diak(diak)
            print(f"{nev} diák hozzáadva az {osztaly.nev} osztályhoz.")
        else:
            print("Az osztály nem található!")

    def show_iskola_info(self):
        self.iskola.iskola_info()

    def find_osztaly(self):
        osztaly_nev = input("Add meg az osztály nevét: ")
        return next((o for o in self.iskola.osztalyok if o.nev == osztaly_nev), None)

    @staticmethod
    def get_integer_input(prompt, allow_zero=False):
        while True:
            try:
                value = int(input(prompt))
                if allow_zero or value > 0:
                    return value
                print("Az érték nem lehet negatív vagy nulla!")
            except ValueError:
                print("Helytelen érték! Adj meg egy számot.")