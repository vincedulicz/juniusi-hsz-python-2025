def csv_orai():
    import csv

    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["név", "kor", "város"]) # fejléc
        writer.writerows([
            ['anna', 25, "bp"],
            ['anna2', 27, "bp2"],
            ['anna3', 26, "bp3"],
        ])

    with open('output.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

    with open('output_dict.csv', "w", newline='', encoding='utf-8') as csvfile:
        filednames = ["név", "kor", "város"]
        writer = csv.DictWriter(csvfile, fieldnames=filednames)
        writer.writeheader()
        writer.writerow({'név': "anna", "kor": 25, "város": "bp"})

    with open('output_dict.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(type(row))
            print(row)
            # név: {row["Név"]}

csv_orai()

