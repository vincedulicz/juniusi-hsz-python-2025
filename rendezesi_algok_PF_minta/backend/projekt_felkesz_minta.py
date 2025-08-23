from abc import ABC, abstractmethod
from typing import List, Callable
import argparse
import time


#
# allIn1File - todo: pkg, print kezelés, komment kivezetés
#

# ---- STRATÉGIAI MINTA ALAPOSZTÁLY ----
class SortAlgorithm(ABC):
    @abstractmethod
    def sort(self, data: List) -> List:
        pass


# ---- KONKRÉT RENDEZÉSI ALGORITMUSOK ----
class QuickSort(SortAlgorithm):
    def sort(self, data: List) -> List:
        if len(data) <= 1:
            return data
        pivot = data[0]
        left = [x for x in data[1:] if x <= pivot]
        right = [x for x in data[1:] if x > pivot]

        return self.sort(left) + [pivot] + self.sort(right)


class MergeSort(SortAlgorithm):
    def sort(self, data: List) -> List:
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])

        return self._merge(left, right)

    @staticmethod
    def _merge(left: List, right: List) -> List:
        result = []
        while left and right:
            result.append(left.pop(0) if left[0] < right[0] else right.pop(0))

        return result + left + right


class CombSort(SortAlgorithm):
    def sort(self, data: List) -> List:
        return NotImplementedError


class BinaryInsertionSort(SortAlgorithm):
    def sort(self, data: List) -> List:
        data = data[:]
        for i in range(1, len(data)):
            key, left, right = data[i], 0, i
            while left < right:
                mid = (left + right) // 2
                if data[mid] < key:
                    left = mid + 1
                else:
                    right = mid
            data = data[:left] + [key] + data[left:i] + data[i + 1:]

        return data


# ---- IDŐMÉRÉS ----
class ExecutionTimer:
    @staticmethod
    def measure_time(func: Callable, data: List) -> tuple:
        start = time.perf_counter()
        result = func(data)
        end = time.perf_counter()

        return result, end - start


# ---- FÁJLKEZELÉS ----
class FileProcessor:
    @staticmethod
    # TODO: biztos jó ez így?
    def read_file(filename: str) -> List:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = []
                for line in file.readlines():
                    # Ellenőrizzük, hogy a sor konvertálható-e int-re
                    try:
                        data.append(int(line.strip()))
                    except ValueError:
                        # Ha nem, akkor stringként tároljuk
                        data.append(line.strip())
                return data
        except FileNotFoundError:
            print(f"Hiba: {filename} nem található.")
            return []

    @staticmethod
    def write_file(filename: str, data: List):
        # TODO: hibakezelés
        with open(filename, 'w', encoding='utf-8') as file:
            if isinstance(data[0], int):  # Ha számok vannak, akkor integerként írjuk
                file.write('\n'.join(map(str, data)))
            else:  # Egyéb esetben sima szövegként
                file.write('\n'.join(data))


# ---- RENDEZÉSI FÜGGVÉNY ----
class SortingData:
    """ TODO: app osztály """

    @staticmethod
    def sort_file(input_file: str, output_file: str, algorithm: SortAlgorithm):
        data = FileProcessor.read_file(input_file)

        if data:
            sorted_data, duration = ExecutionTimer.measure_time(algorithm.sort, data)
            FileProcessor.write_file(output_file, sorted_data)
            print(f"Rendezés {algorithm.__class__.__name__}-vel: {duration:.6f} mp")


# ---- ARGUMENTUMPARSING ----
def main():
    # TODO: app osztály
    parser = argparse.ArgumentParser()

    parser.add_argument('--input', required=True, help='Bemeneti fájl neve')
    parser.add_argument('--output', required=True, help='Kimeneti fájl neve')
    parser.add_argument('--algorithm', required=True,
                        choices=['quick_sort', 'merge_sort', 'comb_sort', 'binary_insertion_sort'],
                        help='Rendezési algoritmus')

    args = parser.parse_args()

    algorithms = {
        'quick_sort': QuickSort(),
        'merge_sort': MergeSort(),
        'comb_sort': CombSort(),
        'binary_insertion_sort': BinaryInsertionSort()
    }

    SortingData.sort_file(args.input, args.output, algorithms[args.algorithm])


if __name__ == "__main__":
    main()
