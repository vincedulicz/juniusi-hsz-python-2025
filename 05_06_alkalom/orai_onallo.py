
def lista_letrehozasa():
    """ Létrehozza a listát a megadott szabályok szerint """
    result = []
    for i in range(1, 43):
        if i % 5 != 0:
            if i % 2 == 0:
                result.append(i * 3)
            else:
                result.append(i * 5 / 2)
    # return result

    return [
        (i * 3 if i % 2 == 0 else i * 5 / 2) for i in range(1, 43) if i % 5 != 0
    ]

def lista_kiirasa(lista, uzenet='Lista:'):
    """ KIiírja a lista tartalmát adott üzenettel """
    print(f'{uzenet} {lista}')

def elem_beszurasa(lista):
    """ Bekér egy kétjegyű számot a usertől és beszúrja a lista 2. helyére """
    szam = int(input('Adj meg egy kétjegyű számot: '))
    lista.insert(1, szam)

def elem_torlese(lista):
    """ Bekér egy elemet amit töröl a listából """
    torlendo = float(input("melyik elemet szeretné törölni"))
    lista.remove(torlendo)

def lista_rendezese(lista):
    """ rendezi a listát növekvő sorrendben """
    lista.sort()

def lista_megforditasa(lista):
    """ megfordítja a listát """
    lista.reverse()

def main_elso_feladat():
    lista = lista_letrehozasa()
    lista_kiirasa(lista, "Eredeti lista")

    elem_beszurasa(lista)
    lista_kiirasa(lista, "módosított lista")

    elem_torlese(lista)
    lista_kiirasa(lista, "törlés után")

    lista_rendezese(lista)
    lista_kiirasa(lista, "rendezett lista")

    lista_megforditasa(lista)
    lista_kiirasa(lista, "fordított sorrendű lista")

# main_elso_feladat()

# Alap adatok
TANULOK = [
    {"nev": "Teszt Elek", "osztaly": "13I", "eletkor": 19},
    {"nev": "Kiss Béla", "osztaly": "12A", "eletkor": 18},
    {"nev": "Nagy Anna", "osztaly": "11B", "eletkor": 17},
    {"nev": "Szabó Gergő", "osztaly": "10C", "eletkor": 16},
    {"nev": "Varga László", "osztaly": "9D", "eletkor": 15},
    {"nev": "Tóth Zsófia", "osztaly": "12A", "eletkor": 18}
]

OSZTALYOK = ["9A", "10B", "11C", "12D", "13I"]

import random

def get_tanulo_ertek_by_nev(nev):
    """ tanuló összes adat """
    return next(tanulo for tanulo in TANULOK if tanulo["nev"] == nev)

def kiir_tanulok():
    """ kiírja a tanulóakat formázottan """
    print("a jelenlegi tagok")

    # for
    for index, tanulo in enumerate(TANULOK, start=1):
        print(f'{index}. {tanulo["nev"]} {tanulo["eletkor"]} éves és a {tanulo["osztaly"]} osztályba jár.')

    # comp
    #   [print(f'{index}. {tanulo["nev"]} {tanulo["eletkor"]} éves és a {tanulo["osztaly"]} osztályba jár.') for index, tanulo in enumerate(TANULOK, start=1)]

def uj_tanulo():
    """ új tanuló hozzáadása a listához """
    nev = input("add meg az új tag nevét: ")
    eletkor = int(input("add meg az életkort: "))

    osztaly = random.choice(OSZTALYOK)

    TANULOK.append({"nev": nev, "osztaly": osztaly, "eletkor": eletkor})

    print(f'Új tag hozzáadva: {nev}, {eletkor} éves, {osztaly} osztály')

def tanulo_torlese():
    """ tanuló törlése a listából """
    nev = input("add meg a törlendő tag nevét: ")
    talalat = get_tanulo_ertek_by_nev(nev)
    print(talalat)

    if talalat:
        megerosites = input("Biztosan ki akarod törölni? (I/N): ")
        if megerosites.lower() == "i":
            TANULOK.remove(talalat)
            print(f'{nev} törölve lett a listából')
        else:
            print("törlés visszavonva")
    else:
        print("nem található ilyen nevű tag")

def tanulo_modositasa():
    nev = input("add meg a módosítani kívánt tag nevét: ")

    talalat = get_tanulo_ertek_by_nev(nev)
    if talalat:
        kulcs = input("melyik adatot szeretnéd módosítani? (nev, osztaly, eletkor): ")

        if kulcs in talalat:
            uj_ertek = input(f'add meg az új értéket a(z) {kulcs} mezőhöz')

            if kulcs == "eletkor":
                uj_ertek = int(uj_ertek)

            talalat[kulcs] = uj_ertek

            print(f'{nev} {kulcs} értéke módosítva lett: {uj_ertek}')
        else:
            print("érvénytelen kulcs")
    else:
        print("nem található ilyen nevű tag")

def main():
    while True:
        print(
            "Az alábbi parancsokat használhatod:"
            "\nÚj tag - newmem | Törlés - delete | Módosítás - modify | Kilépés - end, Q, quit"
        )

        kiir_tanulok()

        parancs = input("mit szeretné' csinálni: ").strip().lower()
        if parancs in ["q", "end", "quit"]:
            print("a program leeáll")
            break
        elif parancs == "newmem":
            uj_tanulo()
        elif parancs == "delete":
            tanulo_torlese()
        elif parancs == "modify":
            tanulo_modositasa()
        else:
            print("érvénytelen parancs, próbálj újra...")

main()