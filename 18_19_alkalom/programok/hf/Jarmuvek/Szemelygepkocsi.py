from TESZTER.hf.Jarmuvek.Jarmu import Jarmu

class Szemelygepkocsi(Jarmu):
    def __init__(self, tipus, gyarto, evjarat, motor, kerekek, ajtok_szama):
        super().__init__(tipus, gyarto, evjarat, motor, kerekek)
        self._ajtok_szama = ajtok_szama

    @property
    def ajtok_szama(self):
        return self._ajtok_szama

    def jarmu_adatok(self):
        return {
            "tipus": self.tipus,
            "gyarto": self.gyarto,
            "evjarat": self.evjarat,
            "motor_tipus": self.motor.tipus,
            "kerekek_szama": self.kerekek.darabszam,
            "ajtok_szama": self.ajtok_szama
        }