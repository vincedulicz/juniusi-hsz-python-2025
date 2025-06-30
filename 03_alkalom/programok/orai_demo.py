"""
import math

PI = 3.14
MAX_POOL_CONNECTIONS = 42
AGE_LIMIT = 18


age = 5
def test_age(age):
    if age < AGE_LIMIT:
        return False

response = test_age(17)

def kiiro(*args):
    print(*args)

# FrontEnd (FE) -> hálózaton -> False-> response

# FRONTEND
if response:
    load_verify_oldal()
else:
    redirect -> google.com
"""


"""
Egy szám osztói

Alap működés:

Input: 15

Kiemenet:

15 osztói:
1; 3; 5; 15

Input: be szám
Konvertálni kell input
osztok = "1" -> + 3 + 5 + 15 ';'

"""

def szam_osztoi():
    szam = int(input("Írjá be egy egész számot: "))
    osztok = "1"

    n = 2
    while n <= szam // 2:
        if szam % n == 0:
            osztok += "; " + str(n)
        n += 1

    osztok += "; " + str(szam)

    print(str(szam) + " osztói:")
    print(osztok)

"""
Tökéletes számok

-> tökéletes szám akkor érvényesül ha önmagánál kisebb osztói összege megegyezik a számmal.
Pl 6 -> 1,2,3 (+) = 6

Input: 6
Tökéletes szám!

Input: 12
Nem tökéletes szám!

input, típuskonverzió, osztók összege, ha osztója + ha nem -> semmit
if osztok osszege == input_szam -> szám:nemaz

"""
def tokeletes_szam():
    # 2**(p-1)(2p-1), ahol 2**(p-1) és p is prím

    szam = int(input("Írj be egy egész számot: "))
    osztok_osszege = 1

    n = 2
    while n <= szam // 2:
        if szam % n == 0:
            osztok_osszege += n
        n += 1

    if osztok_osszege == szam:
        print("Tökéletes szám")
    else:
        print("Nem az")


def tokeletes_szam_felso_hatar():
    felso_hatar = int(input("Tökéletes szám felső határa: "))

    elso_tokeletes_szam = 6
    while elso_tokeletes_szam <= felso_hatar:
        osztok_osszege = 1

        n = 2
        while n <= elso_tokeletes_szam // 2:
            if elso_tokeletes_szam % n == 0:
                osztok_osszege += n
            n += 1

        if osztok_osszege == elso_tokeletes_szam:
            print(elso_tokeletes_szam)

        elso_tokeletes_szam += 1

"""
String műveletek I.
"""
def string_muveletek():
    szoveg = "6füst Fölt SZALO NA toaaaaa qrmf gval xyz"

    # print(len(szoveg))
    # print(f'0. index {szoveg[0]}') # .[2] [-2] [::2] [::-1]

    print(szoveg[0])
    # szoveg[0] = "k" nem mukszik immut / mut

    print(szoveg.replace("ö", "á"))

    # "q"
    if "füst" not in szoveg:
        print("nincs füst")
    else:
        print("van q")

    print(f'kezdő: {szoveg.startswith("FFfüst")} végző: {szoveg.endswith("FFxyz")}')

    if szoveg.startswith("6"):
        print("számmal kezdődik")
    else:
        print("nem")


def string_muveletek_ii():
    szoveg = "Hello"
    print(szoveg)

    lista = list(enumerate(szoveg))
    print(lista)

    elotag = "Törp"
    utotagok_listaja = ["erős", "költő", "morgó", "oltó"]

    for utotag in utotagok_listaja:
        print(elotag + utotag)

    nevek = ["Teszt Elek", "Mérges Béla", "Fos Olok", "Tűz Ábel"]

    print(nevek[2:4])

    szoveg = "szöveg"
    print(szoveg.find("öv"))

def var_swapping():
    a = 5
    b = 4

    print(f'a: {a} ; b: {b}')

    tmp = a
    a = b
    b = tmp

    print(f'a: {a} ; b: {b}')

    a, b = b, a
    # a b tmp -> memory

    print(f'a: {a} ; b: {b}')


# TODO: Felső határig bekérés ellenőrzés kiírás
def primkereso():
    from math import sqrt

    szam = int(input("Szám: "))

    if szam == 1:
        print("def szerint ez nem prím")
    else:
        is_prim = True

        n = 2
        while n <= sqrt(szam):
            if szam % n == 0:
                is_prim = False

            n += 1

        if is_prim:
            print("prím")
        else:
            print("nem prím")

def main():
    # szam_osztoi()
    # tokeletes_szam()
    # tokeletes_szam_felso_hatar()

    # string_muveletek()
    # string_muveletek_ii()

    var_swapping()

main()
