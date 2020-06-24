# programming project 12.4
from random import randint
from typing import Optional

from Lafore.Chapter08.binary_tree import Tree


class PriorityTree(Tree):
    def remove_max(self) -> Optional[int]:
        current = self._root
        while current.right is not None:
            current = current.right
        if current is self._root:
            result = self._root.value
            self._root = self._root.left
            return result
        elif current is not None:
            result = current.value
            self.delete(result)
            return result
        else:
            return None


class PriorityQueue:
    def __init__(self):
        self._state = PriorityTree()

    def insert(self, value) -> None:
        self._state.insert(value)

    def remove(self) -> Optional[int]:
        return self._state.remove_max()

    def peek(self) -> Optional[int]:
        result = self._state.remove_max()
        self.insert(result)
        return result


if __name__ == '__main__':
    print('PrioriryTree test')
    print('insert test')
    data = PriorityTree()
    for item in 50, 25, 75, 12, 37, 43, 30, 33, 87, 93, 94:
        data.insert(item)
    data.display()

    print('remove_max with root test')
    for _ in range(5):
        print(data.remove_max(), end=' ')
    print()
    data.display()

    print('PriorityQueue test')
    data = PriorityQueue()
    for item in 50, 25, 75, 12, 37, 43, 30, 33, 87, 93, 94:
        data.insert(item)
    for _ in range(10):
        print(data.remove(), end=' ')