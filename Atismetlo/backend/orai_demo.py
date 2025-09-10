import sys

x_int = 42
x_float = 3.14
z_complex = 2 + 3j
s_string = "hello world"
b_bool = True

print(type(x_int))

my_list = [1, 2, 3, 4]
my_list.append(5)
print(my_list, my_list[0], my_list[1:4])

my_tuple = (10, 20, 30)
print(my_tuple[0])

my_dict = {"név": "Anna", "kor": 25}
my_dict["varos"] = "Budapest"

print(my_dict)

my_set = {1, 2, 3}
my_set.add(4)
print("set:", my_set)


text = "hello world"
print(text[0:6], text.split(), text.find("hello"))
print(f'{text}... {len(text)}')

a, b = 10, 3
print("aritmetikai", a+b, a-b, a*b, a/b, a%b, a**b)
print("össz", a==b, a!=b, a>b, a<b, a>=b, a<=b)
print("logikai", True and False, True or False, not True)



for i in range(5):
    if i == 3:
        continue
    print("i", i)


i = 0
while i < 5:
    print("while", i)
    i += 1


s_even = [x**2 for x in range(10) if x % 2 == 0]

def osszeg(a, b):
    return a + b


def lista_atlag(lst):
    return sum(lst) / len(lst)


import math
from math import sin

print(math.sqrt(16))

import random
print(random.randint(1, 100))


with open("data/data.txt", "w", encoding="utf-8") as file:
    file.write("írás")

with open("data/data.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("tartalom", content)


try:
    x = int("abc")
except ValueError as e:
    print("hiba", e)
finally:
    print("try-catch blokk vége")


class MyError(Exception):
    pass

try:
    raise MyError("saját kivétel osztály")
except MyError as e:
    print("saját kivétel", e)



class Auto:
    tipus = "ism" # class attr
    def __init__(self, marka):
        self.marka = marka # public
        self._ev = None # protected
        self.__tipus = None # private

    def info(self):
        return f"marka {self.marka}"


class ElektroAuto(Auto):
    def __init__(self, marka):
        super().__init__(marka)
        self.akku = None

    def info(self):
        return f"{self.akku}"


a1 = Auto("t")
a1.info()



adatok = []
while True:
    nev = input("adjá nevet (exit-kilépés): ")
    if nev.lower() == "exit":
        break
    try:
        kor = int(input("adjá kort: "))
    except ValueError:
        print("hiba! számot adjá meg")
        continue
    adatok.append({"nev": nev, "kor": kor})


with open("data/adatok.txt", "w") as file:
    for d in adatok:
        file.write(f'{d["nev"]}, {d["kor"]}\n')



with open("data/adatok.txt", "r") as file:
    for line in file:
        line = line.strip()
        if re.match(r'^[A-Za-z]+,\d+$'):
            print("érvényes sor", line)
        else:
            print("érvénytelen sor", line)


korok = [d["kor"] for d in adatok]
print(f"összes sor {korok}, átlag: {sum(korok) / len(korok) if korok else 0}")





# ---------- start vizsga minta IV/A ------------- #

import json
import re

def is_valid_email(email: str) -> bool:
    return bool(re.match(r"^[^@]+@[^@]+\.[^@]+$", email))

def filter_valid_users(filename: str) -> list:
    with open(filename, "r", encoding='utf-8') as file:
        users = json.load(file)

    return [
        user for user in users
        if user.get("age", 0) >= 18 and is_valid_email(user.get("email", ""))
    ]

# ---------- end vizsga minta IV/A ------------- #



# ---------- start vizsga minta IV/B ------------- #

import unittest
from unittest.mock import patch

def get_weather(city: str):
    raise NotImplementedError("api hívás itt lenne")

class TestWeatherAPI(unittest.TestCase):
    @patch("__main__.get_weather")
    def test_city_name(self, mock_weather):
        mock_weather.return_value = {"city": "Budapest", "temp": 22}
        result = get_weather("Budapest")
        self.assertEqual(result["city"], "Budapest")

    @patch("__main__.get_weather")
    def test_temperature_type(self, mock_weather):
        mock_weather.return_value = {"city": "Pécs", "temp": 25}
        result = get_weather("Pécs")
        self.assertIsInstance(result["temp"], int)

    @patch("__main__.get_weather")
    def test_invalid_city(self, mock_weather):
        mock_weather.side_effect = ValueError("Érvénytelen város")
        with self.assertRaises(ValueError):
            get_weather("InvalidCity")

if __name__ == "__main__":
    unittest.main()


# ---------- end vizsga minta IV/B ------------- #














