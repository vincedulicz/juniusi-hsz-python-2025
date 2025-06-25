def szokoz_nelkul():
    """
    Ez egy olyan függvény ami
    kiszedi a szóközöket!
    """
    szoveg = "H e l l o , v i l á g !"
    spacenelkul = ""

    for i in szoveg:
        if i != ' ':
            spacenelkul += i
    print(spacenelkul)


# szokoz_nelkul()

def palindrom():
    """
    Eldönti egy mondatról, hogy palindrom-e.
    """

    szoveg = "Indul a görög aludni."

    csakbetuk = ""
    for i in szoveg:
        if i.isalnum():
            csakbetuk += i.lower()  # i = A .lower() -> A-a

    print(csakbetuk)

    hibas = False
    index = 0
    hossz = len(csakbetuk)
    while index < hossz / 2:
        if csakbetuk[index] != csakbetuk[hossz - 1 - index]:
            hibas = True
            break
        index += 1

    if hibas:
        print("A megadott szó nem palindrom.")
    else:
        print("A megadott szó palindrom.")

    print(csakbetuk)

    if csakbetuk != csakbetuk[::-1]:
        print("XXX A megadott szó nem palindrom.")
    else:
        print("XXX A megadott szó palindrom.")


# palindrom()


def paros_e_jo():
    szam = 3
    return szam % 2 == 0  # true v false -> 1,


def paros_e_teszt():
    if paros_e_jo():
        print("páros")
    else:
        print("páratlan")


def paros_e_rossz():
    szam = 3

    print(szam % 2 == 0)

    if szam % 2 == 0:
        print("páros")
    else:
        print("páratlan")


def alap_operatorok():
    a = 4
    b = 3

    eredmeny = "eredmény"
    eredmeny_ = "eredmény_"

    if eredmeny == eredmeny_:
        print("stringek megegyeznek")
    elif eredmeny != eredmeny_:  # not == ...
        print("nem egyeznek")
    else:
        print("valami más")

    if a > b:
        print("a > b")
    elif b > a:
        print("b > a")
    elif b == a:
        print("a == b")
    else:
        print("más...")


def print_olvashatosaga():
    i = 0
    szo = "python"

    print("A szó " + str(i) + ". betűje: " + szo[i] + ".")  # olvashatatlan

    print("A szó ", str(i), ". betűje", szo[i], ".", sep="")  # kicsivel szebb...

    formazott = f'A szó {i}. betűje: {szo[i]}'

    print(formazott)


# print_olvashatosaga()


def osszeadas():
    """ str összefűzés """
    egyik = input("Írj bele szöveget: ")
    masik = input("Írj bele mégegyszöveget!: ")

    print("egyik+masik->")
    print(egyik + masik)


# osszeadas() # összefűzés


def szamok_osszeadasa():
    egyik = int(input("szam1: "))
    masik = int(input("szam2: "))

    print(egyik + masik)


# szamok_osszeadasa()


def szakasz_hossz_koordinata():
    """
    Írjunk programot, amely a user-től bekéri két síkblei
    pont x és y koordinátit és kíírja a közéjük húzott egyenes
    szakasz hosszát! (Pitagorasz tétel)
    """

    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))

    import math
    hossz = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    print(hossz)


# szakasz_hossz_koordinata()


def is_operator():
    a = [1, 2, 3]
    b = list(a)

    print(f'a: {a} | b: {b}')

    print("a == b", a == b)
    print("a is b", a is b) # ?

    b.append(4)
    b.remove(1)

    print(a)
    print(b)

# is_operator()

def is_operator_():
    x = [1, 2, 3] # -> 0xef8334.....
    y = [1, 2, 3] # -> 0x333443.....

    x = y # -> y -> 0x33344x = x.ref(0xef8334).... -> ugyanott lakik !!!

    print("x == y", x == y)
    print("x is y", x is y)

    y.append(4)
    print(x)

    print(type(x))
    print(type(y))

    print(id(x))
    print(id(y))

# is_operator_()

def referencia_lista():
    def modify_list(lst):
        lst.append(4)
        print(f'Belső lista: {lst}')

    our_list = [1, 2, 3]
    modify_list(our_list)
    print(f"külső lista: {our_list}")


referencia_lista()

def feladatok_pontok():
    """
    A dolgozotatok 0-10 pontosak lehetnek.
    A ?, hogy melyik pontszámból hány darab lett.
    """

    # bemenet: 3, 4, 5 .... 6 .... n+m

    # kimenet:
    # 0p    1 db
    # 1p    5 db
    # 2p    3 db
    # ...
    # 9p    34 db
    # 10p   120 db

    pontok = []
    be = input("Pont? ")

    while be != "":
        pontok.append(int(be))
        be = input("Pont? ")

    print(pontok)

    # O(n^2) -> O(1) v O(n*log n)
    db_max = 0
    for keresett in range(0, 10 + 1):
        db = 0

        for pont in pontok:
            db_max += 1 # hanyszor futott le
            if pont == keresett:
                db += 1

        print(f"{keresett:2} p, {db:2}")

    print(db_max)

# feladatok_pontok()