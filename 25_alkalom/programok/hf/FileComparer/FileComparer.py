from _hf_25.hf.TextComparer.TextComparerABC import TextComparer
from _hf_25.hf.TextProcessor.TextProcessor import TextProcessor

class FileComparer:
    def __init__(self, comparer: TextComparer):
        self.processor = TextProcessor()
        self.comparer = comparer

    def compare_files(self, file1: str, file2: str) -> float:
        """ compare the content of the 2 files """
        try:
            text1 = self.processor.prepare_text(
                self.processor.load_file(file1)
            )
            text2 = self.processor.prepare_text(
                self.processor.load_file(file2)
            )

            return self.comparer.compare_texts(text1, text2)
        except RuntimeError as e:
            print(e)
            return 0.0
