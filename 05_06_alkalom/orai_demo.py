""" OOP kezdet """
class ListaOsszefuggesek:
    def __init__(self):
        self.custom_list = []
        self.index = 0

    def lista_kiirasa(self):
        print(self.custom_list)


lof = ListaOsszefuggesek() # példány
lof.lista_kiirasa() # osztályhoz tartozó függvény -> művelet
lof_index = lof.index

lof_other = ListaOsszefuggesek() # másik példány
lof.lista_kiirasa() #

lof_other_index = lof_other.index + 1
""" OOP vége """


"""

I. feladat

A program bekér egy szöveget és a választásod alapján
kiír ezt-azt a szövegről. Üres szövegre leáll.
Olvassunk be egy szöveget.

Kérdezzük meg a felhasználót, hogy mit szeretne:
a) Kiírjuk hány 'a' betű van a szövegben
b) Kiírjuk a szöveg hosszát
c) Kiírjuk a szöveg nagybetűs változatát

Addig ismételjük a fentebb írtakat,
amíg üres szöveget nem ad meg a felhasználó.
Mind a három feladatot (a, b, c)
saját külön függvényekkel oldjunk meg.
"""

def elso_feladat():
    def count_char_a(input_text):
        print('A szövegben ennyi "a" betű van:', input_text.count('a'))

    def text_len(input_text):
        print('A szöveg hossza: ', len(input_text))

    def text_to_upper(input_text):
        print('A nagybetűs verizó: ', input_text.upper())

    print('\nA program bekér egy szöveget és a választásod alapján kiír ezt-azt a szövegről. Üres szövegre leáll.')

    text = input('\nAdj meg egy tetszőleges szöveget: ')

    while text != '':
        print('Válassz:')
        print('a) Kiírjuk hány "a" betű van a text-ben')
        print('b) A szöveg hossza')
        print('c) A szöveg nagy betűs változata')

        select = input('Válassz [a,b,c]: ').lower()

        if select == 'a':
            count_char_a(text)
        elif select == 'b':
            text_len(text)
        elif select == 'c':
            text_to_upper(text)

        text = input('\nAdj meg egy tetszőleges szöveget: ')

    print("Viszlát!")


# elso_feladat()



"""

II. Feladat

Egy kör sugarát kérjük be és kiírjuk a
kerületét cm-ben és a területét cm²-ben.
Kérjük be a felhasználótól egy kör sugarát, cm-ben értve.

Feltételezhetjük, hogy a felhasználó valóban
számot ad meg, de az lehet tört szám is.
Írj két saját függvényt a kör
adatainak a kiszámításához.

Az egyik függvény neve 'kerulet' legyen,
bemenő paramétere a kör sugara cm-ben.
A függvény számolja ki a kör kerületét és
írja is ki az eredményt a konzolra a minta szerint, cm-ben.

A másik függvény neve 'terulet' legyen,
bemenő paramétere a kör sugara cm-ben.
A függvény számolja ki a kör területét és
adja vissza az eredményt.
A szöveges, minta szerinti cm²-ben számolt
kiírást a főprogramban hajtsuk végre.
Az eredményeket mindkét esetben 2 tizedesre kerekítsük.

"""

def masodik_feladat():
    from math import pi

    def kerulet(r):
        ker = round(2 * r * pi, 2)
        print(f'a kör kerüelte {ker} cm')

    def terulet(r):
        return round(r * r * pi, 2)

    print('\nEgy kör sugarát kérjük be és kiírjuk a kerület területét cm^2-ben')

    sugar = float(input("Add meg a kör sugarát cm-ben: "))

    kerulet(sugar)
    print(f'A kör területe {terulet(sugar)} cm^2')


# masodik_feladat()



"""

III. feladat

Beolvasunk 5 egész számot és e
listárólírunk ki információkat.
Mindegyik alábbi feladathoz készítsünk saját függvényt.
A 2. feladattól kezdve a függvények bemenő
paramétere a lista, visszatérési értékük
pedig a kiíratandó teljes szöveges válasz a kérdésre.

1. Olvassunk be öt egész számot egy listába.
Feltételezhetjük, hogy a felhasználó
valóban csak egész számokat ad meg.

2. Írjuk ki a lista elemeit egy sorban,
kötőjellel elválasztva, abban a sorrendben,
ahogy azt a felhasználó megadta.

3. Írjuk ki a lista elemeit fordított sorrendben,
egy sorban, kötőjellel elválasztva.

4. Írjuk ki, hányadik elem a legkisebb és mennyi az.

5. Írjuk ki, hányadik elem a legnagyobb és mennyi az.

6. Írjuk ki melyik elem áll a legközelebb
a teljes lista átlagához és hogy az hányadik elem.

"""

