import numpy as np
import matplotlib.pyplot as plt


class NumpyFeladatok:
    @staticmethod
    def matrix_manipulacio():
        matrix = np.random.randint(1, 101, size=(4, 4))

        print("4x4 mátrix:\n", matrix)
        print("Főátló összege\n", np.trace(matrix))
        print("Mátrix transzponált\n", matrix.T)

    @staticmethod
    def vektor_muveletek():
        v1 = np.random.randint(0, 51, size=6)
        v2 = np.random.randint(0, 51, size=6)

        print("Vektor 1:", v1)
        print("Vektor 2:", v2)
        print("Összeg", v1 + v2)
        print("különbség", v1 - v2)
        print("elemnkénti szorzat", v1 * v2)

    @staticmethod
    def adathalmaz_statisztika():
        data = np.random.randint(1, 101, size=1000)
        print("adathalmaz", data)
        print("átlag", np.mean(data))
        print("medián", np.median(data))
        print("szórás", np.std(data))
        print("max", np.max(data))
        print("min", np.min(data))

    @staticmethod
    def maszkolas():
        data = np.random.randint(1, 101, size=10)
        print("eredti tomb", data)
        data[data % 2 != 0] = 0
        print("maszkolt tömb (páratlanok 0)", data)

    @staticmethod
    def matrix_szorzasa():
        m1 = np.random.randint(1, 11, size=(3, 3))
        m2 = np.random.randint(1, 11, size=(3, 3))
        print(f"mátrix1: {m1} | mátrix2: {m2}")
        print("mátrixszorzat", np.dot(m1, m2))

    @staticmethod
    def felteteles_modositas():
        matrix = np.random.randint(1, 101, size=(5, 5))
        print("eredeti mátrix", matrix)
        matrix[matrix > 50] = 100
        print("modify matrix:", matrix)

    @staticmethod
    def sinus_koszinus_gorbe():
        x = np.arange(0, 2 * np.pi, 0.1)
        sin_vals = np.sin(x)
        cos_vals = np.cos(x)
        plt.plot(x, sin_vals, label='sinus')
        plt.plot(x, cos_vals, label='koszinus')
        plt.legend()
        plt.title("Sinus és Koszinus görbék")
        plt.show()

    @staticmethod
    def sor_oszlop_atlag():
        matrix = np.random.randint(1, 101, size=(6, 6))
        print("matrix", matrix)
        print("sorok átlaga", np.mean(matrix, axis=1))
        print("oszlop átlaga", np.mean(matrix, axis=0))
