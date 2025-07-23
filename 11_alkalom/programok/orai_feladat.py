import json
import os

def json_beolvasas(fajlnev):
    with open(fajlnev, "r", encoding='utf-8') as f:
        return json.load(f)

def json_kiir(fajlnev, adat):
    with open(fajlnev, "w", encoding='utf-8') as f:
        json.dump(adat, f, indent=4)

def elso_feladat():
    fajlnev = "jsons/adat.json"
    adat = {"név": "Anna", "kor": 25, "város": "Budapest"}

    json_kiir(fajlnev, adat)
    betoltott_adat = json_beolvasas(fajlnev)

    print(f'betoltott adat: {betoltott_adat}')

def masodik_feladat():
    fajlnev = "jsons/adat.json"

    adat = json_beolvasas(fajlnev)
    adat["orszag"] = "Magyarország"
    json_kiir(fajlnev, adat)

    print("modify data:", adat)

def harmadik_feladat():
    fajlnev = "jsons/szamok.json"

    szamok = json_beolvasas(fajlnev)
    szamok.sort()
    json_kiir(fajlnev, szamok)

    print(f'rendezett számsor:', szamok)

def negyedik_feladat():
    szamok = json_beolvasas("jsons/szamok.json")

    print("max", max(szamok))
    print("min", min(szamok))

def otodik_feladat():
    pontszamok = json_beolvasas("jsons/pontszamok.json")

    osszeg = sum(pontszamok)
    atlag = osszeg / len(pontszamok)

    print(f'összeg: {osszeg}, átlag: {atlag}')

def hatodik_feladt():
    fajl_ut = "jsons/alap.json"

    if not os.path.exists(fajl_ut):
        alap_adat = {"msg": "alap msg"}
        json_kiir(fajl_ut, alap_adat)
        print("alap létrehozva a file-ban")
    else:
        adat = json_beolvasas(fajl_ut)
        print(adat)

def hetedik_feladat():
    try:
        adat = json_beolvasas("jsons/hibas_json.json")
        print(adat)
    except json.JSONDecodeError as e:
        print(f'hibás adat: {e}')

def nyolcadik_feladat():
    felhasznalok = json_beolvasas("jsons/felhasznalok.json")

    szurt_adatok = [felh for felh in felhasznalok if felh["kor"] > 30]
    print(szurt_adatok)

def kilencedik_feladat():
    fajl_txt = "jsons/szavak_50.txt"
    fajl_json = "jsons/szavak.json"

    with open(fajl_txt, "r", encoding='utf-8') as file:
        szavak = [sor.strip() for sor in file.readlines()]

    json_kiir(fajl_json, szavak)
    print(szavak)

def tizedik_feladat():
    fajl_ut = "jsons/pontszamok.json"

    try:
        pontszamok = json_beolvasas(fajl_ut)
        print("legmagasabb pontszámok", max(pontszamok))
        print("legalacsonyabb pontszámok", min(pontszamok))
        print("átlag", sum(pontszamok / len(pontszamok)))
    except FileNotFoundError:
        alap_pontszamok = [0, 0, 0]
        json_kiir(fajl_ut, alap_pontszamok)
        print("nem létezett a fájl, de ezé létrehoztam", alap_pontszamok)

def tizenegyedik_feladat():
    fajlnev = "jsons/dolgozok.json"
    dolgozok = json_beolvasas(fajlnev)
    json_kiir(fajlnev, dolgozok)

    dolgozok.sort(key=lambda d: d["fizetes"])

    legkisebb = dolgozok[0]
    legnagyobb = dolgozok[-1]

    print("legkisebb fizu", legkisebb["nev"], "-", legnagyobb["fizetes"], "Ft")

    osszeg_fizetes = sum(d["fizetes"] for d in dolgozok)
    atlag = osszeg_fizetes / len(dolgozok)

    print(f"atlagfizetes {round(atlag):,} Ft".replace(", ", " "))
    