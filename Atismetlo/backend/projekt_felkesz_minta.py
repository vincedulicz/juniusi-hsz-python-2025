from abc import ABC, abstractmethod
from typing import List, Callable
import argparse
import time


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