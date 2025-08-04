class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f'{self.name} a {self.breed} ugat: Vau vau')

doge = Dog("Bodri", "puli")
doge.bark()

class Vehicle:
    def __init__(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("az autó megy")

car = Car()
car.drive()

class Animal:
    def speak(self):
        pass

# dog cat leopárd

# TODO: kiegészítés
def make_animal_speak(animal: Animal):
    animal.speak()

make_animal_speak(Dog())

class Logger:
    pass

class Service:
    # mint példányváltozó
    def create(self):
        self.logger.log()


# engine: start ... motor goes brrr

class Car:
    pass
# példányként (var) engine

    def elindul(self):
        self.engine.start()


class Person:
    OSZTALY_VALTOZO = {}

    def __init__(self, id):
        self.__id = id
        self._labujjmerethosszsanakafele = 0

    # getter
    @property
    def labujjmerethosszsanakafele(self):
        return self._labujjmerethosszsanakafele

    @labujjmerethosszsanakafele.setter
    def labujjmerethosszsanakafele(self, value):
        if value < 0 and value is not None:
            print("nem adhatsz meg ilyen értéket")
        else:
            self._labujjmerethosszsanakafele = value
