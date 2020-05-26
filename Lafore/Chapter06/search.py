from typing import Optional

from Lafore.Chapter02.sorted_array import SortedArray


class SortedArrayWithRecursiveSearch(SortedArray):
    def find(self, search_key: int) -> Optional[int]:
        return self.rec_find(search_key, 0, len(self._state) - 1)

    def rec_find(self, search_key: int, lower: int, upper: int) -> Optional[int]:
        current_index = (lower + upper) // 2
        if self._state[current_index] == search_key:
            return current_index
        elif lower > upper:
            return None
        else:
            return self.rec_find(search_key, current_index+1, upper) if self._state[current_index] < search_key else self.rec_find(search_key, lower, current_index-1)


if __name__ == '__main__':
    array = SortedArrayWithRecursiveSearch(10)
    array._state = list(range(5, 55, 5))
    print(array.find(5))
    print(array.find(10))
    print(array.find(45))
    print(array.find(50))
    print(array.find(54))
