def buborek_rendezes(t):
    """ 
    Buborékos rendezés:
    Egymás melletti elemeket hasonlít össze, és ha rossz sorrendben vannak, felcseréli őket.
    Minden körben a legnagyobb elem "felúszik" a végére.
    """
    n = len(t)

    for i in range(n - 1, 0, -1):  # Külső ciklus: a lista hátralévő (rendezetlen) részét kezeli
        for j in range(0, i):  # Belső ciklus: egymás melletti elemeket hasonlít össze
            if t[j] > t[j + 1]:
                tmp = t[j + 1]
                t[j + 1] = t[j]
                t[j] = tmp

    print(t)


def rendezes_cserevel(t):
    """
    Rendezés cserékkel:
    Minden elemhez (i) végignézi a nála későbbi elemeket (j), 
    és ha talál kisebbet, akkor cserél. 
    Egyszerű, de nem hatékony megoldás.
    """
    n = len(t)

    for i in range(0, n - 1):  # Külső ciklus: aktuális elem (i)
        for j in range(i + 1, n):  # Belső ciklus: összehasonlítás a hátralévő elemekkel (j)
            if t[i] > t[j]:
                tmp = t[i]
                t[i] = t[j]
                t[j] = tmp

    print(t)


def max_kivalasztas_rendezes(t):
    """
    Maximum kiválasztásos rendezés:
    A lista végéről indulva minden körben megkeresi a maximumot 
    a rendezetlen részben, majd kicseréli az aktuális pozícióval.
    """
    n = len(t)

    for i in range(n - 1, -1, -1):  # Külső ciklus: aktuális végpozíció
        max_index = i
        for j in range(0, i):  # Belső ciklus: maximum keresése a rendezetlen részben
            if t[j] > t[max_index]:
                max_index = j
        tmp = t[i]
        t[i] = t[max_index]
        t[max_index] = tmp

    print(t)


def min_kivalasztas_rendezes(t):
    """
    Minimum kiválasztásos rendezés:
    Balról jobbra haladva minden lépésben megkeresi a legkisebb elemet 
    a rendezetlen részből, majd kicseréli az aktuális pozícióval.
    """
    n = len(t)

    for i in range(0, n - 1):  # Külső ciklus: aktuális kezdőpozíció
        min_index = i
        for j in range(i + 1, n):  # Belső ciklus: minimum keresése a hátralévő részből
            if t[j] < t[min_index]:
                min_index = j
        if min_index != i:
            tmp = t[i]
            t[i] = t[min_index]
            t[min_index] = tmp

    print(t)


def rendezes_beszurasssal(t):
    """
    Beszúrásos rendezés:
    Balról jobbra haladva minden elemet a helyére szúr be 
    az előzőleg már rendezett részbe.
    Hatékony kis listák esetén.
    """
    n = len(t)

    for i in range(0, n):  # Külső ciklus: aktuális elem, amit be kell szúrni a helyére
        kulcs = t[i]
        j = i - 1
        while j >= 0 and t[j] > kulcs:  # Belső ciklus: a kulcs helyének megkeresése visszafelé
            t[j + 1] = t[j]
            j -= 1
        t[j + 1] = kulcs

    print(t)


def shell_rendezes(t):
    """
    Shell-rendezés:
    A beszúrásos rendezés általánosítása, amely kezdetben 
    távolabbi elemeket hasonlít össze és mozgat, csökkentve az "ugrásokat".
    A lépések (gap) egyre kisebbek, végül beszúrásos rendezés lesz belőle.
    """
    h = [5, 3, 1]
    n = len(t)

    for k in range(0, 3):  # Ciklus a lépésközökön (gap)
        lepes = h[k]
        for j in range(lepes, n):  # Beszúrásos rendezés módosított változata adott lépésközzel
            i = j - lepes
            kulcs = t[j]
            while i >= 0 and t[i] > kulcs:  # Belső ciklus: elemek tologatása lépésközzel visszafelé
                t[i + lepes] = t[i]
                i -= lepes
            t[i + lepes] = kulcs

    print(t)


def gyors_rendezes(t):
    """
    Gyorsrendezés (QuickSort):
    Egy kiválasztott pivot érték alapján a listát három részre bontja: 
    kisebbek, egyenlők és nagyobbak. Ezeket rekurzívan rendezi.
    Nagyon hatékony, de nem stabil rendezés.
    """
    n = len(t)

    if n <= 1:  # Alapeset: üres vagy egyelemű lista már rendezett
        return t

    kicsik = []
    egyenlo = []
    nagyok = []
    pivot = t[n-1]  # Utolsó elemet választja pivotnak

    for num in t:  # Ciklus: szétválogatás a pivot alapján
        if num < pivot:
            kicsik.append(num)
        if num == pivot:
            egyenlo.append(num)
        if num > pivot:
            nagyok.append(num)

    return gyors_rendezes(kicsik) + egyenlo + gyors_rendezes(nagyok)  # Rekurzív rendezés



def main():
    lista = [5, 2, 9, 1, 5, 6]

    buborek_rendezes(lista.copy())
    rendezes_cserevel(lista.copy())
    max_kivalasztas_rendezes(lista.copy())
    min_kivalasztas_rendezes(lista.copy())
    rendezes_beszurasssal(lista.copy())
    shell_rendezes(lista.copy())
    print(gyors_rendezes(lista.copy()))


main()