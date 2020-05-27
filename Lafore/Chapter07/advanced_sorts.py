from random import choices, choice
from typing import List, Optional


def shell_sort(array: List[int]) -> None:
    gap = 1
    while gap <= len(array) // 3:
        gap = gap * 3 + 1

    while gap:
        for index in range(gap, len(array)):
            temp_index = index
            while temp_index >= gap and array[temp_index-gap] > array[temp_index]:
                array[temp_index], array[temp_index-gap] = array[temp_index-gap], array[temp_index]
                temp_index -= gap

        gap = (gap - 1) // 3


def partition(array: List[int], left: int = 0, right: Optional[int] = None, pivot: Optional[int] = None) -> int:
    right = len(array) - 1 if right is None else right
    pivot = choice(array) if pivot is None else pivot
    left_index = left
    right_index = right
    while left_index <= right_index:
        while array[left_index] < pivot:
            left_index += 1
        while array[right_index] > pivot:
            right_index -= 1
        if left_index <= right_index:
            array[left_index], array[right_index] = array[right_index], array[left_index]
            left_index += 1
            right_index -= 1
    return right_index + 1


def quick_sort(array, left=0, right=None):
    right = len(array) - 1 if right is None else right
    if left >= right:
        return
    else:
        pivot = choice(array[left:right + 1])
        left_index = left
        right_index = right
        while left_index <= right_index:
            while array[left_index] < pivot:
                left_index += 1
            while array[right_index] > pivot:
                right_index -= 1
            if left_index <= right_index:
                array[left_index], array[right_index] = array[right_index], array[left_index]
                left_index += 1
                right_index -= 1
                quick_sort(array, left, right_index)
                quick_sort(array, left_index, right)


if __name__ == '__main__':
    data = choices(list(range(100)), k=20)
    data_2 = data.copy()
    shell_sort(data_2)
    assert sorted(data) == data_2

    data_3 = data.copy()
    quick_sort(data_3)
    print(data_3)
    assert sorted(data) == data_3


