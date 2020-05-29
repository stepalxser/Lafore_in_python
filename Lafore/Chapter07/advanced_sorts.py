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


def quick_sort_1(array: List[int]) -> None:
    left_border = 0
    right_border = len(array) - 1

    def partition(left_index: int, right_index: int, pivot: int) -> int:
        swap_index = right_index
        right_index -= 1
        while left_index <= right_index:
            while array[left_index] < pivot:
                left_index += 1
            while array[right_index] > pivot and right_index > 0:
                right_index -= 1
            if left_index <= right_index:
                array[left_index], array[right_index] = array[right_index], array[left_index]
                left_index += 1
                right_index -= 1
        right_index += 1
        array[swap_index], array[right_index] = array[right_index], array[swap_index]
        return right_index

    def rec_quick_sort(left_index=left_border, right_index=right_border) -> None:
        if left_index >= right_index:
            return
        pivot = array[right_index]
        partition_index = partition(left_index, right_index, pivot)
        rec_quick_sort(left_index, partition_index - 1)
        rec_quick_sort(partition_index + 1, right_index)

    rec_quick_sort()


def quick_sort_2(array: List[int]) -> None:
    left_border = 0
    right_border = len(array) - 1

    def median(left: int, right: int) -> int:
        center = (left + right) // 2

        if array[left] > array[center]:
            array[left], array[center] = array[center], array[left]
        if array[left] > array[right]:
            array[left], array[right] = array[right], array[left]
        if array[center] > array[right]:
            array[center], array[right] = array[right], array[center]

        array[center], array[right-1] = array[right-1], array[center]
        return array[right-1]

    def manual(left: int, right: int) -> None:
        size = right - left + 1
        if size == 1:
            return
        elif size == 2:
            if array[left] > array[right]:
                array[left], array[right] = array[right], array[left]
                return
        else:
            if array[left] > array[right - 1]:
                array[left], array[right - 1] = array[right - 1], array[left]
            if array[left] > array[right]:
                array[left], array[right] = array[right], array[left]
            if array[right - 1] > array[right]:
                array[right - 1], array[right] = array[right], array[right - 1]

    def partition(left_index: int, right_index: int, pivot: int) -> int:
        swap_index, right_index, left_index = right_index - 1, right_index - 2, left_index + 1
        while left_index <= right_index:
            while array[left_index] < pivot:
                left_index += 1
            while array[right_index] > pivot:
                right_index -= 1
            if left_index <= right_index:
                array[left_index], array[right_index] = array[right_index], array[left_index]
                left_index += 1
                right_index -= 1
        right_index += 1
        array[swap_index], array[right_index] = array[right_index], array[swap_index]
        return right_index

    def rec_quick_sort(left_index=left_border, right_index=right_border) -> None:
        if right_index - left_index + 1 <= 3:
            manual(left_index, right_index)
        else:
            pivot = median(left_index, right_index)
            partition_index = partition(left_index, right_index, pivot)
            rec_quick_sort(left_index, partition_index - 1)
            rec_quick_sort(partition_index + 1, right_index)

    rec_quick_sort()


def quick_sort_3(array: List[int]) -> None:
    left_border = 0
    right_border = len(array) - 1

    def median(left: int, right: int) -> int:
        center = (left + right) // 2

        if array[left] > array[center]:
            array[left], array[center] = array[center], array[left]
        if array[left] > array[right]:
            array[left], array[right] = array[right], array[left]
        if array[center] > array[right]:
            array[center], array[right] = array[right], array[center]

        array[center], array[right - 1] = array[right - 1], array[center]
        return array[right - 1]

    def insertion_sort(left_index: int, right_index: int) -> None:
        for outer_index in range(left_index+1, right_index+1):
            for inner_index in range(outer_index, left_index, -1):
                if array[inner_index] < array[inner_index-1]:
                    array[inner_index], array[inner_index - 1] = array[inner_index-1], array[inner_index]
                else:
                    break

    def partition(left_index: int, right_index: int, pivot: int) -> int:
        swap_index, right_index, left_index = right_index - 1, right_index - 2, left_index + 1
        while left_index <= right_index:
            while array[left_index] < pivot:
                left_index += 1
            while array[right_index] > pivot:
                right_index -= 1
            if left_index <= right_index:
                array[left_index], array[right_index] = array[right_index], array[left_index]
                left_index += 1
                right_index -= 1
        right_index += 1
        array[swap_index], array[right_index] = array[right_index], array[swap_index]
        return right_index

    def rec_quick_sort(left_index=left_border, right_index=right_border) -> None:
        if right_index - left_index + 1 <= 9:
            insertion_sort(left_index, right_index)
        else:
            pivot = median(left_index, right_index)
            partition_index = partition(left_index, right_index, pivot)
            rec_quick_sort(left_index, partition_index - 1)
            rec_quick_sort(partition_index + 1, right_index)

    rec_quick_sort()


def quick_sort_4(array: List[int]) -> List[int]:
    if len(array) <= 1:
        return array
    pivot = choice(array)
    left = [elem for elem in array if elem < pivot]
    right = [elem for elem in array if elem > pivot]
    middle = [pivot for _ in range(array.count(pivot))]
    return [*quick_sort_4(left), *middle, *quick_sort_4(right)]


if __name__ == '__main__':
    data = choices(list(range(1000)), k=54)
    data_2 = data.copy()
    shell_sort(data_2)
    assert sorted(data) == data_2

    data_3 = data.copy()
    quick_sort(data_3)
    assert sorted(data) == data_3

    data_4 = data.copy()
    quick_sort_1(data_4)
    assert sorted(data) == data_4

    data_5 = data.copy()
    print(sorted(data))
    quick_sort_2(data_5)
    print(data_5)
    assert sorted(data) == data_5

    data_6 = data.copy()
    quick_sort_3(data_6)
    assert sorted(data) == data_6

    data_7 = data.copy()
    result = quick_sort_4(data_7)
    assert sorted(data) == result
