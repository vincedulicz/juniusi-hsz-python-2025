
teszt = 0 # integer -> -2.1 - +2.1
bejovo_szam = 1 # ROSSZ KOMMENT: bejovo_szam

valtozo = None

valtozo = "dede "
text = "ez egy text"

print(valtozo + text)

import keyword # az import mindig a tetejére kerül

print(keyword.kwlist)

a_int = 1
b_float = 1.5
c_complex = 3.14j

print(5 / 2)
print(5 // 2)
print(7 % 2)
print(2 ** 3)

print(type(c_complex))

text = "szöveg" # string
betu = 'k' # string

tomb = ["string", 1, None]
print(len(tomb))
print(tomb[2])

print("...")

print(text[0])
print(text[0:2])
print(text[2:])
print(text[-3:])

print(text[0:-1:2])
print(text[::2])

print(text[::1])
print(text[::-1])
print(text[-1])
print(text[-2])

tomb = [1,2,3,4,5]
i = 0
while i <= 4:
    print(f'érték: {tomb[i]}, típus: {type(tomb[i])} ')
    i += 1


# name = input("Hogy hívnak?")
# print(f'Szia {name}')

# first_num = int(input("első szám: "))
# second_num = int(input("második szám: "))
# print(first_num + second_num)

import math

# print("Mennyi kör sugara")
# sugar = float(input())

# print("Kerület = ", 2 * sugar * math.pi)
# print("Terület = ", sugar ** 2 * math.pi)

# metódus
def paros_e_method(szam): # boolean (1,0) True v False -> 1 soros
    if szam % 2 == 0:
        print("páros")
    else:
        print("páratlan")

# függvény
def paros_e_fuggveny(szam):
    return szam % 2 == 0

if paros_e_fuggveny(5):
    print("varázslat")
else:
    print("mér nem páros")

if not False:
    print("true")
else:
    print("false")


a = 4
b = False # 0
c = True # 1

if a > b:
    print("a > b")
elif b > a:
    print("B nagyobb")
elif b == a:
    print("b = a")
else:
    print("más.....")


lista = ["str2", 2,2,2,2,2, 2j, 3.14, "str2"]
print(lista)
print(lista.append(5))
print(lista)

print(lista.count("str2"))

if __name__ == '__main__':
    main()