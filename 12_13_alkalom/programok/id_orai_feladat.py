import json
import random
import string
from datetime import datetime, timedelta
from typing import Dict, Any, Callable


names = [
    "John Doe",
    "Jane Smith",
    "Alice Johnson",
    "Bob Brown",
    "Charlie Davis",
    "Emily Clark"
]


def generate_user_id() -> str:
    """
    Véletlenszerű 6 karakteres felhasználó azonosító generálása.
    :return: str - azonosító
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


def generate_born_date() -> str:
    """
    Születési dátum generálása véletlenszerűen (1920–1980 között).
    :return: str - dátum 'ÉÉÉÉ.HH.NN' formátumban
    """
    year = random.randint(1920, 1980)
    month = random.randint(1, 12)
    day = random.randint(1, 28) # egyszerű...
    return f'{year:04d}.{month:02d}.{day:02d}'


def generate_age(born_date: str) -> int:
    """
    Életkor kiszámítása a születési dátumból.
    :param born_date: str - dátum 'ÉÉÉÉ.HH.NN' formátumban
    :return: int - életkor
    """
    birth_year = int(born_date.split(".")[0])
    current_year = datetime.now().year
    return current_year - birth_year


def generate_country() -> str:
    """
    Véletlenszerű országkód generálása.
    :return: str - például: 'HU', 'EU', 'USA', 'SP'
    """
    return random.choice(['HU', 'EU', 'USA', 'SP'])


def generate_worker() -> bool:
    """
    Dolgozó státusz generálása.
    :return: bool - True ha dolgozó, különben False
    """
    return random.choice([True, False])


def generate_valid_until() -> datetime:
    """
    Érvényesség dátumának generálása a mai naphoz képest 0–365 nappal későbbre.
    :return: datetime - dátum objektum
    """
    return datetime.now() + timedelta(days=random.randint(0, 365))


def generate_random_json(num_users: int = 10) -> Dict[str, Dict[str, Any]]:
    """
    Véletlenszerű felhasználói adatokból álló JSON szerkezet generálása.
    :param num_users: int - felhasználók száma
    :return: dict - felhasználók adatai
    """
    users = {}
    for _ in range(num_users):
        user_id = f'user-{generate_user_id()}'
        born_date = generate_born_date()
        age = generate_age(born_date)

        users[user_id] = {
            "valid_until": generate_valid_until().strftime("%Y.%m.%d"),
            "born-date": born_date,
            "name": random.choice(names),
            "age": age,
            "country": generate_country(),
            "worker": generate_worker(),
            "other": []
        }
    return users


def save_json_to_txt(file_name: str, num_users: int = 10) -> None: # pl: (bool, err) -> (1, null) | (0, err_msg)
    """
    Véletlenszerű JSON adatok mentése fájlba.
    :param file_name: str - a mentendő fájl neve
    :param num_users: int - felhasználók száma
    """
    random_json = generate_random_json(num_users)
    with open(file_name, 'w') as file:
        json.dump(random_json, file, indent=4)


def read_json_from_txt(file_name: str) -> Dict[str, Any]:
    """
    JSON adat beolvasása fájlból.
    :param file_name: str - fájl neve
    :return: dict - beolvasott adat
    """
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data


def save_dict_if_not_empty(data: Dict[str, Any], output_file: str) -> None:
    """
    Elmenti a megadott szótárat JSON fájlba, ha nem üres.
    :param data: dict - mentendő adatok
    :param output_file: str - célfájl neve
    """
    if data:
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)


def filter_users_by_condition(data: Dict[str, Any], condition: Callable[[Dict[str, Any]], bool]) -> Dict[str, Any]:
    """
    Felhasználók szűrése feltétel alapján.
    :param data: dict - bemeneti adatok
    :param condition: függvény, amely True-t ad vissza, ha a felhasználó megfelel
    :return: dict - szűrt felhasználók
    """
    return {
        user_id: user_info for user_id, user_info in data.items() if condition(user_info)
    }


def check_and_save_expiring_users(input_file: str, output_file: str) -> None:
    """
    Lejáró (180 napon belül) felhasználók keresése és mentése.
    :param input_file: str - forrás fájl
    :param output_file: str - cél fájl
    """
    data = read_json_from_txt(input_file)

    def is_expiring(user_info: Dict[str, Any]) -> bool:
        valid_until = datetime.strptime(user_info['valid_until'], '%Y.%m.%d')
        days_left = (valid_until - datetime.now()).days
        return days_left <= 180

    expiring_users = filter_users_by_condition(data, is_expiring)
    save_dict_if_not_empty(expiring_users, output_file)


def save_no_worker_users(input_file: str, output_file: str) -> None:
    """
    Nem dolgozó felhasználók mentése fájlba.
    :param input_file: str - forrás fájl
    :param output_file: str - cél fájl
    """
    data = read_json_from_txt(input_file)
    no_worker_users = filter_users_by_condition(data, lambda u: not u['worker'])
    save_dict_if_not_empty(no_worker_users, output_file)

def save_over_65_users(input_file: str, output_file: str) -> None:
    """
    65 év feletti felhasználók mentése fájlba.
    :param input_file: str - forrás fájl
    :param output_file: str - cél fájl
    """
    data = read_json_from_txt(input_file)
    over_65_users = filter_users_by_condition(data, lambda u: u['age'] > 65)
    save_dict_if_not_empty(over_65_users, output_file)


def save_middle_eu_users(input_file: str, output_file: str) -> None:
    """
    Magyar (HU) felhasználók mentése fájlba.
    :param input_file: str - forrás fájl
    :param output_file: str - cél fájl
    """
    data = read_json_from_txt(input_file)
    middle_eu_users = filter_users_by_condition(data, lambda u: u['country'] == 'HU')
    save_dict_if_not_empty(middle_eu_users, output_file)


def main() -> None:
    """
    A program fő belépési pontja.
    - Véletlenszerű felhasználói adatok generálása és mentése.
    - Szűrések elvégzése: lejáró, nem dolgozó, 65+, magyar felhasználók.
    """
    save_json_to_txt("adatok/random_user_data.txt")

    check_and_save_expiring_users("adatok/random_user_data.txt", "adatok/expire180.json")
    save_no_worker_users("adatok/random_user_data.txt", "adatok/no_worker.json")
    save_over_65_users("adatok/random_user_data.txt", "adatok/over65.json")
    save_middle_eu_users("adatok/random_user_data.txt", "adatok/middle_eu.json")


main()
