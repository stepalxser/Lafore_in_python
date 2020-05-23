from typing import List, Optional


class Queue:
    def __init__(self, size: int) -> None:
        self._size = size
        self._state: List[Optional[int]] = [None for _ in range(size)]
        self._front_pointer = 0
        self._rear_pointer = 0
        self._elem_counter = 0

    def __str__(self) -> str:
        return str(self._state)

    def insert(self, value: int) -> None:
        if self._elem_counter == self._size:
            raise ValueError('Queue is full')
        if self._rear_pointer == self._size:
            self._rear_pointer = 0
        self._state[self._rear_pointer] = value
        self._rear_pointer += 1
        self._elem_counter += 1

    def remove(self) -> int:
        if not self._elem_counter:
            raise ValueError('Queue is empty')
        if self._front_pointer == self._size:
            self._front_pointer = 0
        result = self._state[self._front_pointer]
        self._state[self._front_pointer] = None
        self._front_pointer += 1
        self._elem_counter -= 1
        return result

    def peek(self) -> int:
        if self._elem_counter:
            raise ValueError('Queue is empty')
        return self._state[self._front_pointer]

    @property
    def is_empty(self) -> bool:
        return not self._elem_counter

    @property
    def is_full(self) -> bool:
        return self._elem_counter == self._size

    # chapter04 programming project 4.1
    def display(self) -> None:
        if self._rear_pointer > self._front_pointer:
            print(*self._state[self._front_pointer:self._rear_pointer], sep=' ')
        else:
            print(*self._state[self._front_pointer:], sep=' ', end=' ')
            print(*self._state[0:self._rear_pointer], sep=' ')


# Chapter04 programming project 4.4
class PriorityQueue:
    def __init__(self, size: int) -> None:
        self._size = size
        self._state: List[Optional[int]] = [None for _ in range(size)]
        self._elem_counter = 0

    def __str__(self) -> str:
        return str(self._state)

    @property
    def is_empty(self) -> bool:
        return not self._elem_counter

    @property
    def is_full(self) -> bool:
        return self._elem_counter == self._size

    def insert(self, value) -> None:
        if self._elem_counter == 0:
            self._state[self._elem_counter] = value
        else:
            insert_index = 0
            for index in range(self._elem_counter-1, -1, -1):
                if value > self._state[index]:
                    self._state[index+1] = self._state[index]
                else:
                    insert_index = index + 1
                    break
            self._state[insert_index] = value
        self._elem_counter += 1

    def remove(self) -> int:
        result = self._state[self._elem_counter-1]
        self._state[self._elem_counter-1] = None
        self._elem_counter -= 1
        return result

    def peek(self) -> int:
        return self._state[self._elem_counter]


class FastQueue:
    def __init__(self, size: int) -> None:
        self._size = size
        self._state: List[Optional[int]] = [None for _ in range(size)]
        self._elem_counter = 0

    def __str__(self) -> str:
        return str(self._state)

    @property
    def is_empty(self) -> bool:
        return not self._elem_counter

    @property
    def is_full(self) -> bool:
        return self._elem_counter == self._size

    def insert(self, value) -> None:
        self._state[self._elem_counter] = value
        self._elem_counter += 1

    def remove(self) -> int:
        remove_index, min_elem = 0, float('+inf')
        for index in range(self._elem_counter):
            if self._state[index] > min_elem:
                remove_index = index
        result = self._state[remove_index]
        self._state[remove_index] = None
        for index in range(remove_index+1, self._elem_counter):
            self._state[index], self._state[index-1] = self._state[index-1], self._state[index]
        self._elem_counter -= 1
        return result

    def peek(self) -> int:
        remove_index, min_elem = 0, float('+inf')
        for index in range(self._elem_counter):
            if self._state[index] > min_elem:
                remove_index = index
        return self._state[remove_index]


if __name__ == '__main__':
    queue = Queue(10)
    for item in range(10):
        queue.insert(item)
    queue.display()

    for _ in range(5):
        queue.remove()
    queue.display()

    for item in range(10, 15):
        queue.insert(item)
    queue.display()

    fast_queue = FastQueue(10)
    for item in range(1, 11):
        fast_queue.insert(item)
    print(fast_queue)
    fast_queue.remove()
    fast_queue.remove()
    fast_queue.remove()
    print(fast_queue)

    priority_queue = PriorityQueue(10)
    for item in range(100, 0, -10):
        priority_queue.insert(item)
    print(priority_queue)
    for _ in range(5):
        print(priority_queue.remove())
    print(priority_queue)