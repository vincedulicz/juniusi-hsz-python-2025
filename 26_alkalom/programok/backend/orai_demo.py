from abc import ABC, abstractmethod

class Animal:
    kingdom = "Animals" # class attribute -> minden példánynál azonos

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "animal sound"


a1 = Animal("generic", 5)
print(f'{a1.name} is {a1.age} years old {a1.kingdom} kingdom')



class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.__breed = breed

    # oldschool...
    def get_breed(self):
        return self.__breed

    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, new_breed):
        if not new_breed:
            raise ValueError("cannot be empty")
        self.__breed = new_breed

    def speak(self):
        return "woof"

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        return f"car move {self.brand}"

class Plane(Vehicle):
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        return f"plane move {self.brand}"



class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def __str__(self):
        return f"{self.horsepower} hp"

    def start(self):
        return f'engine {self.horsepower} hp starts'


class Bus(Vehicle):
    def __init__(self, brand, horsepower, seats):
        self.brand = brand
        self.engine = Engine(horsepower)
        self.seats = seats

    def move(self):
        return f'bus... {self.brand} .. {self.engine} .. {self.seats}. {self.engine.start()}'

def main():
    dog1 = Dog("Bodri", 3, "Puli")
    print(dog1.speak())             # Polymorphism
    print(dog1.get_breed())         # Encapsulation régi getterrel
    print(dog1.breed)               # Property getter -> úgy használom, mintha sima attribútum lenne
    dog1.breed = "Mudi"             # Property setter
    print(dog1.breed)               # "Mudi"
    print(dog1.kingdom)             # Class attribute öröklődik

    vehicles = [Car("toyota"), Plane("airbus2000"), Bus("volvo", 300, 50)]
    for v in vehicles:
        print(v.move())

main()