def harmadik_feladat():
    MAX_COUNT = 5               # user ezt kérte.... ne kérdezd mé...

    def szamok_beolvasni(number_count):
        data = []
        for i in range(number_count):
            new_item = int(input('Adj meg egész számot: '))
            data.append(new_item)

        return data

    def lista_kiirasa_kotojellel(custom_list):
        result = str(custom_list[0])
        for i in range(1, len(custom_list)):
            result += f'-{custom_list[i]}'

        return result

    def forditott_lista(custom_list):
        new_list = custom_list.copy()
        new_list.reverse()

        result = lista_kiirasa_kotojellel(new_list)

        return f'A fordított sorrend: {result}'

    def legkisebb_elem_indexxel(custom_list):
        min_idx = 0

        idx = 0
        for i in custom_list[1:]:
            idx += 1
            if i < custom_list[min_idx]:
                min_idx = idx

        return f'A legkisebb elem: {custom_list[min_idx]}, amelynek az indexe: {min_idx}'


    def legnagyobb_elem_indexxel(custom_list):
        max_idx = 0

        idx = 0
        for i in custom_list[1:]:
            idx += 1
            if i > custom_list[max_idx]:
                max_idx = idx

        return f'A legnagyobb elem: {custom_list[max_idx]}, amelynek az indexe: {max_idx}'

    def atlagoz_legkozelebbi(custom_list):
        avarage = sum(custom_list) / len(custom_list)
        avg_idx = 0

        idx = 0
        for i in custom_list[1:]:
            idx += 1

            if abs(avarage - i) < abs(avarage - custom_list[avg_idx]):
                avg_idx = idx

        return f'Az átlaghoz legközelebbi elem: {custom_list[avg_idx]}, amelynek az indexe: {avg_idx}'

    # naming: FE résznek...

    print(f'\nbeolvasunk {max_count} egész számot és erről a listáról írunk ki információkat')

    num_list = szamok_beolvasni(MAX_COUNT)

    # 1.
    print(lista_kiirasa_kotojellel(num_list))

    # 2.
    print(forditott_lista(num_list))

    # 3.
    print(legkisebb_elem_indexxel(num_list))

    # 4.
    print(legnagyobb_elem_indexxel(num_list))

    # 5.
    print(atlagoz_legkozelebbi(num_list))


def harmadik_feladat_alter():
    def beolvas():
        lista = []
        for i in range(5):
            szam = int(input(f'kréem az {i+1} számot'))
            lista.append(szam)
        return lista

    def eredeti_lista_kotojelle(lista):
        return '-'.join(map(str, lista))

    def forditot_lista(lista):
        return '-'.join(map(str, lista[::-1]))

    def legkisebb_elem(lista):
        legkisebb = min(lista)
        index = lista.index(legkisebb)
        return f'a legkisebb elem {index} érték: {legkisebb}'

    def legnagyobb_elem(lista):
        legnagyobb = max(lista)
        index = lista.index(legnagyobb)
        return f'legnagyobb elem  indexe {index} value: {legnagyobb} '

    def legkozelebbi_atlagoz(lista):
        atlag = sum(lista) / len(lista)
        legkozelebbi = min(lista, key=lambda x: abs(x - atlag))
        index = lista.index(legkozelebbi)

        return f'legközelebbi álló elem az átlagohoz {index} érétke {legkozelebbi}'

"""

IV. Feladat

Egy pozitív egész számot alakítunk bináris számmá.
Olvassunk be egy pozitív egész számot
és írjuk ki a bináris alakját.

A beépített bin() függvényt nem használhatod!

Ehhez készítsünk egy dec_bin() függvényt,
amelynek van egy bemenő paramétere és
sztringesen adja vissza a bináris értékét.

A felhasználó biztosan egész számot ad meg,
azt nem kell ellenőrizni.

A program kommunikációját a
mintának megfelelően alakítsd.

"""

def negyedik_feladat():
    def dec_bin(dec):
        bin = ''

        while dec > 0:
            bin = str(dec % 2) + bin
            dec = dec // 2

        return bin

    szam = int(input("adj meg egy számot "))
    print(f'{szam} binárisan: {dec_bin(szam)}')


# negyedik_feladat()

""" önálló lehetséges feladat """

"""

V. feladat

Összegeket kerekítünk.
Kérj be a felhasználótól egy összeget.
Biztosak lehetünk benne, hogy pozitív
egész számot ad meg, azt nem kell ellenőrizni.

Az összeget kerekítsd lefelé százasokra és írd ki,
majd ugyanezt százasra felfelé kerekítéssel is tedd meg.

Ha a megadott összeg százzal osztható,
akkor a két érték természetesen azonos.
A kerekítésekhez írj saját függvényeket kerek_fel()
és kerek_le() néven.

Mindkét függvénynek egy bemenő paramtere van,
egy egész szám, és a visszatérési érték
a kerekített érték.
A program kommunikációját a mintának
megfelelően szövegezd.

"""


"""

VI. feladat

A program induláskor kérjen be egy nevet
és egy születési évszámot, majd írja ki
hány keresztneve van az illetőnek,
és 2030-ban hányadik születésnapja lesz.

A kor meghatározásához hozz létre egy függvényt,
kor2030 néven, ami a paraméterként kapott
évszám alapján kiszámolja a 2030-ban betöltött kort!

A függvény csak adja visszatérési értékül
a számítás eredményét, de a képernyőre ne írja ki!

Amíg a felhasználó kéri, kérje a következő nevet.

A program kommunikációját a mintának
megfelelően szövegezd.

Abban biztosak lehetünk, hogy a felhasználó
egy-egy szóközzel választja csak el a
szavakat és a születési évszámot.

"""


