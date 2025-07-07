"""

Írj egy sorozat nevű függvényt, amely egy számokból álló listát kap paraméterül!
A függvény döntse el, hogy a listában szereplő számok
számtani, illetve mértani sorozatot alkotnak-e!

Kezeld le azt az esetet, amikor a függvény paraméterében
érkező lista 3-nál kevesebb elemet tartalmaz!

Ekkor a visszatérési érték a HIBA! szöveg legyen!
Ezeket a hibas_eset.txt –ben tárold el.

Egyéb hibakezeléssel is kell foglalkoznod amennyiben a program ezt igényli.

"""

def is_error_in_file(lista, file_name="hibas_eset.txt"):
    """ hibásadatok gyűjtése txt-be, boolean -> isValami()... -> t / f """

    minimum_list_len = 3

    try:
        if len(lista) < minimum_list_len:
            with open(file_name, 'w', encoding='utf-8') as hibas_fajl:
                hibas_fajl.write("HIBA!")
                return True
    except (IOError, Exception) as e:
        print(f'Hiba történt a fájl írása közben: {e}')
        return True

    return False

def is_szamtani_sorozat(lista):
    """ számtani sorozat-e """

    try:
        diff = lista[1] - lista[0]
        for i in range(1, len(lista) - 1):
            if lista[i+1] - lista[i] != diff:
                return False
    except (TypeError, Exception) as e:
        print(f'Hiba: {e}')
        return False

    return True

def is_mertani_sorozat(lista):
    """ mértani sorozat-e """

    try:
        if lista[0] == 0:
            return False

        ratio = lista[1] / lista[0]
        for i in range(1, len(lista) - 1):
            if lista[i] == 0 or lista[i + 1] / lista[i] != ratio:
                return False

        return True
    except (ZeroDivisionError, Exception) as e:
        print(f'Hiba: {e}')
        return False

def sorozat(lista):
    """ sorozatok meghívásásnak az ellenőrzése """

    if is_error_in_file(lista):
        return "HIBA"

    if is_szamtani_sorozat(lista):
        return "Számtani sorozat"
    elif is_mertani_sorozat(lista):
        return "Mértani sorozat"
    else:
        return "Nem sorozat"

def main():
    sorozat_eredmeny = sorozat([2, 4 ,6, 8]) # számtani

    sorozat_eredmeny_ = sorozat([16, 8, 4, 2, 1]) # mértani

    sorozat_eredmenytelen = sorozat([2, 4, 6, "?"]) # nem sorozat

    sorozat_eredmenytelen_ = sorozat([2, 3, 67, 120]) # nem sorozat

    print(sorozat_eredmenytelen_)


main()