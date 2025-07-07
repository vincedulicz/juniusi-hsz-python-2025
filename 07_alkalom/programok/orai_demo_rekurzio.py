"""

A hatványozás elvégezhető annál gyorsabban is,
mintha a kitevőnek megfelelő számú szorzást csinálnánk.

Pl. a8 = a4·a4, a4 = a2·a2 és a2 = a·a miatt a nyolcadikra hatványozáshoz
mindössze három szorzásra van szükség.


A következő megfigyelést tehetjük:





Írj rekurzív függvényt, amely a fentiek alapján végzi el a hatványozást!
Paraméterei legyenek az alap és a kitevő, visszatérési értéke pedig a hatvány.
Írd ki kettő első tizenhat hatványát!

A rekurzív függvénybe most se tegyél ciklust, dolgozz a definíció alapján!
Ahhoz, hogy ez működjön, még egy báziskritériumot be kell vezetned,
amit a fenti definíció nem tartalmaz.

Mi lehet az?

"""

"""

A szükséges báziskritérium: ha k == 0, akkor a hatvány értéke 1.

Vagyis annak rögzítése, hogy bármelyik szám 0. hatványa 1.
A rekurzióban közeledünk ehhez a báziskritériumhoz,
mert mindig felezzük a kitevőt, vagy levonunk belőle 1-et.

A k == 1 esetet is vehetnénk báziskritériumnak,
de a k == 0 még jobb, még ha nem is tűnik intuitívnak elsőre.

Így legalább arra is működik a program.
a1 értéke így a * a0 módon számítódik ki.

"""


"""
     ┌
     │ (a·a)k/2, ha k páros
ak = ┤
     │ a·ak-1, ha k páratlan.
     └
"""

def gyorshatvany(a, k):
    if k == 0:
        return 1
    if k % 2 == 0:
        print(f'(pa) if a: {a} : k : {k}')
        return gyorshatvany(a * a, k // 2)
    else:
        print(f'(pá) if a: {a} : k : {k}')
        return a * gyorshatvany(a, k - 1)

def main():
    for k in range(0, 16):
        print(gyorshatvany(2, k))


main()