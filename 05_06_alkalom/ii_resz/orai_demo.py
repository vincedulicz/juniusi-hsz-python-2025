forrasfajl = open('autok_listaja.txt')
for sor in forrasfajl:
    print(sor)

# print
forrasfajl.readline() # 1-es sorok

forrasfajl.readlines() # listával tér vissza az összes elem benne van

forrasfajl.read() # teljes fájltartalom

forrasfajl.close()


# with open


autok = []

with open('autok_listaja.txt', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        auto = {'rendszam': adatok[0], 'típus': adatok[1], 'kor': int(adatok[2])}
        autok.append(auto)

print(f'{autok}')


with open('kimenet.txt', 'w', encoding='utf-8') as celfajl:
    print('ez kerül a fájlba....', file=celfajl)

with open('kimenet.txt', 'w', encoding='utf-8') as celfajl:
    celfajl.write('almafdfdfdfd')

    celfajl.writelines(['alma\n', 'körte\n', 'mézesdió\n'])


import json

with open('diakok.json', 'r', encoding='utf-8') as diakok_adatok:
    adatok = json.load(diakok_adatok) # dict

print(type(adatok))

for diak in adatok['diakok']:
    print(diak.get('név'))
    print(diak)

    if not diak.get('kollegista'):
        print('mér')
    else:
        print("az")