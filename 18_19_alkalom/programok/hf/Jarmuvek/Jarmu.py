from abc import ABC, abstractmethod
from TESZTER.hf.JarmuAlkatreszek.Motor import Motor
from TESZTER.hf.JarmuAlkatreszek.Kerek import Kerekek
class Jarmu(ABC):
    def __init__(self, tipus, gyarto, evjarat, motor_tipus="V12", kerekek_szama=4):
        self._tipus = tipus
        self._gyarto = gyarto
        self.evjarat = evjarat
        self.motor = Motor(motor_tipus)
        self.kerekek = Kerekek(kerekek_szama)

    @property
    def tipus(self):
        return self._tipus

    @tipus.setter
    def tipus(self, new_tipus):
        self._tipus = new_tipus

    @property
    def gyarto(self):
        return self._gyarto

    def __str__(self):
        return f'{self.gyarto} - {self.tipus}'

    @abstractmethod
    def jarmu_adatok(self):
        pass