import csv
import json
import random
import sys
from datetime import datetime, timedelta
from typing import List, Dict, Optional

# TODO: self nincs is használatba
# pkg szétszedése
# entry átgondolása (beolvasás)
# property

class WeatherEntry:
    def __init__(self, date: datetime, condition: str, temperature: float, rain_chance: int):
        self.date = date.strftime('%Y-%m-%d')
        self.condition = condition
        self.temperature = temperature
        self.rain_chance = rain_chance

    def to_dict(self) -> Dict[str, object]:
        return {
            "condition": self.condition,
            "temperature": self.temperature,
            "rain_chance": self.rain_chance
        }

    def to_text(self) -> str:
        return (
            f"Dátum: {self.date}\n"
            f"Időjárás: {self.condition}\n"
            f"Hőmérséklet: {self.temperature}C\n"
            f"Várható eső: {self.rain_chance}%\n"
        )


class WeatherDataGenerator:
    CONDITIONS = ["szeles", "napos", "esős", "ködös", "semillen"]

    def generate(self, start_date: datetime, end_date: datetime) -> List[WeatherEntry]:
        current_date = start_date
        entries = []
        while current_date <= end_date:
            entry = WeatherEntry(
                date=current_date,
                condition=random.choice(self.CONDITIONS),
                temperature=round(random.uniform(0, 20), 1),
                rain_chance=random.randint(0, 100)
            )
            entries.append(entry)
            current_date += timedelta(days=1)
        return entries


class TxtWeatherLoader:
    def load(self, filename: str) -> Dict[str, Dict[str, object]]:
        data = {}
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                current_date = None
                for line in file:
                    if line.startswith("Dátum:"):
                        current_date = line.split(": ")[1].strip()
                        data[current_date] = {}
                    elif line.startswith("Időjárás:"):
                        data[current_date]["condition"] = line.split(": ")[1].strip()
                    elif line.startswith("Hőmérséklet:"):
                        data[current_date]["temperature"] = float(line.split(": ")[1].strip("C\n"))
                    elif line.startswith("Várható eső:"):
                        data[current_date]["rain_chance"] = int(line.split(": ")[1].strip("%\n"))
        except Exception as e:
            print(f"Hiba TXT betöltés során: {e}")
        return data


class JsonWeatherSaver:
    # TODO: ? mé van self????????????????????????????????????????????????????????
    def save(self, data: Dict, filename: str) -> None:
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            print(f"JSON mentve: {filename}")
        except IOError as e:
            print(f"Nem lehet elmenteni '{filename}': {e}")


class CsvWeatherExporter:
    def export(self, data: Dict[str, Dict[str, object]], output_file: str) -> bool:
        try:
            with open(output_file, 'w', encoding='utf-8', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["Dátum", "Időjárás", "Hőmérséklet (C)", "Eső valószínűség (%)"])
                writer.writeheader()
                for date, details in data.items():
                    writer.writerow({
                        "Dátum": date,
                        "Időjárás": details["condition"],
                        "Hőmérséklet (C)": details["temperature"],
                        "Eső valószínűség (%)": details["rain_chance"]
                    })
            print(f"CSV exportálva: {output_file}")
            return True
        except Exception as e:
            print(f"Hiba CSV exportáláskor: {e}")
            return False


class WeatherStorage:
    def __init__(self):
        self.txt_loader = TxtWeatherLoader()
        self.json_saver = JsonWeatherSaver()
        self.csv_exporter = CsvWeatherExporter()

    def save_to_txt(self, filename: str, entries: List[WeatherEntry]) -> None:
        with open(filename, 'w', encoding='utf-8') as file:
            for entry in entries:
                file.write(entry.to_text())

    def load_from_txt(self, filename: str) -> Dict[str, Dict[str, object]]:
        data = self.txt_loader.load(filename)
        self.json_saver.save(data, "teszterweather.json")
        return data

    def export_to_csv(self, data: Dict[str, Dict[str, object]], output_file: str) -> bool:
        return self.csv_exporter.export(data, output_file)


class WeatherReport:
    def __init__(self, data: Dict[str, Dict[str, object]]):
        self.data = data

    def display_day(self, date: str):
        if date in self.data:
            details = self.data[date]
            print(f"\nIdőjárás {date} napján:")
            print(f"Időjárás: {details['condition']}")
            print(f"Hőmérséklet: {details['temperature']}C")
            print(f"Várható eső: {details['rain_chance']}%")
        else:
            print("Nincs adat erre a napra.")

    def display_month(self, month: str):
        print(f"\nIdőjárás jelentés a {month} hónapra:")
        for date, details in self.data.items():
            if date.startswith(month):
                print(f"{date}: {details['condition']}, {details['temperature']}C, eső: {details['rain_chance']}%")

    def analyze_range(self, start: str, end: str):
        date_range = [d for d in self.data if start <= d <= end]
        if not date_range:
            print("Nincs adat a megadott időszakban.")
            return

        temps = [self.data[d]["temperature"] for d in date_range]
        rain_days = sum(1 for d in date_range if self.data[d]["rain_chance"] > 0)
        semillen_days = sum(1 for d in date_range if self.data[d]["condition"] == "semillen")

        print(f"\nStatisztika {start} - {end}:")
        print(f"Átlaghőmérséklet: {sum(temps)/len(temps):.2f}C")
        print(f"Max hőmérséklet: {max(temps)}C")
        print(f"Esős napok: {rain_days}")
        print(f"Semillen napok: {semillen_days}")


class WeatherApp:
    def __init__(self):
        self.generator = WeatherDataGenerator()
        self.storage = WeatherStorage()
        self.data: Optional[Dict[str, Dict[str, object]]] = None

    def run(self):
        entries = self.generator.generate(datetime(2025, 8, 4), datetime(2025, 12, 12))
        self.storage.save_to_txt("weather_data.txt", entries)
        self.data = self.storage.load_from_txt("weather_data.txt")
        self.menu()

    def menu(self):
        report = WeatherReport(self.data)
        while True:
            print("\nMenü:")
            print("1. Napi/havi jelentés")
            print("2. Időintervallum statisztika")
            print("3. Exportálás CSV-be")
            print("4. Kilépés (q)")
            choice = input("Választás: ").strip().lower()

            if choice in ["4", "q", "quit"]:
                print("Kilépés...")
                sys.exit(0)
            elif choice == "1":
                sub = input("Nap vagy hónap? (D/M): ").strip().lower()
                if sub == "d":
                    date = input("Dátum (YYYY-MM-DD): ")
                    report.display_day(date)
                elif sub == "m":
                    month = input("Hónap (YYYY-MM): ")
                    report.display_month(month)
            elif choice == "2":
                start = input("Kezdő dátum (YYYY-MM-DD): ")
                end = input("Végdátum (YYYY-MM-DD): ")
                report.analyze_range(start, end)
            elif choice == "3":
                self.storage.export_to_csv(self.data, "weather_data.csv")
            else:
                print("Érvénytelen választás.")


if __name__ == '__main__':
    app = WeatherApp()
    app.run()
