from typing import Optional


class HashTable:
    def __init__(self, size: int = 8) -> None:
        self._size = size
        self._hash_array = [None for _ in range(size)]
        self._DUMMY = float('nan')

    def __str__(self) -> str:
        return str(self._hash_array)

    def hash_func(self, key: int) -> int:
        return key % self._size

    def insert(self, item: int) -> None:
        hash_index = self.hash_func(item)
        while self._hash_array[hash_index] is not None and self._hash_array[hash_index] is not self._DUMMY:
            hash_index += 1
            hash_index = 0 if hash_index == self._size else hash_index
        self._hash_array[hash_index] = item

    def delete(self, item: int) -> Optional[int]:
        hash_index = self.hash_func(item)
        while self._hash_array[hash_index] is not None:
            if self._hash_array[hash_index] == item:
                result = self._hash_array[hash_index]
                self._hash_array[hash_index] = self._DUMMY
                return result
            hash_index += 1
            hash_index = 0 if hash_index == self._size else hash_index
        return None

    def find(self, item) -> Optional[int]:
        hash_index = self.hash_func(item)
        while self._hash_array[hash_index] is not None:
            if self._hash_array[hash_index] == item:
                return self._hash_array[hash_index]
            hash_index += 1
            hash_index = 0 if hash_index == self._size else hash_index
        return None


class DoubleHashTable:
    def __init__(self, size: int = 8) -> None:
        self._size = size
        self._hash_array = [None for _ in range(size)]
        self._DUMMY = float('nan')

    def __str__(self) -> str:
        return str(self._hash_array)

    def hash_func_first(self, key: int) -> int:
        return key % self._size

    def hash_func_second(self, key: int) -> int:
        return 5 - key % 5

    def insert(self, item: int) -> None:
        hash_index = self.hash_func_first(item)
        hash_step = self.hash_func_second(item)
        while self._hash_array[hash_index] is not None and self._hash_array[hash_index] is not self._DUMMY:
            hash_index += hash_step
            hash_index = 0 if hash_index == self._size else hash_index
        self._hash_array[hash_index] = item

    def delete(self, item: int) -> Optional[int]:
        hash_index = self.hash_func_first(item)
        hash_step = self.hash_func_second(item)
        while self._hash_array[hash_index] is not None:
            if self._hash_array[hash_index] == item:
                result = self._hash_array[hash_index]
                self._hash_array[hash_index] = self._DUMMY
                return result
            hash_index += hash_step
            hash_index = 0 if hash_index == self._size else hash_index
        return None

    def find(self, item) -> Optional[int]:
        hash_index = self.hash_func_first(item)
        hash_step = self.hash_func_second(item)
        while self._hash_array[hash_index] is not None:
            if self._hash_array[hash_index] == item:
                return self._hash_array[hash_index]
            hash_index += hash_step
            hash_index = 0 if hash_index == self._size else hash_index
        return None


if __name__ == '__main__':
    data = DoubleHashTable(15)
    data.insert(54)
    data.insert(65)
    print(data)
    data.insert(76)
    data.delete(65)
    print(data)
    data.insert(87)
    data.insert(44)
    print(data)
    data.delete(76)
    print(data.find(44))
    print(data)