data_list_string_format = """Név;Életkor;Város
Németh Kamilla;19;Debrecen
Fekete Géza;18;Pécs
Kovács Péter;27;Budapest
Kiss Tibor;20;Debrecen
Szabó Erzsébet;21;Budapest
Szilágyi Ede;18;Pécs
Agárdi Pál;26;Budapest
Pálosi Richárd;23;Budapest
Budai Máté;19;Debrecen
Karácsony Antal;20;Budapest
Aradi Márta;27;Pécs
Piros Adél;29;Debrecen
Bíró Zsolt;16;Budapest
Szabados Attila;25;Debrecen
Román Sarolta;24;Budapest
Virág Bertalan;22;Pécs
Varga Imre;18;Budapest
Tóth Sándor;22;Debrecen
Nagy Ibolya;23;Pécs
Horváth Ferenc;17;Budapest
Balogh Edina;26;Budapest"""

""" 

[
{'nev': 'Németh Kamilla', 'age': 19, 'city': 'Debrecen', 'other': []},
{'nev': 'Fekete Géza', 'age': 18, 'city': 'Pécs', 'other': []},
{'nev': 'Kovács Péter', 'age': 27, 'city': 'Budapest', 'other': []},
{'nev': 'Kiss Tibor', 'age': 20, 'city': 'Debrecen', 'other': []},
{…}
]


"""

def string_to_list(data_string):
    return [line.split(';') for line in data_string.strip().split('\n')[1:]]

def list_to_dict(data_list):
    return [{'nev': name, 'age': int(age), 'city': city, 'other': []} for name, age, city in data_list]

def print_data(data, show_name=True, show_age=True, show_city=True):
    if not show_name and not show_age and not show_city:
        print("Nem írunk ki semmit")
        return

    print('\n%-20s%-6s%-12s\n' % ("Név", "Kor", "Város"))

    for entry in data:
        name = entry['nev'] if show_name else ''
        age = entry['age'] if show_age else ''
        city = entry['city'] if show_city else ''

        print('%-20s%-6s%-12s' % (name, age, city))

def categorize_by_age(data):
    age_groups = {'12-20': [], '21-25': [], '26-32': [], '33+': []}

    for person in data:
        age = person['age']

        if 12 <= age <= 20:
            age_groups['12-20'].append(person.get('nev'))
        elif 21 <= age <= 25:
            age_groups['21-25'].append(person.get('nev'))
        elif 26 <= age <= 32:
            age_groups['26-32'].append(person.get('nev'))
        else:
            age_groups['33+'].append(person.get('nev'))

    return age_groups

def calculate_avg_age(data):
    total_age = sum(entry['age'] for entry in data)

    return round(total_age / len(data), 1) if data else 0

def group_people_by_city(data):
    same_city_people = {}

    for entry in data:
        first_name, last_name = entry['nev'].split()
        city = entry['city']

        if city not in same_city_people:
            same_city_people[city] = []

        same_city_people[city].append(first_name + ' ' + last_name[0] + '.')

    return same_city_people

def find_most_common_city(data):
    city_counts = {}

    for entry in data:
        city = entry['city']
        if city not in city_counts:
            city_counts[city] = 0
        city_counts[city] += 1

    return max(city_counts, key=city_counts.get, default=None)

def main():
    data_list = string_to_list(data_list_string_format)
    data_dict_list = list_to_dict(data_list)

    print('Adatok kiírása')
    print_data(data_dict_list) #, show_age=False)

    age_groups = categorize_by_age(data_dict_list)
    most_common_city = find_most_common_city(data_dict_list)
    avg_age = calculate_avg_age(data_dict_list)
    same_city_people = group_people_by_city(data_dict_list)

    print(
        f'Életkor csoportok: '
        f'\n12-20: {age_groups.get("12-20")}'
        f'\n21-25: {age_groups.get("21-25")}'
        f'\n26-32: {age_groups.get("26-32")}'
        f'\n33+: {age_groups.get("33+")}'
    )

    print(f'\nLeggyakoribb város: {most_common_city}')
    print(f'\nÁtlagéletkor: {avg_age}')
    print(f'\nAzonos városban élők:')

    for city, names in same_city_people.items():
        print(f'{city}: {",".join(names)}')


main()