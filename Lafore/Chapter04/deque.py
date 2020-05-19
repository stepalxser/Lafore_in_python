from typing import List, Optional

# Chapter04 programming project 4.2
class Deque:
    def __init__(self, size: int) -> None:
        self._size = size
        self._state: List[Optional[int]] = [None for _ in range(size)]
        self._front_pointer = 0
        self._rear_pointer = 0
        self._elem_counter = 0

    def __str__(self) -> str:
        return str(self._state)

    @property
    def is_empty(self) -> bool:
        return not self._elem_counter

    @property
    def is_full(self) -> bool:
        return self._elem_counter == self._size

    def insert_right(self, value: int) -> None:
        if self._elem_counter == self._size:
            raise ValueError('Queue is full')
        if self._rear_pointer == self._size:
            self._rear_pointer = 0
        self._state[self._rear_pointer] = value
        self._rear_pointer += 1
        self._elem_counter += 1

    def remove_right(self) -> int:
        if not self._elem_counter:
            raise ValueError('Queue is empty')
        if self._rear_pointer == 0:
            self._rear_pointer = self._size
        self._rear_pointer -= 1
        result = self._state[self._rear_pointer]
        self._state[self._rear_pointer] = None
        self._elem_counter -= 1
        return result

    def insert_left(self, value: int) -> None:
        if self._elem_counter == self._size:
            raise ValueError('Queue is full')
        if self._front_pointer == 0:
            self._front_pointer = self._size
        self._front_pointer -= 1
        self._state[self._front_pointer] = value
        self._elem_counter += 1

    def remove_left(self) -> int:
        if not self._elem_counter:
            raise ValueError('Queue is empty')
        if self._front_pointer == self._size:
            self._front_pointer = 0
        result = self._state[self._front_pointer]
        self._state[self._front_pointer] = None
        self._front_pointer += 1
        self._elem_counter -= 1
        return result


if __name__ == '__main__':
    deque = Deque(10)
    for item in range(10):
        deque.insert_right(item)
    print(deque)

    deque.remove_left()
    deque.remove_right()
    print(deque)

    deque.remove_left()
    deque.remove_right()
    print(deque)

    deque.insert_right(10)
    deque.insert_right(20)
    deque.insert_right(30)
    print(deque)

    deque.remove_right()
    deque.remove_right()
    deque.remove_right()
    print(deque)

    deque.insert_left(-10)
    deque.insert_left(-20)
    deque.insert_left(-30)
    print(deque)

    deque.remove_left()
    deque.remove_left()
    deque.remove_left()
    print(deque)


