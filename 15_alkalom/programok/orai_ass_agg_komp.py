import json


class DefaultStandard(object):
    def __init__(self):
        self.publikus_adattag = 0
        self._protected = 1
        self.__privat_adattag = False

ds = DefaultStandard()

class MasikStandard(DefaultStandard):
    pass

ms = MasikStandard()


""" asszociáció """
class Lada:
    def __init__(self, kapacitas):
        self.kapacitas = kapacitas

    def kihasznaltsag_vizsgalo(self, dobozok):
        tomeg = sum([doboz.tomeg for doboz in dobozok])
        return tomeg / self.kapacitas * 100

class Doboz:
    def __init__(self, tomeg):
        self.tomeg = tomeg

lada = Lada(40)
megrendeles = [Doboz(10), Doboz(20)]

print(f'{lada.kihasznaltsag_vizsgalo(megrendeles):.0f}%-os kihasználtság')


""" aggregáció """

class Szerelo:
    def __init__(self, nev):
        self.nev = nev

    def szerel(self):
        print("brutálmód szerel")

class Gepjarmu:
    def __init__(self, alvazszam, szerelo_obj=None):
        self.alvazszam = alvazszam
        self.szerelo_obj = szerelo_obj

    def __str__(self):
        if self.szerelo_obj:
            return f'gépjármű alv: {self.alvazszam}' \
                   f' szerelő név: {self.szerelo_obj.nev}'
        else:
            return f'gépjármú alv: {self.alvazszam}'

    def szereles_nagyon_szerelik(self):
        if self.szerelo_obj:
            self.szerelo_obj.szerel()

"""
szerelo = Szerelo("Szerelo Peter")
szerelo_rossz = Szerelo("Rossz Szerel")

print(szerelo, szerelo_rossz)

gepjarmu = Gepjarmu("ALV0123", szerelo)

gepjarmu.szereles_nagyon_szerelik()


"""




class Kulcs:
    def __init__(self, sorozatszam):
        self.sorozatszam = sorozatszam
        self._data = True

    @property
    def data(self):
        print("getter")
        return self._data


class Gepjarmu:
    def __init__(self, alvazszam, kulcs_serial):
        self.alvazszam = alvazszam
        self.kulcs_obj = Kulcs(kulcs_serial)

    def __str__(self):
        return f"{self.alvazszam} : keyserial {self.kulcs_obj.sorozatszam}"

    def analyze_data(self):
        return self.kulcs_obj.data

uj_gepjarmu = Gepjarmu('ALV0123', "KLCS0123")
regi_gepjarmu = Gepjarmu("ALV999", "KLCS999")

print(uj_gepjarmu.analyze_data())

del uj_gepjarmu

# print(uj_gepjarmu.kulcs_obj.data)






class Kiadas:
    def __init__(self, kiadas_eve, serial):
        self.kiadas_eve = kiadas_eve
        self.serial = serial

class Mu:
    TILTOTT_LISTA = {
        "nber_serial": hash("HMVS-BLA"),
        "data": {
            "isVezsely": True,
            "vezsely_in_uop": 1000
        }
    }

    def __init__(self, szerzo, cim):
        if self.is_tiltott_szerzo(szerzo):
            raise ValueError(f'unkownfail at 2.128.64.9/4 ... {szerzo} offline ')
        self.szerzo = szerzo
        self.cim = cim
        self.kiadasok = []

    @classmethod
    def is_tiltott_szerzo(cls, szerzo):
        return hash(szerzo) == cls.TILTOTT_LISTA.get("nber_serial")

    def kiadast_rogzito(self, kiadas_eve, serial):
        self.kiadasok.append(Kiadas(kiadas_eve, serial))

    def adatlapot_kiir(self):
        print(f'szerzo: {self.szerzo} : {self.cim}')
        print("Kiadásokk: ", end='')
        for kiadas in self.kiadasok:
            print(kiadas.kiadas_eve, end='. ')


szuper_jo_very_gut_konyv = Mu("ZEN-ELK", "C7Dim-Bb-ATHEN")

szuper_jo_very_gut_konyv.kiadast_rogzito('2030', "ZEN_ELK_BEST_OF_SUPER_ADMIN_PLUS_1")
szuper_jo_very_gut_konyv.adatlapot_kiir()

try:
    konyv = Mu("HMVS-BLA", "scientia sacra i-ii-iii")

    konyv.kiadast_rogzito('1944-45', 'HBSC123')
    konyv.kiadast_rogzito("2015", "HBSC123-U")
    konyv.adatlapot_kiir()
except ValueError as e:
    print(e)



class FileReader:
    """ Csak és kizárólag az olvasásért felel!!! """

    @staticmethod
    def read(file_path):
        with open(file_path, 'r') as file:
            return file.read()

    def read_json(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)


class FileWriter:
    """ Csak és kizárólag az írásért felel!!! """

    @staticmethod
    def write(file_path, data):
        with open(file_path, 'w') as file:
            file.write(data)

    @staticmethod
    def write_json(file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

class DataProcessor:
    """ Adatfeldolgozásért felel """

    # TODO: data to adattag mint példányváltozó
    # init data tulajdonság
    # majd property get/set
    def process(self, data):
        return data.upper()

    def filter_by_name(self, data, name):
        return [item for item in data if item["nev"] == name]

    def filter_by_age(self, data, min_age, max_age):
        return [item for item in data if min_age <= item['kor'] <= max_age]

    def filter_by_zip(self, data, zip_code):
        for item in data:
            print(item.get('iranyitoszam'), ':', zip_code)
        return [item for item in data if item.get('iranyitoszam') == zip_code]

class TestData:
    """ Teszt adat osztály publikus használatra """

    EXAMPLE_DATA_name_age_addr = [
        {"nev": "Teszt Elek", "kor": 30, "cim": "Teszt utca 1", "iranyitoszam": 1234},
        {"nev": "Minta Márton", "kor": 25, "cim": "Minta tér 2", "iranyitoszam": 5678},
        {"nev": "Példa Pál", "kor": 40, "cim": "Példa körút 3", "iranyitoszam": 1234}
    ]

    EXAMPLE_NAMES = []


reader = FileReader()
writer = FileWriter()
proccesor = DataProcessor()

writer.write_json("example2.json", TestData.EXAMPLE_DATA_name_age_addr)
print("sikeres kiírás")

loaded_data = reader.read_json("example2.json")

filtered_by_name = proccesor.filter_by_name(loaded_data, "Teszt Elek")

filtered_by_zip = proccesor.filter_by_zip(loaded_data, 1234)

print(filtered_by_name, filtered_by_zip)