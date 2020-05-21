from typing import Any

from Lafore.Chapter05.linked_list import TwoWayLinkedList, LinkedList


class Stack:
    def __init__(self) -> None:
        self._state = LinkedList()

    def __str__(self) -> str:
        return str(self._state)

    def push(self, value: Any) -> None:
        self._state.insert_first(value)

    def pop(self) -> Any:
        result = self._state.delete_first()
        return result.data

    def peek(self) -> Any:
        result = self._state.delete_first()
        self._state.insert_first(result.data)
        return result.data

    @property
    def is_empty(self) -> bool:
        return self._state.is_empty


class Queue:
    def __init__(self) -> None:
        self._state = TwoWayLinkedList()

    def __str__(self) -> str:
        return str(self._state)

    def insert(self, value: Any) -> None:
        self._state.insert_last(value)

    def remove(self) -> Any:
        result = self._state.delete_fisrt()
        return result.data

    def peek(self) -> Any:
        result = self._state.delete_fisrt()
        self._state.insert_first(result.data)
        return result.data

    @property
    def is_empty(self) -> bool:
        return self._state.is_empty


if __name__ == '__main__':
    stack = Stack()
    for item in range(10, 110, 10):
        stack.push(item)
    print(stack)
    while not stack.is_empty:
        print(stack.pop())
    print(stack)

    queue = Queue()
    for item in range(10, 110, 10):
        queue.insert(item)
    print(queue.peek())
    print(queue)
    while not queue.is_empty:
        print(queue.remove())
    print(queue)




