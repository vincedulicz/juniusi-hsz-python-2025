import itertools
import math
import statistics
import copy
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class BuiltInMethods:
    @staticmethod
    def abs_and_sum():
        print(abs(-10))
        print(sum([1, 2, 3]))

    @staticmethod
    def min_and_max():
        print(min(3, 7, 2))
        print(max(3, 7, 2))

    @staticmethod
    def pow_and_round():
        print(pow(2, 3))
        print(round(3.1415192594, 2))

    @staticmethod
    def add_example():
        print(len([1, 2, 3]))
        print(type(123))
        print(sorted([3, 1, 2]))
        # all() -> minden érték True?
        print(all([True, True, False]))
        # any() -> van legalább egy True?
        print(any([False, False, True]))

class MathAndStat:
    @staticmethod
    def math_examples():
        print(math.sqrt(16))
        print(math.pi)
        print(math.factorial(5))

    @staticmethod
    def stat_examples():
        data = [1, 2, 3, 4, 5, 6]
        print(statistics.mean(data))
        print(statistics.median(data))
        print(statistics.stdev(data))

    @staticmethod
    def numpy_example():
        array = np.array([1, 2, 3, 4, 5, 6])
        print(np.mean(array))
        print(array.reshape(2, 3))

    @staticmethod
    def pandas_example():
        df = pd.DataFrame(
            {"Name": ["A", "B"],
             "Score": [90, 80]}
        )
        print(df.head())

    @staticmethod
    def itertools_example():
        combinations = list(itertools.combinations([1, 2, 3], 2))
        print("comb. [1,2,3]", combinations)

    @staticmethod
    def matplotlib_example():
        plt.plot([1, 2, 3], [4, 5, 6])
        plt.title("example plot")
        plt.show()


class CopiesDemo:
    @staticmethod
    def copy_example():
        # sekély másolat (a belső lista hivatkozás marad!)
        original = [1, 2, [3, 4]]
        shallow = copy.copy(original)
        shallow[2][0] = 99  # módosítjuk a belső listát
        print("originial after shallow copy", original)

    @staticmethod
    def deepcopy_example():
        # mély másolat (minden szint újramásolva)
        original = [1, 2, [3, 4]]
        deep = copy.deepcopy(original)
        deep[2][0] = 99  # itt NEM módosul az eredeti
        print("originial after shallow copy", original)
        print(id(original))  # memóriacím az eredetire
        print(id(deep))      # memóriacím a másolatra

class MatplotlibExercise:
    def line_plot(self):
        x = [1, 2, 3, 4]
        y = [10, 20, 25, 30]
        plt.plot(x, y)
        plt.title("alap vonaldiagram")
        plt.xlabel("x tengely")
        plt.ylabel("y tengely")
        plt.show()

    def bar_plot(self):
        categories = ['A', 'B', 'C', 'D']
        values = [3, 7, 2, 5]
        plt.bar(categories, values)
        plt.title("oszlopdiagram")
        plt.xlabel("kategóriák")
        plt.ylabel("értékek")
        plt.show()

    def histogram_plot(self):
        data = [1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7, 6, 7, 8]
        plt.hist(data, edgecolor='black', bins=5)
        plt.title('hisztogram')
        plt.xlabel("értékek")
        plt.ylabel("gyakoriság")
        plt.show()

    def scatter_plot(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        plt.scatter(x, y, color='red')
        plt.title("szórásdiagram")
        plt.xlabel("x értékek")
        plt.ylabel("y értékek")
        plt.show()

    def multiple_line_plot(self):
        x = [1, 2, 3, 4, 5]
        y1 = [2, 4, 6, 8, 10]
        y2 = [1, 2, 3, 4, 5]
        plt.plot(x, y1, label='Line 1', color='blue')
        plt.plot(x, y2, label='Line 2', color='green')
        plt.title("több vonaldiagram")
        plt.xlabel("x tengely")
        plt.ylabel("y tengely")
        plt.legend()
        plt.show()

    def save_plot(self):
        x = [1, 2, 3, 4, 5]
        y = [10, 20, 30, 40, 50]
        plt.plot(x, y)
        plt.title("ábra mentése")
        plt.xlabel("x tengely")
        plt.ylabel("y tengely")
        plt.savefig("plot_example.png")
        plt.close()

    def grid_plot(self):
        x = [1, 2, 3, 4, 5]
        y = [5, 6, 7, 8, 9]
        plt.plot(x, y)
        plt.grid(True)
        plt.title("rács beállítása")
        plt.xlabel("x tengely")
        plt.ylabel("y tengely")
        plt.show()

    def subplot_example(self):
        x = [1, 2, 3, 4, 5]
        y = [1, 4, 9, 16, 25]
        fig, axs = plt.subplots(2, 1)
        axs[0].plot(x, y)
        axs[0].set_title("első szubgrafikon")
        axs[1].scatter(x, y, color='green')
        axs[1].set_title("második szubgrafikon")
        plt.tight_layout()
        plt.show()


def main():
    print("builtin methods:")
    BuiltInMethods.abs_and_sum()
    BuiltInMethods.min_and_max()
    BuiltInMethods.pow_and_round()
    BuiltInMethods.add_example()

    print("math & stat:")
    MathAndStat.math_examples()
    MathAndStat.stat_examples()
    MathAndStat.numpy_example()
    MathAndStat.pandas_example()
    MathAndStat.itertools_example()
    MathAndStat.matplotlib_example()

    print("copy vs deepcopy:")
    CopiesDemo.copy_example()
    CopiesDemo.deepcopy_example()

    exercise = MatplotlibExercise()
    exercise.line_plot()
    exercise.bar_plot()
    exercise.histogram_plot()
    exercise.scatter_plot()
    exercise.multiple_line_plot()
    exercise.save_plot()
    exercise.grid_plot()
    exercise.subplot_example()


main()
