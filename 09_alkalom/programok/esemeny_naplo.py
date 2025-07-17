import datetime
import os.path
import random

EVENTS = [
    "Felhasználói bejelentkezés",
    "Adatfeltöltés",
    "Jelszó módosítás",
    "Kilépés",
    "Hozzáférés megtagadva"
]

def get_log_filename(base_name="naplo", max_size=5 * 1024):
    filename = f'{base_name}.txt' # .log
    counter = 1

    while os.path.exists(filename) and os.path.getsize(filename) > max_size:
        counter += 1
        filename = f'{base_name}_{counter}.txt'

    return filename

def random_past_datatime():
    days_ago = random.randint(0, 30)
    hours_ago = random.randint(0, 23)
    minutes_ago = random.randint(0, 59)

    event_time = datetime.datetime.now() - datetime.timedelta(
        days=days_ago,
        hours=hours_ago,
        minutes=minutes_ago
    )

    return event_time

def create_log_entry():
    event_time = random_past_datatime()
    event = random.choice(EVENTS)
    formatted_time = event_time.strftime("%Y. %b %D. %a, %H:%M")

    return f'{formatted_time} - {event}'

def write_log_evenets(num_entries=10):
    filename = get_log_filename()
    with open(filename, "a", encoding="utf-8") as file:
        for _ in range(num_entries):
            entry = create_log_entry()
            file.write(entry + "\n")
            print(f'Naplózott esemény: {entry}')

def main():
    write_log_evenets(1000)


main()