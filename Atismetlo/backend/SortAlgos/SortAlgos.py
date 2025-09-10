class SortAlgorithm(ABC):
    @abstractmethod
    def sort(self, data: List) -> List:
        pass


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

