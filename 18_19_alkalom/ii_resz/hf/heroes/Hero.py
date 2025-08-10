from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, hp, level):
        self.name = name
        self._hp = hp
        self.level = level
        self._damage: Damage = None

    @abstractmethod
    def attack(self):
        pass

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f'{self.name} has {self.hp} HP left\n')

    def is_alive(self) -> bool:
        return self.hp > 0

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, value)

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value: Damage):
        self._damage = value

    def __str__(self):
        pass

    def __repr__(self):
        pass