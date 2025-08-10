from TESZTER.hf.Jarmuvek.Jarmu import Jarmu

class Teherauto(Jarmu):
    def __init__(self, tipus, gyarto, evjarat, motor, kerekek, teherbiras):
        super().__init__(tipus, gyarto, evjarat, motor, kerekek)
        self.teherbiras = teherbiras

    def jarmu_adatok(self):
        return {
            "tipus": self.tipus,
            "gyarto": self.gyarto,
            "evjarat": self.evjarat,
            "motor_tipus": self.motor.tipus,
            "kerekek_szama": self.kerekek.darabszam,
            "teherbiras": self.teherbiras
        }

    def szerviz_adatok(self):
        return {
            "gyarto": self.gyarto,
            "motor": self.motor
        }