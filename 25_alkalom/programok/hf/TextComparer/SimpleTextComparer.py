from _hf_25.hf.TextComparer.TextComparerABC import TextComparer

class SimpleTextComparer(TextComparer):
    @staticmethod
    def compare_texts(text1: str, text2: str) -> float:
        """ Jaccard hasonlóság két text között """
        set1 = set(text1.split())
        set2 = set(text2.split())
        intersection = len(set1 & set2)
        union = len(set1 | set2)

        return (intersection / union) * 100 if union != 0 else 0.0
