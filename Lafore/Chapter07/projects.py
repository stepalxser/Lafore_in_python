from random import choices
from typing import List


# 7.3 programming project
def find_median(array: List[int]) -> int:
    median_index = len(array) // 2
    left_border = 0
    right_border = len(array) - 1

    def partition(left_index: int, right_index: int) -> int:
        swap_index, right_index = right_index, right_index-1
        pivot = array[swap_index]
        while left_index <= right_index:
            while left_index < right_border and array[left_index] < pivot:
                left_index += 1
            while right_index > left_border and array[right_index] > pivot:
                right_index -= 1
            if left_index <= right_index:
                array[left_index], array[right_index] = array[right_index], array[left_index]
                left_index += 1
                right_index -= 1
        array[left_index], array[swap_index] = array[swap_index], array[left_index]
        return left_index

    def median(left_index, right_index) -> int:
        index = partition(left_index, right_index)
        if index == median_index:
            return array[index]
        if index > median_index:
            return median(left_border, index-1)
        if index < median_index:
            return median(index+1, right_border)

    return median(left_border, right_border)


# 7.4 programming project
def find_index(array: List[int], search_index) -> int:
    left_border = 0
    right_border = len(array) - 1

    def partition(left_index: int, right_index: int) -> int:
        swap_index, right_index = right_index, right_index - 1
        pivot = array[swap_index]
        while left_index <= right_index:
            while left_index < right_border and array[left_index] < pivot:
                left_index += 1
            while right_index > left_border and array[right_index] > pivot:
                right_index -= 1
            if left_index <= right_index:
                array[left_index], array[right_index] = array[right_index], array[left_index]
                left_index += 1
                right_index -= 1
        array[left_index], array[swap_index] = array[swap_index], array[left_index]
        return left_index

    def median(left_index, right_index) -> int:
        index = partition(left_index, right_index)
        if index == search_index:
            return array[index]
        if index > search_index:
            return median(left_border, index - 1)
        if index < search_index:
            return median(index + 1, right_border)

    return median(left_border, right_border)


if __name__ == '__main__':
    data = choices(range(100), k=11)
    print(data)
    print(sorted(data))
    print(sorted(data)[5])
    print(find_median(data))
    print(data)
    print('end')

    data = choices(range(100), k=11)
    print(data)
    print(sorted(data))
    index = 7
    print(sorted(data)[index])
    print(find_index(data, index))
    print(data)
    print('end')