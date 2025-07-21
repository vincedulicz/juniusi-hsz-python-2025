import random


def task_01():
    with open('01_feladat.txt', encoding='utf-8') as f:
        students = [line.strip().split(";") for line in f]

    students = [(name, int(score)) for name, score in students]

    total_score = sum(score for _, score in students)

    avarag_score = total_score / len(students)

    passed_students = [name for name, score in students if score >= 60]

    best_student_name, best_score = max(students, key=lambda x: x[1])

    worst_student_name, worst_score = min(students, key=lambda x: x[1])

    # print()

    with open('01_eredmeny.txt', 'w', encoding='utf-8') as f:
        for name, score in students:
            passed = 'yes' if score >= 60 else 'no'
            f.write(f'{name};{score};{passed}\n')

def task_02():
    drawn_numbers = set(random.sample(range(1, 91), 5))
    print(f'drawn numbers {sorted(drawn_numbers)}')

    with open('02_feladat.txt', encoding="utf-8") as f:
        players = [line.strip().split(';') for line in f]

    results = []
    for name, numbers_str in players:
        numbers = set(map(int, numbers_str.split(',')))

        hits = len(drawn_numbers & numbers)

        results.append((name, hits))

    with open('02_eredmeny.txt', 'w', encoding='utf-8') as f:
        for name, hits in results:
            f.write(f'{name};{hits}\n')

def task_03():
    with open('03_feladat.txt', encoding='utf-8') as f:
        orders = [line.strip().split(';') for line in f]

    orders = [(product, int(quantity)) for product, quantity in orders]

    total_items = sum(quantity for _, quantity in orders)

    bakery_orders_count = sum(1 for product, _ in orders if product == 'Pékáru')

    more_than_3 = [(product, quantity) for product, quantity in orders if quantity > 3]

    product_totals = {}
    for product, quantity in orders:
        product_totals[product] = product_totals.get(product, 0) + quantity

    most_ordered_product = max(product_totals, key=product_totals.get)

    with open('03_eredmeny.txt', 'w', encoding='utf-8') as f:
        f.write(f'total orderes items {total_items}')
        # bakery_orders_count
        for product, quantity in more_than_3:
            f.write(f'{product};{quantity}')
        f.write(f'most ordered product {most_ordered_product}\n')

def task_04():
    # beolvas ua.
    # TODO: szét szedni függvényekre a beolvasást (egyre)
    # TODO: újra felhasználni
    books = []

    # TODO: konvertálás ua.

    # (a, b) -> b int()
    loans_10_or_more = [b for b in books if b[1] >= 10]

    loans_less_than_10 = [b for b in books if b[1] < 10]

    most_popular_book = max(books, key=lambda x: x[1])

    # TODO: kiiratás...

def task_05():
    # TODO: beolvasás ua.

    runners = []

    # TODO: float konvertálni...

    avg_time = sum(time for _, time in runners) / len(runners)

    under_15 = [name for name, time in runners if time < 15]

    under_13_count = sum(1 for _, time in runners if time < 13)

    fastest_runner = min(runners, key=lambda x: x[1])

    slowest_runner = max(runners, key=lambda x: x[1])

    # TODO: kiiratás...

    with open('05_eredmney.txt', 'w', encoding='utf-8') as f:
        for name, time in runners:
            category = 'fast' if time < 15 else 'slow'
            f.write(f'{name};{time};{category}\n')

# TODO: main...