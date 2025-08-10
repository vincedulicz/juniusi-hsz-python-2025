from TESZTER.hf.Autopark.Autopark import Autopark
from TESZTER.hf.Jarmuvek.Szemelygepkocsi import Szemelygepkocsi
from TESZTER.hf.Jarmuvek.Teherauto import Teherauto
from TESZTER.hf.Dataprocess.Dataprocess import DataProcess as dp

if __name__ == "__main__":
    autopark = Autopark()

    fajlnev = "autopark.json"
    autopark.betoltes_fajlbol(fajlnev)

    auto = Szemelygepkocsi("sedan", "toyota", 2020, "v6", 4, 700)
    auto2 = Teherauto("kamiom", "volvo", 2018, "v120", 8, 12000)

    autopark.jarmu_hozzadas(auto)
    autopark.jarmu_hozzadas(auto2)

    autopark.mentes_fajlba(fajlnev)

    szurt_jarmuvek = dp.szures_evjarat_alapjan(autopark.jarmuvek, 2019)
    for jarmu in szurt_jarmuvek:
        print(jarmu.jarmu_adatok())

    if dp.van_e_megfelelo_jarmu(autopark.jarmuvek, 2020):
        print("van illen")
    else:
        print("nincsen :C")