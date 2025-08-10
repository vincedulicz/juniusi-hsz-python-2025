from TESZTER.hf.Jarmuvek.Jarmu import Jarmu

class DataProcess:
    @staticmethod
    def szures_evjarat_alapjan(jarmuvek: list[Jarmu], min_evjarat: int) -> list[Jarmu]:
        return [j for j in jarmuvek if j.evjarat >= min_evjarat]

    @staticmethod
    def van_e_megfelelo_jarmu(jarmuvek: list[Jarmu], min_evjarat: int) -> bool:
        return any(j.evjarat >= min_evjarat for j in jarmuvek)
