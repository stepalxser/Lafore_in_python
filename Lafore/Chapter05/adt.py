from typing import Any

from Lafore.Chapter05.linked_list import TwoWayLinkedList, LinkedList, SortedList, LoopList
from Lafore.Chapter05.doubly_linked import DoublyLinked


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

    @property
    def is_empty(self) -> bool:
        return self._state.is_empty

    def insert(self, value: Any) -> None:
        self._state.insert_last(value)

    def remove(self) -> Any:
        result = self._state.delete_first()
        return result.data

    def peek(self) -> Any:
        result = self._state.delete_first()
        self._state.insert_first(result.data)
        return result.data


# programming project 5.1
class PriorityQueue:
    def __init__(self) -> None:
        self._state = SortedList()

    def __str__(self) -> str:
        return str(self._state)

    @property
    def is_empty(self) -> bool:
        return self._state.is_empty

    def insert(self, value) -> None:
        self._state.insert(value)

    def remove(self) -> Any:
        return self._state.delete()

    def peek(self) -> Any:
        return self._state.first.data


# programming project 5.2
class Deque:
    def __init__(self) -> None:
        self._state = DoublyLinked()

    def __str__(self) -> str:
        return str(self._state)

    @property
    def is_empty(self) -> bool:
        return self._state.is_empty

    def insert_right(self, value: Any) -> None:
        self._state.insert_last(value)

    def remove_right(self) -> Any:
        return self._state.delete_last()

    def insert_left(self, value: Any) -> None:
        self._state.insert_first(value)

    def remove_left(self) -> Any:
        return self._state.delete_first()


# programming project 5.4
class LoopStack:
    def __init__(self) -> None:
        self._state = LoopList()

    def __str__(self) -> str:
        return str(self._state)

    def push(self, value: Any) -> None:
        self._state.insert(value)

    def pop(self) -> Any:
        result = self._state.delete()
        return result.data

    def peek(self) -> Any:
        return self._state.current.data

    @property
    def is_empty(self) -> bool:
        return self._state.is_empty


if __name__ == '__main__':
    print('Stack tests')
    stack = Stack()
    for item in range(10, 110, 10):
        stack.push(item)
    print(stack)
    while not stack.is_empty:
        print(stack.pop())
    print(stack, end='\n\n')

    print('Queue tests')
    queue = Queue()
    for item in range(10, 110, 10):
        queue.insert(item)
    print(queue.peek())
    print(queue)
    while not queue.is_empty:
        print(queue.remove())
    print(queue, end='\n\n')

    print('PriorityQueue tests')
    priority_queue = PriorityQueue()
    for item in range(100, 0, -10):
        priority_queue.insert(item)
    print(priority_queue)
    for _ in range(5):
        print(priority_queue.remove())
    print(priority_queue, end='\n\n')

    print('Deque tests')
    deque = Deque()
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
    print(deque, end='\n\n')

    print('LoopStack tests')
    loop_stack = LoopStack()
    for item in range(10, 110, 10):
        loop_stack.push(item)
    print(loop_stack)
    while not loop_stack.is_empty:
        print(loop_stack.pop())
    print(loop_stack, end='\n\n')
