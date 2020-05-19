# Chapter 3 Experiments 1 implementation
import time
import random
from typing import List, Callable, Tuple

from Lafore.Chapter03.sort_methods import ArrayWithSort


def test_sorts(instance: ArrayWithSort, sort_method: Callable[[ArrayWithSort], None], test_data: List[int]):
    instance._state = test_data
    time_start = time.time()
    sort_method(instance)
    time_end = time.time() - time_start
    print(f'{sort_method.__name__}: {time_end:.2f} seconds')


def test_sorts2(instance: ArrayWithSort, sort_method: Callable[[ArrayWithSort], Tuple[int, int]], test_data: List[int]):
    instance._state = test_data
    time_start = time.time()
    data = sort_method(instance)
    time_end = time.time() - time_start
    print(f'{sort_method.__name__} with result {data}: {time_end:.2f} seconds')


if __name__ == '__main__':
    array = ArrayWithSort(10000)
    # Chapter 3 Experiments 1
    test_sorts(array, ArrayWithSort.bubble_sort, random.choices(range(10000), k=10000))
    test_sorts(array, ArrayWithSort.selection_sort, random.choices(range(10000), k=10000))
    test_sorts(array, ArrayWithSort.insertion_sort, random.choices(range(10000), k=10000))

    # Chapter 3 Experiments 2
    print()
    test_sorts(array, ArrayWithSort.bubble_sort, list(range(10000, 0, -1)))
    test_sorts(array, ArrayWithSort.selection_sort, list(range(10000, 0, -1)))
    test_sorts(array, ArrayWithSort.insertion_sort, list(range(10000, 0, -1)))

    # Chapter 3 Experiments 3
    print()
    test_sorts(array, ArrayWithSort.bubble_sort, list(range(10000)))
    test_sorts(array, ArrayWithSort.selection_sort, list(range(10000)))
    test_sorts(array, ArrayWithSort.insertion_sort, list(range(10000)))

    # Chapter 3 programming project 1
    print()
    test_sorts(array, ArrayWithSort.bubble_two_way_sort, random.choices(range(10000), k=10000))
    test_sorts(array, ArrayWithSort.bubble_two_way_sort, list(range(10000, 0, -1)))
    test_sorts(array, ArrayWithSort.bubble_two_way_sort, list(range(10000)))

    # Chapter 3 programming project 5
    print()
    test_sorts2(array, ArrayWithSort.insertion_sort_with_counter, random.choices(range(10000), k=10000))
    test_sorts2(array, ArrayWithSort.insertion_sort_with_counter, list(range(10000, 0, -1)))
    test_sorts2(array, ArrayWithSort.insertion_sort_with_counter, list(range(10000)))


