# I. Feladat: Adott dátumhoz napok hozzáadása
import random
from datetime import datetime, timedelta


def i_feladat():
    start_date = datetime(2025, 7, 16)
    days_to_add = 15

    new_date = start_date + timedelta(days=days_to_add)

    print("New date:", new_date.strftime("%Y-%m-%d"))

    i_feladat()

i_feladat()

# II. Feladat: Véletlen szám generálása adott intervallumban
def ii_feladat():
    random_number = random.randint(1, 100)
    print("rand", random_number)

# III. Feladat: Véletlenszerű dátum generálása egy évben belül
def iii_feladat():
    start_date = datetime(2025, 7, 16)
    end_date = datetime(2025, 12, 30)

    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)

    print("rand", random_date.strftime("%Y-%m-%d"))

# IV. Feladat: Véletlenszerű listaelem kiválasztása
def iv_feladat():
    names = ["Alice", "Bob", "Charlie", "Diana"]
    chosen_name = random.choice(names)

    print("Chosen name:", chosen_name)

# V. Feladat: Időkülönbség kiszámítása
def v_feladat():
    start_date = datetime(2025, 7, 16)
    end_date = datetime(2025, 12, 30)

    difference = (end_date - start_date).days

    print("diff", difference)

# VI. Feladat: Véletlenszerű számsorozat generálása
def vi_feladat():
    random_numbers = [random.randint(1, 50) for _ in range(10)]
    print("rand seq", random_numbers)

# VII. Feladat: Dátum érvényességének ellenőrzése
def vii_feladat():
    year, month, day = 2025, 7, 16
    try:
        valid_date = datetime(year, month, day)
        print("Valid date", valid_date)
    except ValueError:
        print("Invalid date")

# VIII. Feladat: Véletlenszerű sorrend létrehozása
def viii_feladat():
    items = ["apple", "banana", "cherry", "date"]
    random.shuffle(items)

    print("shuffled list", items)

# IX. Feladat: Jövőbeli dátum és idő kiszámítása
def ix_feladat():
    now = datetime.now()
    future_time = now + timedelta(days=3, hours=4, minutes=30)

    print("fut time", future_time)

# X. Feladat: Születésnap kiszámítása
def x_feladat():
    today = datetime.now()
    birthday = datetime(today.year, 12, 25)

    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)
    days_left = (birthday -today).days

    print("days until birthday", days_left)

# XI. Feladat: Véletlenszám generálása folytonos intervallumban (uniform)
def xi_feladat():
    random_float = random.uniform(1.0, 10.0)
    print("rand float", random_float)

# XII. Feladat: Egész véletlenszám generálása (randint)
def xii_feladat():
    random_integer = random.randint(50, 100)
    print("rand int", random_integer)

# XIII. Feladat: Lista elemeinek megkeverése (shuffle)
def xiii_feladat():
    items = [1, 2, 3, 4, 5]
    random.shuffle(items)

    print("Shuffled list", items)

# XIV. Feladat: Lista egy elemének kiválasztása (choice)
def xiv_feladat():
    colors = ["red", "blue", "green", "yellow"]
    chosen_color = random.choice(colors)

    print("Chosen color", chosen_color)

# XV. Feladat: Több elem véletlenszerű kiválasztása (sample)
def xv_feladat():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random_sample = random.sample(numbers, 3)

    print("Random sample", random_sample)

# XVI. Feladat: Dátum formázása szöveggé (strftime)
def xvi_feladat():
    today = datetime.now()
    formatted_date = today.strftime("%Y-%m-%d")

# XVII. Feladat: Szövegből dátum objektum készítése (strptime)
def xvii_feladat():
    date_string = "2025-07-16"
    date_object = datetime.strptime(date_string, "%Y-%m-%d")

    print("dt object", date_object)

# XVIII. Feladat: Születési dátum formázása
def xviii_feladat():
    birth_date = "15/05/1888"
    formatted_date = datetime.strptime(birth_date, "%d/%m/%Y").strftime("%Y-%m-%d")

    print("formatted date", formatted_date)

# XIX. Feladat: Véletlenszerű lebegőpontos számok listája (uniform)
def xix_feladat():
    random_floats = [random.uniform(0.0, 1.0) for _ in range(5)]

    print("random floats:", random_floats)

# XX. Feladat: Véletlenszerű csapatok generálása (sample)
def xx_feladat():
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]

    team_a = random.sample(names, 5)
    team_b = [name for name in names if name not in team_a]

    print("team a:", team_a)
    print("team b:", team_b)

def main():
    i_feladat()
    ii_feladat()
    iii_feladat()
    iv_feladat()
    v_feladat()
    vi_feladat()
    vii_feladat()
    viii_feladat()
    ix_feladat()
    x_feladat()
    xi_feladat()
    xii_feladat()
    xiii_feladat()
    xiv_feladat()
    xv_feladat()
    xvi_feladat()
    xvii_feladat()
    xviii_feladat()
    xix_feladat()
    xx_feladat()

main()
