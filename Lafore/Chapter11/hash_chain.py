from typing import List, Optional

from Lafore.Chapter05.linked_list import LinkedList


class HashChainTable:
    def __init__(self, size: int = 8) -> None:
        self._size = size
        self._hash_array: List[LinkedList] = [LinkedList() for _ in range(size)]

    def __str__(self) -> str:
        return '\n'.join(str(item) for item in self._hash_array)

    def hash_func(self, key: int) -> int:
        return key % self._size

    def insert(self, item: int) -> None:
        hash_index = self.hash_func(item)
        self._hash_array[hash_index].insert_first(item)

    def delete(self, item: int) -> Optional[int]:
        hash_index = self.hash_func(item)
        if self._hash_array[hash_index].first.data == item:
            return self._hash_array[hash_index].delete_first().data
        result = self._hash_array[hash_index].delete(item)
        return result if result is None else result.data

    def find(self, item: int) -> Optional[int]:
        hash_index = self.hash_func(item)
        result = self._hash_array[hash_index].find(item)
        return result if result is None else result.data


if __name__ == "__main__":
    data = HashChainTable(10)
    for value in range(0,100, 7):
        data.insert(value)
    data.delete(21)
    data.delete(91)

    print(data)