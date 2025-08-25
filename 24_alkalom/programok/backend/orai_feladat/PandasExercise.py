import pandas as pd
import numpy as np
from datetime import datetime

class PandasFeladatok:
    @staticmethod
    def dataframe_letrehozasa():
        df = pd.DataFrame(
            {"Név":
                 ["Anna", "Béla", "Cecil"],
             "Életkor":
                 [25, 30, 22],
             "Pontszám":
                 [85, 92, 78]
             }
        )
        print("df", df)
        atlag_pontszam = df["Pontszám"].mean()
        print("átlagpontszám", atlag_pontszam)
        szurt = df[df["Pontszám"] > atlag_pontszam]
        print("átlagnál jobb pontszámok:", szurt)

    @staticmethod
    def csv_beolvasas():
        df = pd.DataFrame(
                {"Név":
                     ["Anna", "Béla", "Cecil"],
                 "Életkor":
                     [25, 30, 22],
                 "Pontszám":
                     [85, 92, 78]
                 }
            )
        print("df", df)
        print("sorok száma", len(df))
        print("pontszám oszlop max", df["Pontszám"].max())
        print("pontszám oszlop min", df["Pontszám"].min())
        print("pontszám oszlop átlag", df["Pontszám"].mean())

    @staticmethod
    def csoportositas():
        df = pd.DataFrame({
            "Kategória": ["A", "A", "B", "B"],
            "Érték": [10, 20, 30, 40]
        })
        print("csoportosított átlagok", df.groupby("Kategória").mean())

    @staticmethod
    def hianyzo_kezeles():
        df = pd.DataFrame({"A": [1, 2, None], "B": [None, 5, 6]})
        print("eredeti df", df)
        df_filled = df.fillna(df.mean())
        print("hiányzó érték ki lett töltve", df_filled)

    @staticmethod
    def idosor_elemzes():
        dates = pd.date_range(start=datetime.today(), periods=10)
        values = np.random.randint(1, 101, size=10)
        df = pd.DataFrame({"Dátum": dates, "Érték": values})
        df["Mozgó átlag"] = df["Érték"].rolling(window=3).mean()
        print("idősor mozgóátlag", df)

    @staticmethod
    def felteteles_szures():
        df = pd.DataFrame({"A": [10, 20, 30], "B": [5, 15, 25]})
        szurt = df[df["A"] > 15]
        print("szűrt df", szurt)

    @staticmethod
    def adatok_modositasa():
        df = pd.DataFrame({"Érték": [10, 20, 30]})
        print("eredeti df", df)
        df["Érték"] *= 2
        print("modify df", df)

    @staticmethod
    def adatok_rendezese():
        df = pd.DataFrame({"Érték": [30, 10, 20]})
        print("rendezett df", df.sort_values(by="Érték", ascending=False))






