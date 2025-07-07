""" I. feladat """

def szokoev(ev):
    return ev % 400 == 0 or (ev % 4 == 0 and ev % 100 != 0)


def evnapja(ev, honap, nap):
    honapok = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    napszam = 0
    i = 0
    while i < honap - 1:
        napszam += honapok[i]
        i += 1

    if szokoev(ev) and honap > 2:
        napszam += 1

    napszam += nap

    return napszam

def main_elso_feladat():
    ev = int(input("Kérem az évet: "))
    honap = int(input("Kérem a hónapot: "))
    nap = int(input("Kérem a napot: "))

    n = evnapja(ev, honap, nap)
    print(f'{ev}.{honap}.{nap}. az én {n}. napja')

""" ii. feladat """

def szoveget_elemez(szoveg):
    eredmeny = {"betu": 0, "szamjegy": 0, "egyeb": 0}

    for karakter in szoveg:
        if karakter.isalpha():
            eredmeny["betu"] += 1
        elif karakter.isdigit():
            eredmeny["szamjegy"] += 1
        else:
            eredmeny["egyeb"] += 1

    return eredmeny

# print(szoveget_elemez(""))

""" iii. feladat """

def kuruskodot_csoportosit(kurzuskodok):
    if kurzuskodok == "":
        return {}

    kurzuskodok_lista = kurzuskodok.split(";")
    eredmeny = {"infos": [], "matekos": [], "szabval": []}

    for kurzuskod in kurzuskodok_lista:
        if kurzuskod.startswith("I"):
            eredmeny["infos"].append(kurzuskod)
        elif kurzuskod.startswith("M"):
            eredmeny["matekos"].append(kurzuskod)
        elif kurzuskod.startswith("X"):
            eredmeny["szabval"].append(kurzuskod)

    return eredmeny

# print(kuruskodot_csoportosit("IB370G;MBNXK114E;MBNXK114G;XA0021-GTK-MM1;IB370E"))


def statisztika(fajlok):
    eredmeny = {}

    for fajl in fajlok:
        kit = fajl.split(".")[-1]
        kit = kit.lower()

        if kit not in eredmeny:
            eredmeny[kit] = 1
        else:
            eredmeny[kit] += 1

    return eredmeny

# print(statisztika(['feladat.py', 'Bolygo.java', 'HELLOFRIENDS.MP4', 'TEST.PY', 'biro.gib.maxpont.py', 'russian-driving-fails.mp4']))