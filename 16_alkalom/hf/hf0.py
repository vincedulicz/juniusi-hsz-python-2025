import csv
import json
import random
import sys
from datetime import datetime, timedelta


def generate_weather_entry(current_date, conditions):
    condition = random.choice(conditions)
    temperature = round(random.uniform(0, 20), 1)
    rain_chance = random.randint(0, 100)

    return f"Dátum: {current_date.strftime('%Y-%m-%d')}\n" \
           f"Időjárás: {condition}\n" \
           f"Hőmérséklet: {temperature}C\n" \
           f"Várható eső: {rain_chance}%\n"


def generate_weather_data(file_name, start_date, end_date):
    weather_conditions = ["szeles", "napos", "esős", "ködös", "semillen"]
    current_date = start_date

    with open(file_name, "w", encoding='utf-8') as file:
        while current_date <= end_date:
            file.write(generate_weather_entry(current_date, weather_conditions))
            current_date += timedelta(days=1)


def load_weather_data(file_name):
    """ Load weather data nagyon usefull infomartion """

    weather_data = {}

    try:
        with open(file_name, "r", encoding='utf-8') as file:
            current_date = None

            for line in file:

                if line.startswith("Dátum:"):
                    current_date = line.split(": ")[1].strip()
                    weather_data[current_date] = {}

                elif line.startswith("Időjárás:"):
                    weather_data[current_date]["condition"] = line.split(": ")[1].strip()

                elif line.startswith("Hőmérséklet:"):
                    weather_data[current_date]["temperature"] = float(line.split(": ")[1].strip("C\n"))

                elif line.startswith("Várható eső:"):
                    weather_data[current_date]["rain_chance"] = int(line.split(": ")[1].strip("%\n"))

        save_json(weather_data, "teszterweather.json")
        return weather_data
    except (Exception, FileNotFoundError) as e:
        print(f'Hiba: {e}')
        return {}


def export_to_csv(data, output_file):
    is_data_writed = False
    try:
        with open(output_file, "w", encoding='utf-8', newline='') as csvfile:
            fieldnames = ["Dátum", "Időjárás", "Hőmérséklet (C)", "Eső valószínűség (%)"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for date, details in data.items():
                writer.writerow({
                    "Dátum": date,
                    "Időjárás": details["condition"],
                    "Hőmérséklet (C)": details["temperature"],
                    "Eső valószínűség (%)": details["rain_chance"]
                })
        is_data_writed = True
        print(f"\nAz adatok sikeresen exportálva a következő fájlba: {output_file}")
    except (Exception, IOError) as e:
        print(f'Hiba: {e}')
        return is_data_writed

    return is_data_writed


def save_json(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Adat elmentve mint {filename}")
    except IOError as e:
        print(f"Error: Nem lehet elmenteni '{filename}'. {e}")


def display_day_report(data, date):
    if date in data:
        print(f"\nIdőjárás {date} napján:")
        print(f"Időjárás: {data[date]['condition']}")
        print(f"Hőmérséklet: {data[date]['temperature']}C")
        print(f"Várható eső: {data[date]['rain_chance']}%")
    else:
        print("Nem található adat a megadott dátumra.")


def display_month_report(data, month):
    print(f"\nIdőjárás jelentés a {month} hónapra:")

    for date, details in data.items():
        if date.startswith(month):
            print(f"{date}: {details['condition']}, "
                  f"{details['temperature']}C, "
                  f"eső: {details['rain_chance']}%")


def display_daily_or_monthly(data):
    option = input("Napra vagy hónapra keresel? (D/M): ").strip().lower()

    if is_exit_program(option):
        exit_process()
    if option == "d":
        date = input("Add meg a dátumot (YYYY-MM-DD): ").strip()
        display_day_report(data, date)
    elif option == "m":
        month = input("Add meg a hónapot (YYYY-MM): ").strip()
        display_month_report(data, month)


def analyze_date_range(data, start_date, end_date):
    date_range = [date for date in data if start_date <= date <= end_date]
    if not date_range:
        print("Nem található adat a megadott időszakban.")
        return

    total_temp = sum(data[date]["temperature"] for date in date_range)
    max_temp = max(data[date]["temperature"] for date in date_range)
    rainy_days = sum(1 for date in date_range if data[date]["rain_chance"] > 0)
    semillen_days = sum(1 for date in date_range if data[date]["condition"] == "semillen")

    print(f"\nStatisztika {start_date} és {end_date} között:")
    print(f"Átlaghőmérséklet: {total_temp / len(date_range):.2f}C")
    print(f"Maximális hőmérséklet: {max_temp}C")
    print(f"Esős napok száma: {rainy_days}")
    print(f"Semillen napok száma: {semillen_days}")


def handle_date_range_analysis(data):
    start_date = input("Add meg a kezdő dátumot (YYYY-MM-DD): ").strip()
    if is_exit_program(start_date):
        exit_process()

    end_date = input("Add meg a végdátumot (YYYY-MM-DD): ").strip()
    if is_exit_program(end_date):
        exit_process()

    analyze_date_range(data, start_date, end_date)


def is_exit_program(choice):
    return choice in ["4", "end", "q", "quit"]


def exit_process():
    sys.exit(1)


def main_menu(data):
    while True:
        print("\nMenü:")
        print("0. Kilépés")
        print("1. Napi/havi jelentés")
        print("2. Két időpont közötti statisztika")
        print("3. Adatok exportálása CSV-be")
        print("4. Kilépés (end/q/quit)")
        choice = input("Választás: ").strip().lower()

        if choice == "0":
            print("Kilépés...")
            exit_process()
        elif choice == "1":
            display_daily_or_monthly(data)
        elif choice == "2":
            handle_date_range_analysis(data)
        elif choice == "3":
            output_file = "weather_data.csv"
            export_to_csv(data, output_file)
        else:
            print("Érvénytelen választás, próbáld újra!")


def main():
    file_name = "weather_data.txt"
    generate_weather_data(file_name, datetime(2025, 8, 4), datetime(2025, 12, 12))
    data = load_weather_data(file_name)
    main_menu(data)


main()

