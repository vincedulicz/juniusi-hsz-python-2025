"""

Események naplózása és hiba-ellenőrzés egy fájlban

Készíts egy Python programot, amely:

Beolvas egy "esemenyek.txt" nevű fájlt és megjeleníti a tartalmát.
Új eseményt ír a fájlba, és biztosítja, hogy a fájl
minden szükséges adatot tartalmazzon.

Kivételkezeléssel ellenőrzi, hogy a fájl elérhető-e (pl. létezik-e).
Biztosítja, hogy csak érvényes formátumú adatokat
(pl. dátum és eseménynév) írjon be.

Újrafelhasználható függvényeket tartalmaz
különböző fájlkezelési feladatokhoz.

Egyedi kivételt is definiál hibás adatbevitel esetére.

Külön kezeli a fájl átnevezését és felülírását.

"""
import datetime


class InvalidDataException(Exception):
    """ Egyedi kivétel osztály """

    def __init__(self, message="Érvenytelen adat!"):
        self.message = message
        super().__init__(self.message)

def write_event(event_name):
    try:
        if not event_name:
            raise InvalidDataException("Az esemény nem lehet üres!")

        with open("esemenyek.txt", "a", encoding="utf-8") as file:
            event_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f'{event_time} - {event_name}\n')
            print(f'Az esemény {event_name} sikeresen naplózva')
    except InvalidDataException as e:
        print(e)
    except Exception as e:
        print(f'Váratlan hiba {e}')

def read_events():
    try:
        with open("naplo.txt", "r", encoding="utf-8") as file:
            print(f"Események naplója: {file.read()}")
    except FileNotFoundError:
        print("Nincs ilyen fájl")
    except IOError as e:
        print(f"Olvasási hiba: {e}")

def modify_event(old_text, new_text):
    try:
        with open("esemenyek.txt", "r+", encoding="utf-8") as file:
            content = file.read()
            if old_text not in content:
                raise InvalidDataException("Az esemény nem található")

            updated_content = content.replace(old_text, new_text)

            file.seek(0)
            file.write(updated_content)
            file.truncate()

            print(f'Az esemény módosítva lett: {old_text}-ről {new_text}-re')
    except InvalidDataException as e:
        print(e)
    except Exception as e:
        print(f'váratlan hiba {e}')

def rename_file(new_name):
    try:
        os.rename("esemenyek.txt", new_name)
        print(f"A fájl sikeresen átnevezve: {new_name}")
    except FileNotFoundError:
        print("nem található a file")
    except FileExistsError:
        print("a fájl már létezik")
    except Exception as e:
        print(f'váratlan hiba: {e}')

def overwrite_file():
    try:
        with open("esemenyek.txt", "a", encoding="utf-8") as file:
            file.write("Az események napló újraindítva\n")
            print("a fájl tartalma felül írva")
    except Exception as e:
        print(f"váratlan hiba: {e}")

def main():
    write_event("bejelentkezés")
    write_event("adatfeltölés")
    write_event("kijelentkezés")

    read_events()

    modify_event("adatfeltölés", "adatFel")

    rename_file("uj_esemenyek.txt")

    overwrite_file()

    read_events()


main()
