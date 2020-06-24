from typing import List, Optional
from Lafore.Chapter12.max_heap import Node, Heap


# programming project 12.1
class MinHeap(Heap):
    def _trickle_up(self, index: int) -> None:
        parent = (index - 1) // 2
        bottom = self._heap_array[index]
        while index > 0 and self._heap_array[parent] > bottom:
            self._heap_array[index] = self._heap_array[parent]
            index = parent
            parent = (index - 1) // 2
        self._heap_array[index] = bottom

    def _trickle_down(self, index: int) -> None:
        top = self._heap_array[index]
        while index < len(self._heap_array) // 2:
            left_child = 2 * index + 1
            right_child = left_child + 1
            if right_child < len(self._heap_array) and self._heap_array[left_child] > self._heap_array[right_child]:
                larger_child = right_child
            else:
                larger_child = left_child

            if top < self._heap_array[larger_child]:
                break
            self._heap_array[index] = self._heap_array[larger_child]
            index = larger_child
        self._heap_array[index] = top


if __name__ == '__main__':
    data = MinHeap()
    for item in [70, 40, 50, 20, 60, 100, 80, 30, 10, 90]:
        data.insert(item)
        data.display()
        print(*data._heap_array)

    data.insert(53)
    data.display()
    print(data.remove())
    data.display()
