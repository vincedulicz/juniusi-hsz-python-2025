import re
from collections.abc import Iterable # list string tuple ...

def get_length(item):
    """ Megnézi, hogy a paraméter iterálható-e és vissza adja a hosszát """
    if isinstance(item, Iterable):
        return len(item)
    else:
        return "nem iterálható"

#print(get_length("hello"))
#print(get_length([1,2,3]))
#print(get_length(213))




def my_decorator(func):
    def wrapper():
        print("ez a van függvényhívás előtt")
        func()
        print("ez van a függvényhívás után")
    return wrapper

@my_decorator
def say_hello():
    print("hello")


# say_hello()



gyumi = [("apple", 50), ("banana", 10), ("cherry", 30)]

sorted_list = sorted(gyumi, key=lambda x: x[1])
print(sorted_list)

my_list = [1,2,3,4,5,6]
odd_numbers = list(filter(lambda x: x % 2 != 0, my_list))
print(odd_numbers)


teszt_list = list(map(lambda x: x**2, my_list))
print(teszt_list)

square = lambda x: x**2
print(square(5))

# user@domain.com -> pelda.elek@mail-server-example.com

email_minta = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
email_szoveg = "az email cím: nemvalid@.email.h pelda.elek@mail-server-example.com user@domain.com info@test.org."

talalatok = re.findall(email_minta, email_szoveg)
print(talalatok)