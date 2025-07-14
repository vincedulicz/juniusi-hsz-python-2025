import math
import random
from datetime import date, datetime, timedelta
from statistics import mean, stdev



##################
### 1. feladat ###
##################



def get_today_info():
    today = date.today()
    return {
        "date": today,
        "weekday": today.strftime('%A'),
        "day_of_year": today.timetuple().tm_yday
    }

def generate_random_numbers(count=10, start=1, end=100):
    return [random.randint(start, end) for _ in range(count)]

def get_lucky_number(numbers):
    return random.choice(numbers)

def calculate_statistics(numbers):
    return {
        "average": mean(numbers),
        "stdev": stdev(numbers),
        "maximum": max(numbers),
        "minimum": min(numbers),
        "sqrt_sum": math.sqrt(sum(numbers))
    }

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def task_1_lucky_statistics():
    today_info = get_today_info()
    numbers = generate_random_numbers()
    lucky_number = get_lucky_number(numbers)
    stats = calculate_statistics(numbers)

    print("\nDátum:", today_info['date'])
    print("Nap neve:", today_info['weekday'])
    print("Év", today_info['day_of_year'], ". napja")
    print("\nGenerált számok:", numbers)
    print("Szerencseszám:", lucky_number)

    print("\nStatisztikák:")
    print(f" - Átlag: {stats['average']:.2f}")
    print(f" - Szórás: {stats['stdev']:.2f}")
    print(f" - Max: {stats['maximum']}, Min: {stats['minimum']}")
    print(f" - Összeg négyzetgyöke: {stats['sqrt_sum']:.2f}")

    if is_prime(lucky_number):
        print("\nMa különösen szerencsés napod van! A szerencseszám prímszám.")

        

        
##################
### 2. feladat ###
##################




def days_until_birthday(month: int, day: int) -> int:
    today = date.today()
    current_year = today.year
    try:
        birthday = date(current_year, month, day)
    except ValueError:
        print("Hibás dátum!")
        return -1

    if birthday < today:
        birthday = date(current_year + 1, month, day)

    return (birthday - today).days

def task_2_birthday_countdown():
    try:
        month = int(input("Add meg a születésnapod hónapját (1-12): "))
        day = int(input("Add meg a napot (1-31): "))
        days_left = days_until_birthday(month, day)
        if days_left >= 0:
            print(f"\n{days_left} nap van hátra a születésnapodig.")
    except ValueError:
        print("Nem számot adtál meg.")

        
        
##################
### 3. feladat ###
##################



def task_3_trig_quiz():
    angle_deg = random.randint(0, 360)
    angle_rad = math.radians(angle_deg)
    func = random.choice(['sin', 'cos'])

    correct = math.sin(angle_rad) if func == 'sin' else math.cos(angle_rad)
    print(f"\nMennyi a {func}({angle_deg})?")
    
    try:
        user_input = float(input("Válasz: "))
        diff = abs(user_input - correct)
        if diff < 0.01:
            print("Helyes tipp!")
        else:
            print(f"Nem pontos. Helyes érték: {correct:.4f}")
    except ValueError:
        print("Nem számot adtál meg.")

        
        
##################
### 4. feladat ###
##################



def generate_random_time():
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)

    return datetime.combine(date.today(), datetime.min.time()) + timedelta(hours=hour, minutes=minute)

def task_4_time_difference():
    time1 = generate_random_time()
    time2 = generate_random_time()
    start, end = sorted([time1, time2])

    delta = end - start
    hours, remainder = divmod(delta.seconds, 3600)
    minutes = remainder // 60

    print("\nVéletlen időpontok:")
    print("Első:", start.time())
    print("Második:", end.time())
    print(f"Különbség: {hours} óra {minutes} perc")

def main_menu():
    while True:
        print("1. Szerencseszám + statisztikák")
        print("2. Születésnapig hátralévő napok")
        print("3. Trigonometrikus kvíz")
        print("4. Két időpont különbsége")
        print("0. Kilépés")

        choice = input("Válassz egy feladatot (0-4): ")

        if choice == '1':
            task_1_lucky_statistics()
        elif choice == '2':
            task_2_birthday_countdown()
        elif choice == '3':
            task_3_trig_quiz()
        elif choice == '4':
            task_4_time_difference()
        elif choice == '0':
            print("A progi leáll...")
            break
        else:
            print("Érvénytelen! Válassz újra...")

            
main_menu()