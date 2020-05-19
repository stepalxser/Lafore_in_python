from __future__ import annotations

from typing import Optional, List


class SortedArray:
    def __init__(self, length: int) -> None:
        self._state: List[Optional[int]] = [None for _ in range(length)]
        self._length: int = length

    def __str__(self) -> str:
        return str(self._state)

    def size(self) -> int:
        return self._length

    def find(self, search_key: int) -> Optional[int]:
        start_index, end_index = 0, self._length - 1
        while True:
            middle_index = (start_index + end_index) // 2
            if self._state[middle_index] == search_key:
                return middle_index
            elif start_index > end_index:
                return None
            else:
                if self._state[middle_index] is not None and self._state[middle_index] < search_key:
                    start_index = middle_index + 1
                else:
                    end_index = start_index = middle_index - 1

    def insert(self, value: int) -> None:
        for index in range(self._length):
            if self._state[index] is None:
                self._state[index] = value
                return
            elif value < self._state[index]:
                insert_index: int = index
                break

        for index in range(self._length-1, insert_index-1, -1):
            if self._state[index] is None:
                continue
            self._state[index+1] = self._state[index]

        self._state[insert_index] = value

    def delete(self, value: int) -> bool:
        elem_index = self.find(value)
        if elem_index is None:
            return False

        self._state[elem_index] = None

        for index in range(elem_index+1, self._length):
            if self._state[index] is not None:
                self._state[index], self._state[index-1] = self._state[index-1], self._state[index]
            else:
                break
        return True

    # noinspection SpellCheckingInspection
    def megre(self, other: SortedArray) -> SortedArray:
        data = SortedArray(self.size() + other.size())
        for index in range(self._length):
            if self._state[index] is None:
                break
            data.insert(self._state[index])
        for index in range(other._length):
            if other._state[index] is None:
                break
            data.insert(other._state[index])
        return data


if __name__ == '__main__':
    array_1 = SortedArray(5)
    array_1._state = [0, 2, 4, 6, 8]
    array_2 = SortedArray(5)
    array_2._state = [1, 3, 5, 7, 9]
    array_3 = array_1.megre(array_2)
    print(array_3)
