from __future__ import annotations

from functools import total_ordering
from typing import List, Optional


@total_ordering
class Node:
    def __init__(self, key: int) -> None:
        self.key: int = key

    def __str__(self) -> str:
        return str(self.key)

    def __eq__(self, other: Node):
        return self.key == other.key

    def __lt__(self, other: Node):
        return self.key < other.key


class Heap:
    def __init__(self) -> None:
        self._heap_array: List[Node] = []

    def insert(self, key: int) -> None:
        new_node = Node(key)
        self._heap_array.append(new_node)
        self._trickle_up(len(self._heap_array) - 1)

    def remove(self) -> Optional[Node]:
        try:
            root = self._heap_array[0]
        except IndexError:
            return None
        self._heap_array[0] = self._heap_array.pop()
        self._trickle_down(0)
        return root

    def _trickle_up(self, index: int) -> None:
        parent = (index - 1) // 2
        bottom = self._heap_array[index]
        while index > 0 and self._heap_array[parent] < bottom:
            self._heap_array[index] = self._heap_array[parent]
            index = parent
            parent = (index - 1) // 2
        self._heap_array[index] = bottom

    def _trickle_down(self, index: int) -> None:
        top = self._heap_array[index]
        while index < len(self._heap_array) // 2:
            left_child = 2 * index + 1
            right_child = left_child + 1
            if right_child < len(self._heap_array) and self._heap_array[left_child] < self._heap_array[right_child]:
                larger_child = right_child
            else:
                larger_child = left_child

            if top > self._heap_array[larger_child]:
                break
            self._heap_array[index] = self._heap_array[larger_child]
            index = larger_child
        self._heap_array[index] = top

    def change(self, index: int, new_value: int) -> bool:
        if index < 0 or index >= len(self._heap_array):
            return False
        old_value = self._heap_array[index].key
        self._heap_array[index].key = new_value

        if old_value > new_value:
            self._trickle_down(index)
        else:
            self._trickle_up(index)

        return True

    def display(self) -> None:
        level, index = 0, 0
        print('*' * 64)
        while index + 2 ** level < len(self._heap_array) * 2:
            filler = 64 // 2 ** level
            for node_index in range(index, index + 2 ** level):
                try:
                    print(f'{str(self._heap_array[node_index]):^{filler}}', end='')
                except IndexError:
                    break
            print()
            index += 2 ** level
            level += 1
        print('*' * 64)


if __name__ == '__main__':
    data = Heap()
    for item in [70, 40, 50, 20, 60, 100, 80, 30, 10, 90]:
        data.insert(item)
        data.display()
        print(*data._heap_array)

    data.insert(53)
    data.display()
    print(data.remove())
    data.display()
