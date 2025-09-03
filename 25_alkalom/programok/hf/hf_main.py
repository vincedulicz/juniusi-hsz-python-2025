from _hf_25.hf.FileComparer.FileComparer import FileComparer
from _hf_25.hf.ResultPrinter.ResultPrinter import ResultPrinter
from _hf_25.hf.TextComparer.CharTextComparer import CharTextComparer
from _hf_25.hf.TextComparer.SimpleTextComparer import SimpleTextComparer

def main():
    file1 = "data/407.txt"
    file2 = "data/408.txt"

    word_comparer = FileComparer(SimpleTextComparer())
    word_result = word_comparer.compare_files(file1, file2)

    printer = ResultPrinter()
    printer.print_result(word_result, "word-level")

    char_comparer = FileComparer(CharTextComparer())
    char_result = char_comparer.compare_files(file1, file2)

    printer.print_result(char_result, "char-level")


main()
