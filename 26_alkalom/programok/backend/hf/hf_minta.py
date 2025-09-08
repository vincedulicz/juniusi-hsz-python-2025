import argparse
import os.path
from typing import List, Optional

class FileHandler:
    """ fájlkezelés műveletek """
    @staticmethod
    def read_file(file_path: str) -> List[str]:
        """ beolvassa a fájlt """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f'Hiba: {file_path} nem található')
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()

    @staticmethod
    def write_file(file_path: str, lines: List[str]) -> None:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)

class LineFilter:
    """ sorok szűréséért felelős """
    @staticmethod
    def filter_lines(lines: List[str], keyword: Optional[str]) -> List[str]:
        return [line for line in lines if keyword in line] if keyword else lines


class CLIHandler:
    """ parancssori arg kezelő """
    @staticmethod
    def parse_arguments() -> argparse.Namespace:
        parser = argparse.ArgumentParser(description="Szöveges fájl sorainak szűrése keyword alapján")
        parser.add_argument("--input", required=True, help="A bemeneti szöveges fájl neve")
        parser.add_argument("--filter", required=False, help="Szűréshez használt keyword")
        parser.add_argument("--output", required=False, help="Az output fájl neve -> szűrt sorok kerülnek bele")

        return parser.parse_args()


class App:
    def __init__(self,
                 input_file: str,
                 filter_word: Optional[str] = None,
                 output_file: Optional[str] = None):

        self._input_file = input_file
        self._filter_word = filter_word
        self._output_file = output_file

    @property
    def input_file(self) -> str:
        return self._input_file

    @property
    def filter_word(self) -> Optional[str]:
        return self._filter_word

    @property
    def output_file(self) -> Optional[str]:
        return self._output_file

    def run(self) -> None:
        try:
            lines = FileHandler.read_file(self.input_file)
            filtered_lines = LineFilter.filter_lines(lines, self.filter_word)

            if self.output_file:
                FileHandler.write_file(self.output_file, filtered_lines)
                print(f"A szűrt sorok mentve ide: {self.output_file}")
            else:
                print("Szűrt sorok")
                for line in filtered_lines:
                    print(line.strip())
        except FileNotFoundError as e:
            print(e)
            exit(1)

def main():
    args = CLIHandler.parse_arguments()
    app = App(input_file=args.input, filter_word=args.filter, output_file=args.output)
    app.run()


main()
