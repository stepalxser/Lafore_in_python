from typing import Optional, List


class Array:
    def __init__(self, length: int) -> None:
        self._state: List[Optional[int]] = [None for _ in range(length)]
        self._length: int = length
        self._pointer: int = 0

    def __str__(self) -> str:
        return str(self._state)

    def size(self) -> int:
        return self._length

    def find(self, value: int) -> Optional[int]:
        for index in range(self._length):
            if self._state[index] == value:
                return index
        return None

    def insert(self, value: int) -> None:
        if self._pointer == self._length:
            raise ValueError('maximum items reached')
        self._state[self._pointer] = value
        self._pointer += 1

    def delete(self, value: int) -> bool:
        elem_index = self.find(value)
        if elem_index is None:
            return False

        self._state[elem_index] = None
        self._pointer -= 1

        for index in range(elem_index + 1, self._length):
            if self._state[index] is not None:
                self._state[index], self._state[index - 1] = self._state[index - 1], self._state[index]
            else:
                break
        return True

    def no_dups(self) -> None:
        unuqie_elements: Array = Array(self._length)
        for index in range(self._length):
            if unuqie_elements.find(self._state[index]) is None:
                unuqie_elements.insert(self._state[index])
        self._state = unuqie_elements._state


class ArrayWithMax(Array):
    def get_max(self) -> Optional[int]:
        if self._state[0] is None:
            return None

        result = float('-inf')
        for index in range(self._length):
            if self._state[index] is None:
                return result
            result = result if result > self._state[index] else self._state[index]
        return result

    def remove_max(self) -> Optional[int]:
        if self._state[0] is None:
            return None

        result = float('-inf')
        for index in range(self._length):
            if self._state[index] is None:
                break
            result = result if result > self._state[index] else self._state[index]

        self.delete(result)
        return result


if __name__ == '__main__':
    array = Array(10)
    array.insert(77)
    array.insert(99)
    array.insert(44)
    array.insert(55)
    array.insert(22)
    array.insert(88)
    array.insert(11)
    array.insert(00)
    array.insert(66)
    array.insert(33)
    print(array)
    print(array.find(55))
    array.delete(00)
    print(array)
    array.delete(55)
    array.delete(100)
    array.delete(99)
    print(array)

    array = ArrayWithMax(10)
    array.insert(77)
    array.insert(99)
    array.insert(44)
    array.insert(55)
    array.insert(22)
    array.insert(88)
    array.insert(11)
    array.insert(00)
    array.insert(99)
    array.insert(33)
    print(array)
    assert array.get_max() == 99
    print(array)

# 2.3 programming project
    sorted_array = ArrayWithMax(array.size())
    for _ in range(array.size()):
        if array.get_max() is None:
            break
        sorted_array.insert(array.remove_max())
    print(sorted_array)
    sorted_array.no_dups()
    print(sorted_array)
