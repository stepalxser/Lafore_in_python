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


# programming project 11.1
class QuadHashTable(HashTable):
    def insert(self, item: int) -> None:
        hash_index, hash_step = self.hash_func(item), 1
        while self._hash_array[hash_index] is not None and self._hash_array[hash_index] is not self._DUMMY:
            hash_index += hash_step * hash_step
            hash_index %= self._size
            hash_step += 1
        self._hash_array[hash_index] = item

    def delete(self, item: int) -> Optional[int]:
        hash_index, hash_step = self.hash_func(item), 1
        while self._hash_array[hash_index] is not None:
            if self._hash_array[hash_index] == item:
                result = self._hash_array[hash_index]
                self._hash_array[hash_index] = self._DUMMY
                return result
            hash_index += hash_step * hash_step
            hash_index %= self._size
            hash_step += 1
        return None

    def find(self, item) -> Optional[int]:
        hash_index, hash_step = self.hash_func(item), 1
        while self._hash_array[hash_index] is not None:
            if self._hash_array[hash_index] == item:
                return self._hash_array[hash_index]
            hash_index += hash_step * hash_step
            hash_index %= self._size
            hash_step += 1
        return None


# programming project 11.2
class StringHashTable(HashTable):
    def hash_func(self, key: str) -> int:
        result = sum(ord(char) * 27 ** index for index, char in enumerate(reversed(key)))
        return result % self._size


# programming project 11.4
class ResizebleHashTable:
    def __init__(self, size: int = 8) -> None:
        self._size = size
        self._hash_array = [None for _ in range(size)]
        self._DUMMY = float('nan')
        self._counter = 0

    def __str__(self) -> str:
        return str(self._hash_array)

    def hash_func(self, key: int) -> int:
        return key % self._size

    def resize_table(self) -> None:
        self._size *= 2
        new_hash_array = [None for _ in range(self._size)]

        for elem in self._hash_array:
            if elem is not None and elem is not self._DUMMY:
                hash_index = self.hash_func(elem)
                while new_hash_array[hash_index] is not None:
                    hash_index += 1
                    hash_index %= self._size
                new_hash_array[hash_index] = elem

        self._hash_array = new_hash_array

    def insert(self, item: int) -> None:
        if (self._counter / self._size) > 2 / 3:
            self.resize_table()
        hash_index = self.hash_func(item)
        while self._hash_array[hash_index] is not None and self._hash_array[hash_index] is not self._DUMMY:
            hash_index += 1
            hash_index %= self._size
        self._hash_array[hash_index] = item
        self._counter += 1

    def delete(self, item: int) -> Optional[int]:
        hash_index = self.hash_func(item)
        while self._hash_array[hash_index] is not None:
            if self._hash_array[hash_index] == item:
                result = self._hash_array[hash_index]
                self._hash_array[hash_index] = self._DUMMY
                self._counter -= 1
                return result
            hash_index += 1
            hash_index %= self._size
        return None

    def find(self, item) -> Optional[int]:
        hash_index = self.hash_func(item)
        while self._hash_array[hash_index] is not None:
            if self._hash_array[hash_index] == item:
                return self._hash_array[hash_index]
            hash_index += 1
            hash_index %= self._size
        return None


if __name__ == '__main__':
    data = ResizebleHashTable()
    for item in range(10, 70, 10):
        data.insert(item)
    print(data)

    data.insert(70)
    print(data)