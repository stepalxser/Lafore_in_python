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
        array[swap_index], array[left_index] = array[left_index], array[swap_index]

        return right_index + 1

    def median(left_index, right_index) -> int:
        if right_index - left_index <= 1:
            return array[right_index]
        index = partition(left_index, right_index)
        if index == median_index:
            return array[index]
        elif index > median_index:
            median(left_border, index-1)
        else:
            median(index+1, right_border)

    return median(left_border, right_border)


if __name__ == '__main__':
    data = choices(range(100), k=7)
    print(data)
    print(sorted(data))
    print(sorted(data)[3])
    print(find_median(data))
    print(data)
    print('end')






