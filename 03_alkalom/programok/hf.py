
def szamjegyek_osszege():
    szam = input("Adj meg egész számot: ")
    osszeg = 0

    for karakter in szam:
        if karakter.isdigit():
            osszeg += int(karakter)
    print(f'számjegyek összege: {osszeg}')

# szamjegyek_osszege()

def leggyakoribb_szam():
    print("adj meg egy számot (enter kilépés): ")
    szamok = []

    while True:
        adat = input()
        if adat == "":
            break
        if adat.isdigit() or (adat.startswith('-') and adat[1:].isdigit()):
            szamok.append(int(adat))

    if not szamok:
        print("nem adtál meg semmit")
        return

    legtobbszor = None
    max_db = 0
    for szam in szamok:
        db = szamok.count(szam)
        if db > max_db:
            max_db = db
            legtobbszor = szam

    print(f'leggyakoribb szám: {legtobbszor} | {max_db} alkalommal')

# leggyakoribb_szam()