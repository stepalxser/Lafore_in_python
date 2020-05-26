from __future__ import annotations

from typing import List


def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if right[right_index] < left[left_index]:
            result.append(right[right_index])
            right_index += 1
        else:
            result.append(left[left_index])
            left_index += 1
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1
    return result


def merge_sort(array: List[int]) -> List[int]:
    if len(array) == 1:
        return array[:]
    else:
        mid_index = len(array) // 2
        left = merge_sort(array[:mid_index])
        right = merge_sort(array[mid_index:])
        return merge(left, right)


if __name__ == '__main__':
    array = list(range(100, 0, -1))
    array = merge_sort(array)
    print(array)

