"""5.6 programming project"""
from typing import Any
from Lafore.Chapter05.linked_list import LinkedList


class _ArrayNode(LinkedList):
    def __init__(self, size: int) -> None:
        super().__init__()
        self._pointer = None
        for _ in range(size):
            self.insert_first(None)

    def __getitem__(self, item: int) -> Any:
        current = self.first
        for index in range(item):
            if current.next is None:
                raise IndexError('Out of index')
            current = current.next
        return current.data

    def __setitem__(self, key: int, value: Any) -> None:
        current = self.first
        for index in range(key):
            if current.next is None:
                raise IndexError('Out of index')
            current = current.next
        current.data = value

    def __iter__(self):
        self._pointer = self.first
        return self

    def __next__(self):
        if self._pointer is not None:
            result = self._pointer
            self._pointer = self._pointer.next
            return result
        else:
            raise StopIteration


class TwoDimensionalArray:
    def __init__(self, *, rows: int, cols: int) -> None:
        self._state = _ArrayNode(rows)
        for row in self._state:
            row.data = _ArrayNode(cols)

    def __getitem__(self, item: int) -> _ArrayNode:
        return self._state[item]

    def __setitem__(self, key, value) -> None:
        self._state[key] = value

    def __str__(self) -> str:
        return '\n'.join(str(row) for row in self._state)


if __name__ == '__main__':
    rows, cols = 10, 7
    array = TwoDimensionalArray(rows=rows, cols=cols)
    element = 0
    for row_index in range(rows):
        for col_index in range(cols):
            array[row_index][col_index] = element
            element += 1
    print(array)
