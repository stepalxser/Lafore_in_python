from typing import List, Optional


class Stack:
    def __init__(self, size: int) -> None:
        self._size = size
        self._state: List[Optional[int]] = [None for _ in range(size)]
        self._pointer = 0

    def __str__(self) -> str:
        return str(self._state)

    def push(self, value: int) -> None:
        if self._pointer == self._size:
            raise ValueError('Stack is full')
        self._state[self._pointer] = value
        self._pointer += 1

    def pop(self) -> int:
        if not self._pointer:
            raise ValueError('Stack is empty')
        result = self._state[self._pointer-1]
        self._pointer -= 1
        return result

    def peek(self) -> int:
        if not self._pointer:
            raise ValueError('Stack is empty')
        return self._state[self._pointer-1]

    @property
    def is_empty(self) -> bool:
        return not self._pointer

    @property
    def is_full(self) -> bool:
        return self._pointer == self._size


if __name__ == '__main__':
    stack = Stack(10)
    for value in range(20, 220, 20):
        stack.push(value)

    print(stack)

    while not stack.is_empty:
        print(stack.pop())
