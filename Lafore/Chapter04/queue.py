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
            self._elem_counter += 1
        else:
            insert_index = 0
            for index in range(self._elem_counter-1, -1, -1):
                if value > self._state[index]:
                    self._state[index+1] = self._state[index]
                else:
                    insert_index = index
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


if __name__ == '__main__':
    # queue = Queue(10)
    # for value in range(10, 110, 10):
    #     queue.insert(value)
    # print(queue)
    # for _ in range(5):
    #     print(queue.remove())
    # print(queue)
    #
    # for value in range(3):
    #     queue.insert(value)
    #
    # print(queue)
    # for _ in range(6):
    #     print(queue.remove())
    # print(queue)

    pqueue = PriorityQueue(10)
    for value in range(10):
        pqueue.insert(value)
    print(pqueue)

    while not pqueue.is_empty:
        print(pqueue.remove())

    print(pqueue)