from abc import ABC, abstractmethod

class TextComparer(ABC):
    @staticmethod
    @abstractmethod
    def compare_texts(text1: str, text2: str) -> float:
        """ compare two texts return their similarityx in %"""
        pass