import random

mylist = ["apple", "banana", "cherry"]

# print(random.choice(mylist))

def bemutatkozas(nev, kor):
    print(f'nevem {nev} és {kor} éves vagyok')


# bemutatkozas("Anna", 25)
# bemutatkozas(kor=25, nev="anna")
# bemutatkozas(nev="teszt elek", kor=66)

def koszont(nev, udvozles="Szia"):
    print(f'{udvozles}, {nev}!')

# koszont("Péter")
# koszont("Péter", "csá")
# koszont(udvozles="sziaheló", nev="teszt elek")

def rendeles_vegosszeg(termek, darab=1, ar=1000, kedvezmeny=0):
    return darab * ar * (1 - kedvezmeny / 100)

# print(rendeles_vegosszeg("laptop", 2, kedvezmeny=10))
# print(rendeles_vegosszeg("telefon", darab=3, ar=800))

"""


TANULOK = [
    {"nev": "Teszt Elek", "osztaly": "13I", "eletkor": 19},
    {"nev": "Kiss Béla", "osztaly": "12A", "eletkor": 18},
    {"nev": "Nagy Anna", "osztaly": "11B", "eletkor": 17},
    {"nev": "Szabó Gergő", "osztaly": "10C", "eletkor": 16},
    {"nev": "Varga László", "osztaly": "9D", "eletkor": 15},
    {"nev": "Tóth Zsófia", "osztaly": "12A", "eletkor": 18}
]

"""

TANULOK = [
    {"nev": "Teszt Elek", "osztaly": "13I", "eletkor": 19},
    {"nev": "Kiss Béla", "osztaly": "12A", "eletkor": 18},
    {"nev": "Nagy Anna", "osztaly": "11B", "eletkor": 17},
    {"nev": "Szabó Gergő", "osztaly": "10C", "eletkor": 16},
    {"nev": "Varga László", "osztaly": "9D", "eletkor": 15},
    {"nev": "Tóth Zsófia", "osztaly": "12A", "eletkor": 18}
]

""" a tanulók adatinak frissítése """
def frissit_tanulo(tanulok, nev, uj_kor=None, uj_osztaly=None):
    for tanulo in tanulok:
        if tanulo["nev"] == nev:
            if uj_kor is not None:
                tanulo["eletkor"] = uj_kor
            if uj_osztaly is not None:
                tanulo["osztaly"] = uj_osztaly
            break

frissit_tanulo(TANULOK, "Kiss Béla", uj_kor=19, uj_osztaly="13A")
# print("frisített lista:", TANULOK)

def torol_tanulo(tanulok, nev):
    for i, tanulo in enumerate(tanulok):
        if tanulo["nev"] == nev:
            del tanulok[i]
            return True
    return False

torol_tanulo(TANULOK, "Teszt Elek")
# print("törlés után", TANULOK)

# print(TANULOK[0].get("neeeev"))



suti = {"nev": "dobostorta", "szeletek": 12, "elfogyott": False}
#print(suti["nev"])
#print(suti.get("nev"))

# bejárás
for kulcs, ertek in suti.items():
    #print(kulcs, "értéke:", ertek)
    pass


my_dict = {
    1: "alma",
    2: "körte",
    3: "szilva",
    12: "alma",
    23: "körte",
    32: "szilva",
    41: "alma",
    42: "körte",
    34: "szilva"
}

# {'alma': [1, 12, 41] .... }

csoportok = {}
for kulcs, ertek in my_dict.items():
    csoportok[ertek] = csoportok.get(ertek, []) + [kulcs]

# print(csoportok)


# args-nak szokás hívni : *tobbi = *args
def legkisebb(elso, *tobbi): # arg -> argumentum (1db) -> args -> (n db)
    acc = elso
    print(type(tobbi))

    for x in tobbi:
        if x < acc:
            acc = x
    return acc

print(legkisebb(3,4,2,-8,65,54,-10,4)) # ........ n

#########################
"""                     #
II. rész :)
"""
#########################


try:
    szam = int(input("adj meg egy számot"))
    print(f'szám négyzete {szam ** 2}')
except Exception as e:
    print(e)
    print("nem szám")

try:
    oszto = int(input("mennyivel osszam a 10-et"))
    print(f'az eredmény: {10 / oszto}')
except ZeroDivisionError as e:
    print(f'hiba {e} nullával nem lehet osztani')
except ValueError as e:
    print("ez nem szám")
finally:
    print("ez mindig lefut...")



try:
    oszto = int(input("mennyivel osszam a 10-et"))
    print(f'az eredmény: {10 / oszto}')
except (ZeroDivisionError, ValueError) as e:
    print(f'hiba {e}')
finally:
    print("proginak vége")
