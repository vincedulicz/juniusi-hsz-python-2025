class Motor:
    def __init__(self, teljesitmeny):
        self.__teljesitmeny = teljesitmeny

    def __str__(self):
        return f'ez egy motor objektum'

    def motor_info(self):
        return f'motor tej.: {self.teljesitmeny}'

    @property
    def teljesitmeny(self):
        print("getter")
        return self.__teljesitmeny

    @teljesitmeny.setter
    def teljesitmeny(self, value):
        print("setter")
        self.__teljesitmeny = value

"""
motor2 = Motor(120)
print(motor2)
print(motor2.teljesitmeny)
motor2.teljesitmeny = 121
print(motor2.teljesitmeny)
"""



class Auto:
    def __init__(self, marka, motor):
        self.marka = marka
        self.motor = motor

    def __eq__(self, other):
        if isinstance(other, Auto):
            return self.marka == other.marka
        return False

    def auto_info(self):
        return f'márka: {self.marka}, {self.motor.motor_info()}'

motor = Motor(120)
auto = Auto("toyota", motor)

motor2 = Motor(110)
auto2 = Auto("toyota", motor2)

print(auto == auto2)

